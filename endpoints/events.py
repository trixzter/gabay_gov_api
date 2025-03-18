from flask import jsonify, Blueprint, request
from dao.event_dao import create_event, get_events, get_event_dao, update_event, delete_event, check_event_dao
events_bp = Blueprint("events", __name__)


@events_bp.route('', methods=['POST'])
def add_event():
    data = request.json 
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    create_event(title, date, time, location, photo, description)

    return jsonify({"success":"Event Added Succesfully"}), 200


@events_bp.route('', methods=['GET'])
def get_events_info():
    title = request.args.get('title')
    location = request.args.get('location')

    events = get_events(title, location)
    
    if not events:
        return jsonify({"Error": "No events found"}), 404

    for event in events:
        event['time'] = event['time'].strftime('%H:%M:%S')
    
    return jsonify(events)


@events_bp.route('/<int:id>', methods=['GET'])
def get_event_info(id:int):                     
    
    if get_event_dao(id):
        event = get_event_dao(id)
        event['time'] = event['time'].strftime('%H:%M:%S')
        return jsonify(event)
    
    return jsonify({"Error": "Event not found"}), 404
    

@events_bp.route('/<int:id>', methods=['PUT'])
def edit_event(id:int):
    data = request.json
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    if check_event_dao(id):
        update_event(id, title, date, time, location, photo, description)
        return jsonify({"success":"Event Updated Succesfully"}), 200
    
    return jsonify({'Error':'No Event Found'}), 404


@events_bp.route('/<int:id>', methods=['DELETE'])
def remove_event(id:int):

    if check_event_dao(id):
        delete_event(id)
        return jsonify({"success":"Event deleted succesfully"}), 200
    
    return jsonify({"error":"Event not found"}), 404