from flask import jsonify, Blueprint, request
from dao import user_dao

users_bp = Blueprint("users", __name__)


@users_bp.route('/register', methods=['POST'])
def register():
  data = request.json
  first_name = data.get('first_name')
  last_name = data.get('last_name')
  email = data.get('email')
  username = data.get('username')
  password = data.get('password')
  government_id = data.get ('government_id')
  
  if not user_dao.unique_email(email):
    return jsonify({"Error": "Email Already Exists"}), 422
  
  if not user_dao.unique_username(username):
    return jsonify({"Error": "Username Already Exists"}), 422
  
  user_dao.create_user(first_name, last_name, email, username, password, government_id)

  return({"Success":"User Added Succesfully"}), 200


@users_bp.route('/login', methods = ['POST'])
def login():
  data = request.json
  username = data.get('username')
  password = data.get('password')
  
  user = user_dao.login_user(username, password)
      
  if user:
    first_name, last_name, email, username = user
    fullname = f'{first_name} {last_name}'
    return jsonify({"Email": email, "Name": fullname}), 200

  return jsonify({"Failed": "Login Failed"}), 422


@users_bp.route('/<int:id>', methods=['PUT'])
def update_user(id:int):
  data = request.json
  first_name = data.get('first_name')
  last_name = data.get('last_name')
  email = data.get('email')
  username = data.get('username')
  password = data.get('password')
  government_id = data.get('government_id')

  if not user_dao.email_existing(id):
    return jsonify({"Error": "No User Found"}), 422

  if not user_dao.unique_email(email):
    return jsonify({"Error": "Email Already Exists"}), 422

  if not user_dao.unique_username(username):
    return jsonify({"Error": "Username Already Exists"}), 422

  user_dao.update_user(id, first_name, last_name, email, username, password, government_id)
  return jsonify({"Success": "User Updated Successfully"}), 200