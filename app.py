# -*- coding: utf-8 -*-
import streamlit as st
from groq import Groq
# ... დანარჩენი კოდი იგივე დარჩესimport streamlit as st
from groq import Groq

st.set_page_config(page_title="Mixit - AI მზარეული", page_icon="🍳")
st.title("🍳 თქვენი AI მზარეული")

try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
    
    st.write("ჩაწერეთ რა ინგრედიენტები გაქვთ და მე მოგიფიქრებთ რეცეპტს!")
    ingredients = st.text_input("ინგრედიენტები (მაგ: კვერცხი, ყველი, პომიდორი):")

    if st.button("რეცეპტის მომზადება"):
        if ingredients:
            with st.spinner('AI ფიქრობს...'):
                try:
                    # აი აქ ჩავასწორეთ მოთხოვნა
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "შენ ხარ პროფესიონალი ქართველი მზარეული. უპასუხე მხოლოდ ქართულად."},
                            {"role": "user", "content": str(ingredients)} # ვაქცევთ ტექსტად მკაცრად
                        ],
                    )
                    st.success("აი თქვენი რეცეპტი:")
                    st.write(completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"AI შეცდომა: {e}")
        else:
            st.warning("გთხოვთ, ჩაწეროთ ინგრედიენტები.")

except Exception as e:
    st.error("გთხოვთ, შეამოწმოთ API Key საიტის Secrets-ში.")
