from botocore.errorfactory import ClientError
from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, String, Date, ForeignKey, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import json

Base = declarative_base()


class CasesGlobal(Base):
    __tablename__ = 'CasesGlobal'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    confirmed = Column(Integer)
    deaths = Column(Integer)
    recovered = Column(Integer)

    country_id = Column(Integer, ForeignKey('Country.id'))


class Country(Base):
    __tablename__ = 'Country'

    id = Column(Integer, primary_key=True)
    country = Column(String)


class Location(Base):
    __tablename__ = 'Location'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('Country.id'))
    location = Column(String)
    location_level = Column(String)


class CasesLocal(Base):
    __tablename__ = 'CasesLocal'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    confirmed = Column(Integer)
    location_id = Column(Integer, ForeignKey('Location.id'))


class Tests(Base):
    __tablename__ = 'Tests'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    cumulative_tests = Column(Integer)
    country_id = Column(Integer, ForeignKey('Country.id'))





if __name__ == "__main__":
    secret = {
        "username": "admin",
        "password": "",
        "host": "database-1.ccwgqdqrrmvt.eu-west-1.rds.amazonaws.com",
        "port": "1433"
    }

    #     engine = create_engine(
    #         'mssql+pymssql://' +
    #         secret['username'] + ':' + secret['password'] + '@' + secret['host'] + ':' +
    #         str(secret['port']),
    #         connect_args={'autocommit': True}
    #     )

    engine = create_engine(
        'mssql+pymssql://' +
        secret['username'] + ':' + secret['password'] + '@' + secret['host'] + ':' +
        str(secret['port']) + '/Corona'

    )

    Base.metadata.create_all(engine)

    # class ConfirmedPatients(Base):
    #     __tablename__ = 'ConfirmedPatients'
    #
    #     id = Column(Integer, primary_key=True)
    #     date = Column(Date)
    #     age = Column(Integer)
    #     gender = Column(Integer)
    #     travel_status = Column(String)
    #     location_id = Column(Integer, ForeignKey('Location.id'))
