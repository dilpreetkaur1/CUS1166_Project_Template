from app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AppointmentEntry(db.Model):
    __tablename__ = "AffirmationEntry"
    AppoitnmentEntryID = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    AppointmentEntryTitle = db.Column(db.String)
    AppointmentEntryDate=db.Column(db.DateTime)
    AppointmentEntryAddress = db.Column(db.String)
    AppointmentEntryName=db.Column(db.String)
    AppointmentEntryNotes=db.Column(db.String)

    def add_AEntry(self, aTitle, aDate, aAddress, aName,aNotes):
        new_AppointmentEntry = AppointmentEntry(AppointmentEntryTitle=aTitle, AffirmationEntryDate=aDate, AffirmationEntryAddress=aAddress, AppointmentEntryName=aName,AppointmentEntryNotese=aNotes )
        db.session.add(new_AppointmentEntry)
        db.session.commit()