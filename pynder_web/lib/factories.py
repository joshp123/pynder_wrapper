from pynder_web import session


class BaseFactory(dict):
    def __init__(self, parent, name):
        self.__parent__ = parent
        self.__name__ = name


class RootFactory(dict):
    def __init__(self, request):
        self['match'] = MatchFactory(self, 'match')


class MatchFactory(BaseFactory):
    def __getitem__(self, key):
        if not key:
            pass
            # TODO: display match view
        print(key)
        print([match.id for match in session.matches])
        if key in [match.id for match in session.matches]:
            return match
