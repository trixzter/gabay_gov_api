from flask import jsonify, Blueprint, request
from dao.event_dao import create_event, view_all_events, view_events, edit_event, remove_event

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
    event = view_events(id)

    if event is None:
        return jsonify({"Error": "Event not found"}), 404
    
    event['time'] = event['time'].strftime('%H:%M:%S')
    return jsonify(event)


@events_bp.route('/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.json
    title=data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    event = edit_event(id, title, date, time, location, photo, description)

    if event:
        return jsonify({"success":"Event Updated Succesfully"}), 200
    
    return jsonify({'Error':'No Event Found'})


@events_bp.route('/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = remove_event(id)

    if event is None:
        return jsonify({"error":"Event not found"}), 404
    
    return jsonify({"success":"Event deleted succesfully"}), 200