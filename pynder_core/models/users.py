import json

from sqlalchemy import (Column, String, Text)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

from pynder.models.user import User as APIUser, Hopeful

Base = declarative_base()


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

    def __init__(self, user_obj):
        self.id = user_obj.id
        self.data = json.dumps(user_obj._data)
        self.name = user_obj.name
        self.bio = user_obj.bio
        self.liked = "not yet"
        # TODO: fancy init shit can come later
        # super(User, self).__init__(data=user_obj._data, session=None)

    def to_hopeful_api_user(self, session):
        return Hopeful(json.loads(self.data), session=session)

    def to_api_user(self, session):
        return APIUser(json.loads(self.data), session=session)
