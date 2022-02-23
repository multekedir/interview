from flask import current_app as app
from flask import jsonify, json
from datetime import datetime
from src.models import Doctor, Appointment, Patient, db

from flask import request, make_response


@app.route("/add_doctors", methods=["POST"])
def add_doctors():
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")

    if first_name and last_name:
        existing_user = Doctor.query.filter(
            Doctor.first_name == first_name or Doctor.last_name == last_name
        ).first()
        if existing_user:
            return make_response(f"{first_name} ({last_name}) already created!")

        new_doctor = Doctor(
            first_name=request.args.get("first_name"),
            last_name=request.args.get("last_name"),
        )
        db.session.add(new_doctor)  # Adds new doctor record to database
        db.session.commit()  # Commits all changes
        return make_response(f"{new_doctor} created!")


@app.route("/add_patient", methods=["POST"])
def add_patient():
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")

    if first_name and last_name:
        existing_user = Patient.query.filter(
            Patient.first_name == first_name or Patient.last_name == last_name
        ).first()
        if existing_user:
            return make_response(f"{existing_user} already created!")

        new_patient = Patient(
            first_name=request.args.get("first_name"),
            last_name=request.args.get("last_name"),
        )
        db.session.add(new_patient)  # Adds new doctor record to database
        db.session.commit()  # Commits all changes
        return make_response(f"{new_patient} created!")


@app.route("/add_appointment/", methods=["POST"])
def add_appointment():
    dr_id = request.args.get("dr_id")
    patient_id = request.args.get("patient_id")

    existing_doc = Doctor.query.filter(Doctor.id == dr_id).first()
    if not existing_doc:
        return make_response("Doctor not found")

    existing_patient = Patient.query.filter(Patient.id == patient_id).first()
    if not existing_patient:
        return make_response("Doctor not found")

    kind = request.args.get("kind")

    new_appointment = Appointment(
        follow_up=bool(kind == "follow_up"),
        day=datetime.strptime(request.args.get("day"), '%m-%d-%Y-%I-%M-%p'),
        dr=existing_doc.id,
        patient=existing_patient.id,
    )

    db.session.add(new_appointment)  # Adds new doctor record to database
    db.session.commit()  # Commits all changes
    return make_response(f"{new_appointment} created!")


@app.route("/doctors", methods=["GET"])
def doctors():
    data = Doctor.query.all()

    return make_response(f"{data}")


@app.route("/patients", methods=["GET"])
def patients():
    data = Patient.query.all()

    return make_response(f"{data}")


@app.route("/appointments/<dr_id>/<day>", methods=["GET"])
def appointments(dr_id, day):
    d = datetime.strptime(day, '%m-%d-%Y'),
    return make_response(
        f"{Appointment.query.filter(Appointment.dr == dr_id).filter(Appointment.day.strftime('%m/%d/%y') == d).all()}")


@app.route("/del_appointment/<app_id>", methods=["DELETE"])
def del_appointment(app_id):
    appointment = Appointment.query.get(int(app_id))
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return f"{appointment} Removed"
    return "Appointment Not Found"
