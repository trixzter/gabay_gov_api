from pathlib import Path
import secrets, string

UPLOAD_DIR = Path("storage/images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def generate_random_filename(original_filename):
    ext = Path(original_filename).suffix  
    random_name = ''.join(secrets.choice(string.ascii_letters) for _ in range(10))  
    return f"{random_name}{ext}"

def save_file(file):
    filename = generate_random_filename(file.filename)
    file_path = UPLOAD_DIR / filename
    file.save(file_path)
    return filename

def get_file_path(filename):
    file_path = UPLOAD_DIR / filename
    return file_path if file_path.exists() else None
