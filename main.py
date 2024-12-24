from ai_engine import extract_text_from_image, summarize_text
from file_utils import save_file_to_upload, validate_file_from_request
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    file = validate_file_from_request(request)
    if file is None:
        return redirect("/")
    image_path = save_file_to_upload(file)
    extracted_text = extract_text_from_image(image_path)
    summary = summarize_text(extracted_text)
    return render_template("result.html", text_in_image=extracted_text, text_summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
