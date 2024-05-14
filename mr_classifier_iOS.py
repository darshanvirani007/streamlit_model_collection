import streamlit as st
import os
import pandas as pd
import re
import distutils
from PyPDF2 import PdfReader
import json


# Positive and negative symptoms lists
positive_symptoms = [
    "Further evaluation recommended for detected polyp.",
    "Mild inflammation noted, likely due to diverticulosis.",
    "Polyp removed and submitted for histopathological examination.",
    "Biopsy specimens obtained for further analysis.",
    "Follow-up colonoscopy recommended based on clinical findings.",
    "Biopsies taken from suspicious areas for pathological assessment.",
    "Polyp resected completely, no residual tissue observed.",
    "Polypoid lesions excised completely, no residual tissue present.",
    "Tissue samples collected for histological analysis.",
    "Tissue samples sent for pathological examination.",
    "Results pending",
    "No evidence of active bleeding or vascular abnormalities seen.",
    "No evidence of active inflammation or other acute abnormalities seen.",
    "No significant deviations from expected findings, no further intervention required.",
    "Polyps removed successfully, no complications encountered during the procedure.",
    "No concerning features noted, patient advised to maintain regular follow-up appointments.",
    "Colonoscopy results within expected range, no significant abnormalities detected.",
    "Tissue samples obtained for pathological assessment, results pending.",
    "Colonoscopy results within normal limits, no worrisome findings detected.",
    "Normal post-procedure impression, patient discharged home.",
    "No significant pathology identified, routine follow-up recommended.",
    "Impression unchanged from previous exams, no new concerns.",
    "Colonoscopy findings stable, no evidence of disease recurrence.",
    "Impression benign, no indication of significant mucosal abnormalities.",
    "No concerning lesions identified, patient advised to continue regular care.",
    "No need for immediate intervention, plan for routine follow-up.",
    "Impression normal, no evidence of significant colonic disease.",
    "Colonoscopy findings unremarkable, no new abnormalities detected.",
    "No features concerning for high-grade dysplasia or malignancy.",
    "Polyps removed completely, no residual adenomas visualized.",
    "No signs of procedural complications observed.",
    "Impression consistent with benign colorectal findings.",
    "Colonoscopy results negative for significant pathology.",
    "Findings consistent with normal colonic mucosa.",
    "No significant deviations from expected findings, no further intervention required.",
    "Polyps removed successfully, no complications encountered during the procedure.",
    "No concerning features noted, patient advised to maintain regular follow-up appointments.",
    "Colonoscopy results within expected range, no significant abnormalities detected.",
    "No evidence of dysplasia or malignancy, patient advised to continue surveillance as scheduled."
    # Your positive symptoms list here
]

negative_symptoms = [
    "No significant abnormalities detected.",
    "Normal colonoscopy findings, no further action required.",
    "Impression consistent with routine colonoscopic examination.",
    "No concerning pathology identified, follow-up not necessary.",
    "Benign findings observed, no need for additional intervention.",
    "Colonoscopy results negative for significant abnormalities.",
    "No evidence of malignancy detected, routine surveillance recommended.",
    "No concerning features identified, ongoing surveillance advised.",
    "No acute abnormalities detected, continue with standard care.",
    "Normal post-procedure impression, no complications identified.",
    "Impression consistent with expected post-procedure course.",
    "No suspicious lesions seen, regular screening advised.",
    "No pathology requiring immediate attention identified.",
    "Colonoscopy results reassuring, no further action needed.",
    "No concerning features noted, plan for routine follow-up.",
    "No acute abnormalities seen, continue with standard follow-up.",
    "Impression normal, no pathology requiring further investigation.",
    "Colonoscopy results negative for high-risk lesions.",
    "No need for immediate intervention, continue with standard care.",
    "Impression unremarkable, no need for immediate intervention.",
    "No evidence of inflammatory bowel disease detected.",
    "Impression unchanged from prior examinations, no new pathology identified.",
    "No evidence of dysplasia or carcinoma detected.",
    "No evidence of ischemia or vascular abnormalities detected.",
    "Impression benign, no indication of significant pathology.",
    "No features suggestive of advanced neoplasia seen.",
    "No evidence of dysplasia or malignancy, continue with regular surveillance.",
    "Normal post-procedure impression, patient can resume normal activities.",
    "No features suggestive of advanced neoplasia seen.",
    "No evidence of malignancy or dysplasia, continue with routine surveillance.",
    "Normal post-procedure impression, patient discharged home.",
    "No significant pathology identified, routine follow-up recommended.",
    "Impression unchanged from previous exams, no new concerns.",
    "Colonoscopy findings stable, no evidence of disease recurrence.",
    "No features suggestive of infectious colitis or other acute pathology.",
    "Impression benign, no indication of significant mucosal abnormalities.",
    "Colonoscopy results consistent with expected post-procedure course.",
    "No concerning lesions identified, patient advised to continue regular care.",
    "No need for immediate intervention, plan for routine follow-up.",
    "Impression normal, no evidence of significant colonic disease.",
    "Colonoscopy findings unremarkable, no evidence of disease progression.",
    "No features concerning for malignancy detected.",
    "Polyps removed with clear margins, no residual adenomatous tissue.",
    "No signs of acute complications following the procedure.",
    "Impression consistent with benign colorectal changes.",
    "Colonoscopy results negative for advanced neoplasia.",
    "No evidence of active bleeding or vascular abnormalities seen.",
    "Findings consistent with benign mucosal changes.",
    "No significant deviations from expected findings, no further action needed.",
    "Polyps removed successfully, no complications encountered.",
    "No concerning features noted, continue with regular monitoring.",
    "Tissue samples sent for pathological examination.",
    "Colonoscopy results within normal limits, no worrisome findings detected.",
    "No evidence of malignancy or dysplasia, continue with routine surveillance.",
    "Normal post-procedure impression, patient discharged home.",
    "No significant pathology identified, routine follow-up recommended.",
    "Impression unchanged from previous exams, no new concerns.",
    "Colonoscopy findings stable, no evidence of disease recurrence.",
    "No features suggestive of infectious colitis or other acute pathology.",
    "Impression benign, no indication of significant mucosal abnormalities."
    # Your negative symptoms list here
]

# Function to classify report as normal or abnormal
def classify_report(report_text):
    if any(symptom in report_text for symptom in positive_symptoms):
        return "Positive Symptoms"
    elif any(symptom in report_text for symptom in negative_symptoms):
        return "Negative Symptoms"
    else:
        return "Unknown"

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    except Exception as e:
        st.error(f"Error occurred while processing PDF: {e}")
    return text

def main():
    st.title("Medical Report Classifier")

    # File upload
    uploaded_file = st.file_uploader("Upload PDF medical report", type="pdf")

    if uploaded_file is not None:
        # Display uploaded file
        st.subheader("Uploaded Medical Report:")
        st.write(uploaded_file)

        # Extract text from uploaded PDF
        report_text = extract_text_from_pdf(uploaded_file)

        # Classify report
        classification_result = classify_report(report_text)
        st.subheader("Classification Result:")
        st.write(classification_result)

        # Create JSON response
        json_response = {
            "filename": uploaded_file.name,
            "classification_result": classification_result
        }

        # Convert to JSON format
        st.subheader("JSON Response:")
        st.json(json_response)

if __name__ == "__main__":
    main()
