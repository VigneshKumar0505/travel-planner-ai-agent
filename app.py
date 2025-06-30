import streamlit as st
import openai

st.title("AI Travel Planner Assistant")

openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

user_input = st.text_area("Ask your travel question or describe your trip:")

if st.button("Get Suggestion"):
    if not openai_api_key or not user_input:
        st.warning("Please enter your API key and your query.")
    else:
        openai.api_key = openai_api_key
        prompt = (
            "You are a helpful travel planner assistant. "
            "Answer questions, suggest itineraries, and give travel advice:\n"
            + user_input
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a travel planner AI assistant."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=400,
        )
        st.markdown("**Assistant:** " + response['choices'][0]['message']['content'])

st.info("Sample queries: 'Suggest a 5-day itinerary for Kerala', 'Best time to visit Japan', etc.")
