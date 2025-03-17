from flask import Blueprint, jsonify, request
from dao.email_dao import create_email

emails_bp = Blueprint ('emails', __name__)

@emails_bp.route('/', methods=['POST'])
def add_email ():
    data=request.json
    subscriber_email = data.get('subscriber_email')
    
    user = create_email(subscriber_email)

    if user:
        return jsonify ({"Success":"Email Added Successfully"}), 200

    return jsonify ({"Error":"Email Already Exist"}), 422