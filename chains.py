
from langchain_groq import ChatGroq
import os

# ตั้งค่าโมเดล LLM จาก Groq
llm = ChatGroq(
    temperature=0,
    groq_api_key= "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",
    model_name="llama-3.3-70b-versatile"
)

# ฟังก์ชันสร้างสรุปจากข้อความโดยใช้ Groq Llama
def summarize_text(text):
    prompt = f"""
    คุณคือ AI ผู้ช่วยที่สามารถสรุปการประชุมได้อย่างมีประสิทธิภาพ
    โปรดสรุปเนื้อหาต่อไปนี้เป็น 3-5 ประเด็นสำคัญ พร้อมยกตัวอย่างเป็นไอเดียใหม่:

    {text}
    """
    response = llm.invoke(prompt)
    return response.content  # ดึงข้อความที่ได้จากโมเดล