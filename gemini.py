import google.generativeai as genai
import os

# Set your API key securely
from dotenv import load_dotenv
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

# Get user input
prompt = input("Enter prompt: ")

# Generate a response
response = model.generate_content(prompt)

# Print the response
print(f"{response.text}")
