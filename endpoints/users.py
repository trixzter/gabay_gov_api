from flask import jsonify, Blueprint, request
from dao.user_dao import register_user, login_user, update_user, check_user

users_bp = Blueprint("users", __name__)

@users_bp.route('/register', methods = ['POST'])
def register():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    government_id = data.get ('government_id')
    
    register_user (first_name, last_name, email, username, password, government_id)

    return ({"Success":"User Added Succesfully"}), 200


@users_bp.route('/login', methods = ['POST'])
def login():
    data=request.json
    username = data.get('username')
    password = data.get('password')
    
    user = login_user(username, password)
        
    if user:
        first_name, last_name, email, username = user
        fullname = f'{first_name} {last_name}'
        return jsonify({"Email": email, "Name": fullname}), 200
    
    return jsonify({"Failed": "Login Failed"}), 422


@users_bp.route('/<int:id>', methods=['PUT'])
def update_user_info(id):
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    government_id = data.get('government_id')


    user_exist = check_user(id)

    if user_exist:
        update_user(id, first_name, last_name, email, username,password, government_id)
        return jsonify({"Success": "User Updated Successfully"}), 200
 
    return jsonify({"Error": "No user found"}), 422