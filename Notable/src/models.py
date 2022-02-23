from sqlalchemy import Integer, ForeignKey, String, Column
from . import db


class Doctor(db.Model):
    """Data model for Doctor """

    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=False, unique=True, nullable=False)
    last_name = db.Column(db.String(64), index=False, unique=False, nullable=False)

    def __repr__(self):
        return f"<Doctor {self.first_name} {self.last_name} >"

    def __str__(self):
        return f"Doctor {self.first_name} {self.last_name} "

    # def __dict__(self):
    #     return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, }


class Patient(db.Model):
    """Data model for Doctor """

    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=False, unique=True, nullable=False)
    last_name = db.Column(db.String(64), index=False, unique=False, nullable=False)

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name}>"


class Appointment(db.Model):
    """Data model for Doctor """

    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    follow_up = db.Column(db.Boolean, index=False, unique=False, nullable=False)
    day = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    dr = Column(Integer, ForeignKey("doctors.id"))
    patient = Column(Integer, ForeignKey("patients.id"))

    def __repr__(self):
        return f"<Appointment {self.day} {self.follow_up} {self.dr} {self.patient}>"
