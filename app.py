import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI მზარეული", page_icon="🍳")
st.title("🍳 თქვენი AI მზარეული")

api_key = st.sidebar.text_input("შეიყვანეთ თქვენი Groq API Key:", type="password")

if api_key:
    client = Groq(api_key=api_key)
    ingredients = st.text_input("მაგალითად: კვერცხი, ყველი, პომიდორი")

    if st.button("რეცეპტის მომზადება"):
        if ingredients:
            with st.spinner('ვფიქრობ...'):
                try:
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "შენ ხარ პროფესიონალი მზარეული. უპასუხე ქართულად."},
                            {"role": "user", "content": f"მაქვს ეს ინგრედიენტები: {ingredients}. რისი მომზადება შემიძლია?"}
                        ],
                    )
                    st.success("აი თქვენი რეცეპტი:")
                    st.write(completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"შეცდომა: {e}")
else:
    st.info("შეიყვანეთ API Key გვერდითა პანელში.")
