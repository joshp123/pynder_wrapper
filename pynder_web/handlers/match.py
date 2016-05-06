from pyramid.view import view_config
from pynder_web import session


@view_config(route_name='matches', renderer='json')
def matches(request):
    print("adsfads")
    return {'matches': [m.user.name for m in session.matches]}


@view_config(route_name='matches2',
             renderer='pynder_web:templates/matches.mako')
def matches_template(request):
    return {'matches': session.matches}
