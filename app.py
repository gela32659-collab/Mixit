import streamlit as st
from groq import Groq

# საიტის სათაური და დიზაინი
st.set_page_config(page_title="AI მზარეული", page_icon="🍳")
st.title("🍳 თქვენი AI მზარეული")
st.write("ჩაწერეთ რა ინგრედიენტები გაქვთ და მე მოგიფიქრებთ რეცეპტს!")

# API Key-ს შეყვანა (უსაფრთხოებისთვის)
api_key = st.sidebar.text_input("შეიყვანეთ თქვენი Groq API Key:", type="password")

if api_key:
    client = Groq(api_key=api_key)
    
    # ინგრედიენტების ველი
    ingredients = st.text_input("მაგალითად: კვერცხი, ყველი, პომიდორი")

    if st.button("რეცეპტის მომზადება"):
        if ingredients:
            with st.spinner('ვფიქრობ...'):
                try:
                    # AI-სთვის გაგზავნილი მოთხოვნა
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "შენ ხარ პროფესიონალი მზარეული. მომხმარებელი გეტყვის რა ინგრედიენტები აქვს, შენ კი უნდა შესთავაზო მხოლოდ ისეთი რეცეპტები, რომელთა მომზადებაც ამ ინგრედიენტებითაა შესაძლებელი. უპასუხე ქართულ ენაზე."},
                            {"role": "user", "content": f"მაქვს ეს ინგრედიენტები: {ingredients}. რისი მომზადება შემიძლია?"}
                        ],
                    )
                    
                    # პასუხის გამოტანა
                    st.success("აი თქვენი რეცეპტი:")
                    st.write(completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"მოხდა შეცდომა: {e}")
        else:
            st.warning("გთხოვთ, ჩაწეროთ ინგრედიენტები.")
else:
    st.info("გთხოვთ, შეიყვანოთ Groq API Key გვერდითა პანელში მუშაობის დასაწყებად.")
