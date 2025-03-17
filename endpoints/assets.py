from flask import Blueprint, request, jsonify, send_from_directory
from pathlib import Path
import secrets, string

assets_bp = Blueprint('assets', __name__)

UPLOAD_DIR = Path("storage/images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def generate_random_filename(original_filename):
    ext = Path(original_filename).suffix 
    random_name = ''.join(secrets.choice(string.ascii_letters) for i in range(10))  
    return f"{random_name}{ext}"


@assets_bp.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not file.content_type.startswith('image/'):
        return jsonify({'error': 'File must be an image'}), 400

    filename = generate_random_filename(file.filename)
    file_path = UPLOAD_DIR / filename
    file.save(file_path)

    return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200


@assets_bp.route('/<filename>', methods=['GET'])
def download(filename):
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        return jsonify({'error': 'File not found'}), 404
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)