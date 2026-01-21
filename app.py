import subprocess
import sys

# ეს კოდი თავად დააინსტალირებს Groq-ს, თუ ის არ არის სისტემაში
try:
    from groq import Groq
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "groq"])
    from groq import Groq

import streamlit as st

# საიტის სათაური
st.set_page_config(page_title="AI მზარეული", page_icon="🍳")
st.title("🍳 თქვენი AI მზარეული")

# API Key-ს შეყვანა
api_key = st.sidebar.text_input("შეიყვანეთ თქვენი Groq API Key:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        ingredients = st.text_input("მაგალითად: კვერცხი, ყველი, პომიდორი")

        if st.button("რეცეპტის მომზადება"):
            if ingredients:
                with st.spinner('ვფიქრობ...'):
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "შენ ხარ პროფესიონალი მზარეული. უპასუხე ქართულად."},
                            {"role": "user", "content": f"მაქვს ეს ინგრედიენტები: {ingredients}. რისი მომზადება შემიძლია?"}
                        ],
                    )
                    st.success("აი თქვენი რეცეპტი:")
                    st.write(completion.choices[0].message.content)
            else:
                st.warning("გთხოვთ, ჩაწეროთ ინგრედიენტები.")
    except Exception as e:
        st.error(f"მოხდა შეცდომა: {e}")
else:
    st.info("გთხოვთ, შეიყვანოთ Groq API Key გვერდითა პანელში.")
