import os

def validate_file_from_request(request):
    if "file" not in request.files:
        return None
    file = request.files["file"]
    if file.filename == "":
        return None
    return file

def save_file_to_upload(file):
    os.makedirs("uploads", exist_ok=True)
    image_path = os.path.join("uploads", file.filename)
    file.save(image_path)
    return image_path
