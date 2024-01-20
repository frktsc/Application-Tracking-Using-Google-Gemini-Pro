from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import PyPDF2 as pdf
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_response(input,pdf_content,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=" "
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
    

st.set_page_config(page_title="ATS Resume EXpert")
st.header("Resume Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("Percentage match")

submit3=st.button("write a cover letter")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
    Hey Act Like a skilled or very experience ATS(Application Tracking System)
    with a deep understanding of tech field,software engineering,data science ,data analyst
    and big data engineer. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide 
    best assistance for improving thr resumes.
    Also, examine the resume carefully and do not consider anything on the resume as a missing match.
    Assign the percentage Matching based 
    on Job describtion and
    the missing keywords with high accuracy
    resume:{text}
    description:{jd}

    I want the response in one single string having the structure
    {{"JD Match":"%",
    "MissingKeywords:[]",
    "Profile Summary":""}}
"""

input_prompt3 = """
We will give you the requirements of the company and the resume of the person who wants to apply.You will review the resume and write a cover letter in accordance with the job description.
If you do not see the job experience section in the CV, write cover letter as if you are someone who is willing to improve in that field, not as if you are experienced.
Examine the uploaded CV carefully and do not write anything that is not there.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_text(uploaded_file)
        response=get_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_text(uploaded_file)
        response=get_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
        
elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_text(uploaded_file)
        response=get_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")