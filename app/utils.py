import pytesseract
from PyPDF2 import PdfReader
from PIL import Image
import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_text_from_file(filepath):
    """
    Extract text from a PDF or image file.
    Args:
        filepath (str): Path to the file.
    Returns:
        str: Extracted text or None if extraction fails.
    """
    try:
        if filepath.endswith(".pdf"):
            reader = PdfReader(filepath)
            text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
        elif filepath.lower().endswith((".png", ".jpg", ".jpeg")):
            image = Image.open(filepath)
            text = pytesseract.image_to_string(image)
        else:
            text = None
        return text.strip() if text else None
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def generate_summary(text, length="medium"):
    """
    Generate a summary for the given text using OpenAI's API.
    Args:
        text (str): The text to summarize.
        length (str): The desired summary length ('short', 'medium', 'long').
    Returns:
        str: Generated summary or an error message if summarization fails.
    """
    try:
        messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
        {"role": "user", "content": f"Summarize the following text into a {length} summary:\n{text}"}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=200 if length == "long" else 100 if length == "medium" else 50,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Failed to generate summary."

def process_file(filepath, summary_length="medium"):
    """
    Process a file to extract text and generate a summary.
    Args:
        filepath (str): Path to the file.
        summary_length (str): The desired summary length ('short', 'medium', 'long').
    Returns:
        dict: A dictionary with extracted text and the generated summary.
    """
    extracted_text = extract_text_from_file(filepath)
    if not extracted_text:
        return {"error": "Failed to extract text from the document."}

    summary = generate_summary(extracted_text, summary_length)
    return {
        "extracted_text": extracted_text,
        "summary": summary
    }
