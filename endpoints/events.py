from flask import jsonify, Blueprint, request
from dao.event_dao import create_event, view_all_events, view_event, edit_event, remove_event, check_event

events_bp = Blueprint ("events", __name__)


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
def all_events():
    title = request.args.get('title')
    location = request.args.get('location')

    events = view_all_events(title, location)
    
    if not events:
        return jsonify({"Error": "No events found"}), 404

    for event in events:
        event['time'] = event['time'].strftime('%H:%M:%S')
    
    return jsonify(events)


@events_bp.route('/<int:id>', methods=['GET'])
def get_event(id):
    event = view_event(id)

    if event is None:
        return jsonify({"Error": "Event not found"}), 404
    
    event['time'] = event['time'].strftime('%H:%M:%S')
    return jsonify(event)


@events_bp.route('/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.json
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    event = check_event(id)

    if event:
        edit_event(id, title, date, time, location, photo, description)
        return jsonify({"success":"Event Updated Succesfully"}), 200
    
    return jsonify({'Error':'No Event Found'}), 404


@events_bp.route('/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = check_event(id)

    if event:
        remove_event(id)
        return jsonify({"success":"Event deleted succesfully"}), 200
    
    return jsonify({"error":"Event not found"}), 404