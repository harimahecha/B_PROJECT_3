import os
from flask import Blueprint, request, render_template, jsonify
from werkzeug.utils import secure_filename
from .utils import extract_text_from_file, generate_summary, process_file

main = Blueprint("main", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Process file
    summary_length = request.form.get("summary_length", "medium")
    result = process_file(filepath, summary_length)

    if "error" in result:
        return jsonify({"error": result["error"]}), 500

    return jsonify({
        "extracted_text": result["extracted_text"],
        "summary": result["summary"]
    })

