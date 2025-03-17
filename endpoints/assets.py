from flask import Blueprint, request, jsonify, send_from_directory
from dao.asset_dao import save_file, get_file_path, UPLOAD_DIR

assets_bp = Blueprint('assets', __name__)

@assets_bp.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not file.content_type.startswith('image/'):
        return jsonify({'error': 'File must be an image'}), 400

    filename = save_file(file)

    return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200

@assets_bp.route('/<filename>', methods=['GET'])
def download(filename):
    file_path = get_file_path(filename)
    
    if not file_path:
        return jsonify({'error': 'File not found'}), 404
    
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)
