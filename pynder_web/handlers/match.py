from functools import partial

from pyramid.view import view_config
from pynder_web import session

match_view = partial(view_config, context="pybynder.user.models.Match")


@view_config(route_name='matches', renderer='json')
def matches(request):
    print("adsfads")
    return {'matches': [m.user.name for m in session.matches]}


@view_config(route_name='matches2',
             renderer='pynder_web:templates/matches.mako')
def matches_template(request):
    return {'matches': session.matches}


@view_config(context="pynder.models.user.Match", name='messages',
             renderer="pynder_web:templates/message.mako")
def messages_for_match(request):
    messages = request.context.messages
    return {'match': request.context,
            'messages': messages}
