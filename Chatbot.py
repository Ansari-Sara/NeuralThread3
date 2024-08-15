import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "Api Key"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Choose the model you want to use
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Streamlit app
def main():
    st.title("OpenAI Chatbot")
    st.write("Enter your message below to chat with the AI.")

    # Create a text input field for user input
    user_input = st.text_input("You: ", "")

    if user_input:
        # Generate the chatbot response
        bot_response = generate_response(user_input)

        # Display the chatbot response
        st.write(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()

