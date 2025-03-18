from flask import jsonify, Blueprint, request
from dao import event_dao
from utils.gmail import create_event_notification

events_bp = Blueprint("events", __name__)


@events_bp.route('', methods=['POST'])
def create_event():
    data = request.json 
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    event_dao.create_event(title, date, time, location, photo, description)

    create_event_notification(title, description)

    return jsonify({"success":"Event Added Succesfully"}), 200


@events_bp.route('', methods=['GET'])
def get_events():
    title = request.args.get('title')
    location = request.args.get('location')

    events = event_dao.get_events(title, location)
    
    if not events:
        return jsonify({"Error": "No events found"}), 404

    for event in events:
        event['time'] = event['time'].strftime('%H:%M:%S')
    
    return jsonify(events)


@events_bp.route('/<int:id>', methods=['GET'])
def get_event(id:int):                     
    
    if event_dao.get_event(id):
        event = event_dao.get_event(id)
        event['time'] = event['time'].strftime('%H:%M:%S')
        return jsonify(event)
    
    return jsonify({"Error": "Event not found"}), 404
    

@events_bp.route('/<int:id>', methods=['PUT'])
def update_event(id:int):
    data = request.json
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    if event_dao.event_existing(id):
        event_dao.update_event(id, title, date, time, location, photo, description)
        return jsonify({"success":"Event Updated Succesfully"}), 200
    
    return jsonify({'Error':'No Event Found'}), 404


@events_bp.route('/<int:id>', methods=['DELETE'])
def delete_event(id:int):

    if event_dao.event_existing(id):
        event_dao.delete_event(id)
        return jsonify({"success":"Event deleted succesfully"}), 200
    
    return jsonify({"error":"Event not found"}), 404