
# **Document Summary Assistant**

Document Summary Assistant is a Flask-based web application that allows users to upload PDF and image files to extract text and generate smart summaries. The app uses Optical Character Recognition (OCR) and OpenAI's API to deliver concise and insightful summaries.

## **Features**

1. **Document Upload**
   - Drag-and-drop or file picker interface for uploading documents.
   - Supports PDF files and image files (e.g., scanned documents).

2. **Text Extraction**
   - PDF Parsing: Extracts text while maintaining formatting.
   - OCR: Extracts text from images using Tesseract.

3. **Summary Generation**
   - Generates summaries of various lengths: short, medium, or long.
   - Highlights key points and main ideas.

4. **User-Friendly Interface**
   - Simple and intuitive UI.
   - Mobile-responsive design for seamless use on different devices.

## **Project Structure**
```
app/
├── static/
│   └── style.css          
├── templates/
│   └── index.html         
├── __init__.py            
├── routes.py              
├── utils.py                                  
.env                      
render.yaml                
requirements.txt           
run.py                     
```

## **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/document-summary-assistant.git
cd document-summary-assistant
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory with the following content:
```
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the Application
```bash
python run.py
```
Access the app at `http://127.0.0.1:5000`.

## **Deployment on Render**

1. Push the code to GitHub.
2. Create a new **Web Service** on Render and connect your GitHub repository.
3. Use the following configurations in `render.yaml`:
   ```yaml
    services:
    - type: web
        name: document-summary-assistant
        env: python
        region: oregon
        buildCommand: |
            apt-get update && apt-get install -y tesseract-ocr libtesseract-dev
            export PATH=$PATH:/usr/bin
            pip install -r requirements.txt
        startCommand: "gunicorn run:app --bind 0.0.0.0:8000"
        envVars:
        - key: OPENAI_API_KEY
            sync: false

   ```
4. Add the necessary environment variables (`OPENAI_API_KEY`) in Render.

## **Troubleshooting**

- **Tesseract Not Found**: Ensure that `pytesseract.pytesseract.tesseract_cmd` points to the correct Tesseract binary path.
- **API Errors**: Verify your OpenAI API key is valid and active.

## **Technologies Used**

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS
- **OCR**: Tesseract
- **Text Summarization**: OpenAI GPT API

