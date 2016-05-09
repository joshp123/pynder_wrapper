import logging
import json

from pynder.models.user import User as APIUser

from pynder_web import session
from pynder_core.models.users import User

# TODO: this is a recipe for circular imports, should fix
from pynder_web import db_session

log = logging.getLogger(__name__)


class BaseFactory(dict):
    def __init__(self, parent, name):
        self.__parent__ = parent
        self.__name__ = name


class RootFactory(dict):
    def __init__(self, request):
        self['match'] = MatchFactory(self, 'match')
        self['likes'] = UserFactory(self, 'user')


class MatchFactory(BaseFactory):
    def __getitem__(self, key):
        if not key:
            pass
            # TODO: display match view
        matches = {match.id: match for match in session.matches}
        return matches.get(key)


class UserFactory(BaseFactory):
    def __getitem__(self, key):
        user = db_session.query(User).get(key)
        if user:
            log.critical("user retrieved!")
            return user.to_hopeful_api_user(session)
        available_to_like = db_session.query(User).filter(User.liked == "not yet").all()
        log.critical(len(available_to_like))
        if len(available_to_like) == 0:
            nearby = session.session.nearby_users()
            for user in nearby:
                db_user = User(user)
                db_session.add(db_user)

            db_session.commit()
            log.critical("we should update likes and persist here")
            return nearby[0]

        else:
            return available_to_like[0].to_hopeful_api_user(session)
