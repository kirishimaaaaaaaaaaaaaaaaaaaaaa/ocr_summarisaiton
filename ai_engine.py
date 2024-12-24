import cv2
import pytesseract
from PIL import Image
from transformers import pipeline

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    pil_image = Image.fromarray(thresh)
    extracted_text = pytesseract.image_to_string(pil_image).strip()
    return extracted_text

def summarize_text(text):
    if not text:
        return "No text found in the image."
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
    return summary
