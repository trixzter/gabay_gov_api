from flask import Blueprint, jsonify, request
from dao.email_dao import create_email, email_existing

emails_bp = Blueprint('emails', __name__)


@emails_bp.route('', methods=['POST'])
def add_email():
    data = request.json
    subscriber_email = data.get('subscriber_email')

    if email_existing(subscriber_email):
        return jsonify({"Error":"Email Already Exist"}), 422

    create_email(subscriber_email)
    return jsonify({"Success":"Email Added Successfully"}), 200