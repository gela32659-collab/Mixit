import streamlit as st
from groq import Groq

# საიტის კონფიგურაცია
st.set_page_config(page_title="AI მზარეული", page_icon="🍳")
st.title("🍳 თქვენი AI მზარეული")

# API Key-ს ავტომატური წაკითხვა Secrets-დან
try:
    # აქ ვიყენებთ იმ სახელს, რაც Secrets-ში დავარქვით
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
    
    st.write("ჩაწერეთ რა ინგრედიენტები გაქვთ და მე მოგიფიქრებთ რეცეპტს!")
    
    ingredients = st.text_input("ინგრედიენტები (მაგ: ქათამი, ხახვი, ნიორი):")

    if st.button("რეცეპტის მომზადება"):
        if ingredients:
            with st.spinner('AI ფიქრობს...'):
                try:
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "შენ ხარ პროფესიონალი ქართველი მზარეული. უპასუხე მხოლოდ ქართულად."},
                            {"role": "user", "content": f"მაქვს ეს ინგრედიენტები: {ingredients}. გთხოვ, მომიძებნო საუკეთესო რეცეპტი."}
                        ],
                    )
                    st.success("აი თქვენი რეცეპტი:")
                    st.write(completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"AI-სთან დაკავშირების შეცდომა: {e}")
        else:
            st.warning("გთხოვთ, ჯერ ჩაწეროთ ინგრედიენტები.")

except Exception as e:
    st.error("API Key ვერ მოიძებნა. დარწმუნდით, რომ Secrets-ში სწორად ჩაწერეთ GROQ_API_KEY.")
    st.info("ინსტრუქცია: Settings > Secrets > ჩაწერეთ: GROQ_API_KEY = 'თქვენი_კოდი'")
