import json
import logging

from pyramid.security import Allow, ALL_PERMISSIONS
from sqlalchemy import (Column, String, Text)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.declarative import declarative_base

from pynder.models.user import User as APIUser, Hopeful

Base = declarative_base()

log = logging.getLogger(__name__)


class User(Base):
    __tablename__ = "hopeful_users"

    id = Column(String(48), index=True, primary_key=True)
    name = Column(String(48), index=True)
    bio = Column(Text())
    # TODO: maybe add photos as an array column
    # TODO: jesus you could do some evil stuff with ping times here

    liked = Column(String(20), default="not yet")  # lazy mans enum here

    # TODO: proper serializing, foreign key shit here
    data = Column(Text())

    def __acl__(self):
        return [(Allow, "admin", ALL_PERMISSIONS)]

    def __init__(self, user_obj):
        self.id = user_obj.id
        self.data = json.dumps(user_obj._data)
        self.name = user_obj.name
        self.bio = user_obj.bio
        self.liked = "not yet"
        # TODO: fancy init shit can come later
        # super(User, self).__init__(data=user_obj._data, session=None)

    def to_hopeful_api_user(self, session):
        return Hopeful(json.loads(self.data), session=session.session)

    def to_api_user(self, session):
        return APIUser(json.loads(self.data), session=session.session)


class LoginUser(Base):
    __tablename__ = "login_users"
    id = Column(UUID(as_uuid=True), index=True, primary_key=True)
    username = Column(String(255), index=True, primary_key=True)
    password = Column(String(255))  # yolo
    profile = Column(String(255))
