import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:

    def __init__(self):
        api_key=os.getenv("GEMINI_API_KEY")
        model_name=os.getenv("GEMINI_MODEL","gemini-1.5-pro")

        if not api_key or api_key=="YOUR_GEMINI_API_KEY":
            raise ValueError("GEMINI_API_KEY is not configured.")

        genai.configure(api_key=api_key)

        self.model=genai.GenerativeModel(model_name)

    def generate_document(self,document_type,parties,terms,dates):

        prompt=f"""
You are a legal document drafting assistant.

Create a professional draft for the following document.

Document Type:
{document_type}

Parties Involved:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{dates}

Requirements:
- Use clear professional legal language.
- Include a suitable document title.
- Include the parties involved.
- Include the effective date.
- Organize the terms and conditions clearly.
- Add suitable general clauses where appropriate.
- Do not invent specific personal information.
- Do not claim that the document provides legal advice.
- Return only the document content.
"""

        response=self.model.generate_content(prompt)

        if not response or not response.text:
            raise ValueError("Gemini returned an empty response.")

        return response.text.strip()