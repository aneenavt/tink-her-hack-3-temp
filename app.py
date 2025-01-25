import streamlit as st
import google.generativeai as genai
import os

# Load environment variables from .env file (if it exists)
load_dotenv()

# Ensure you are securely loading the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is set properly
if api_key is None:
    st.error("API key is missing! Please set the GEMINI_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

    # Enhanced system instruction for a mental health chatbot
    system_instruction = """
    You are a compassionate and empathetic mental health chatbot designed to provide emotional support. 
    Your role is to listen without judgment, offer understanding, and respond with kindness and empathy. 
    You should acknowledge the user's feelings, ask open-ended questions when appropriate, and gently guide them through their emotions. 
    You are not a licensed therapist, but you aim to create a safe space for the user to express themselves. 
    Provide soothing and thoughtful responses, and offer resources or encourage seeking professional help if the user expresses severe distress.
    """

    # Initialize the model with the instruction
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction)

    # Streamlit app UI
    st.title("Mental Health Support Chatbot")
    st.write("Welcome to the Mental Health Support Chatbot! I'm here to listen and offer support. How are you feeling today?")

    # Store conversation history in session state
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # User input
    user_input = st.text_area("Enter your message:")

    # Generate response when user submits
    if st.button("Submit"):
        if user_input:
            try:
                # Append user input to conversation history
                st.session_state["conversation"].append({"user": user_input})

                # Construct the full conversation history as input for the model
                full_conversation = ""
                for message in st.session_state["conversation"]:
                    if "user" in message:
                        full_conversation += f"User: {message['user']}\n"
                    if "chatbot" in message:
                        full_conversation += f"Chatbot: {message['chatbot']}\n"

                # Generate the response from the AI model using the full conversation
                response = model.generate_content(full_conversation)

                # Append the chatbot's response to conversation history
                st.session_state["conversation"].append({"chatbot": response.text})

                # Show the full conversation so far
                for message in st.session_state["conversation"]:
                    if "user" in message:
                        st.write(f"**You:** {message['user']}")
                    if "chatbot" in message:
                        st.write(f"**Chatbot:** {message['chatbot']}")

            except Exception as e:
                st.error(f"Error generating response: {e}")
        else:
            st.write("Please enter something so I can respond.")
