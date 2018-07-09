from database import db, Column, Model
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.types import PickleType

class Test(Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Test %r>' % self.name


"""
DB model corresponding to the Person schema.
Used to post/retrieve information from DB

"""


class Person(Model):
    id = Column(db.Integer, primary_key=True)
    job = Column(db.String(50))
    company = Column(db.String(130))
    ssn = Column(db.String(30), unique=True)  # Guess it should be unique
    residence = Column(db.String(250))
    website = Column(PickleType)  # Store list to DB field
    blood_group = Column(db.String(3))  # Can't be more than 3 letters long
    username = Column(db.String(50), unique=True)
    name = Column(db.String(100))
    sex = Column(db.String(1))
    address = Column(db.String(250))
    mail = Column(db.String(120))
    birthdate = Column(db.String())  # Should be date, but fails
    current_location = Column(PickleType)

    def __init__(self, job, company, ssn, residence, current_location, blood_group, website, username, name,
                 sex, address, mail, birthdate):

        self.job = job
        self.company = company
        self.ssn = ssn
        self.residence = residence
        self.current_location = current_location
        self.blood_group = blood_group
        self.website = website
        self.username = username
        self.name = name
        self.sex = sex
        self.address = address
        self.mail = mail
        self.birthdate = birthdate
