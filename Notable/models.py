from . import db


class Doctor(db.Model):
    """Data model for Doctor """

    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=False, unique=True, nullable=False)
    last_name = db.Column(db.String(64), index=False, unique=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)

    def __repr__(self):
        return f"<Doctor {self.first_name} {self.last_name} {self.email}>"


class Patient(db.Model):
    """Data model for Doctor """

    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=False, unique=True, nullable=False)
    last_name = db.Column(db.String(64), index=False, unique=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name} {self.email}>"


class Appointment(db.Model):
    """Data model for Doctor """

    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    follow_up = db.Column(db.Boolean, index=False, unique=False, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    app_for = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return f"<Appointment {self.created} {self.app_for} {self.follow_up}>"

