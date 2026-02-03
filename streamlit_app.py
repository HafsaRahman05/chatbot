import streamlit as st
from openai import OpenAI, RateLimitError, AuthenticationError
from openai.error import RateLimitError, AuthenticationError

st.title("💬 Chatbot")
st.write(
    "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys)."
)

# Ask user for their OpenAI API key
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    # Create OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Initialize session state for chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What is up?"):
        # Store user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response with error handling
        try:
            # Streamed response
            response_text = ""
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )

            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                # Collect and display streamed content
                for chunk in stream:
                    delta = chunk.choices[0].delta.get("content", "")
                    response_text += delta
                    response_placeholder.markdown(response_text)

            # Save assistant message
            st.session_state.messages.append({"role": "assistant", "content": response_text})

        except RateLimitError:
            st.error("⚠️ OpenAI quota exceeded. Please try again later.")
        except AuthenticationError:
            st.error("⚠️ Invalid API key. Please check your key and try again.")
        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {e}")
