import streamlit as st
from chains import summarize_text

st.title("📑 AI สรุปการประชุมจากข้อความ (Groq Llama)")
user_input = st.text_area("✍️ กรอกข้อความการประชุมที่ต้องการสรุป", height=200)

if st.button("📝 สร้างสรุป"):
    if user_input.strip():
        st.write("⏳ กำลังสรุปข้อความ...")
        summary = summarize_text(user_input)
        st.success("✅ สรุปเสร็จเรียบร้อย!")
        st.text_area("📌 สรุปประเด็นสำคัญ", summary, height=150)
    else:
        st.warning("⚠️ กรุณากรอกข้อความก่อนกดสรุป!")