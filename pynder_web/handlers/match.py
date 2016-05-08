import logging
from functools import partial

from pyramid.view import view_config
from pynder_web import session

log = logging.getLogger(__name__)

match_view = partial(view_config, context="pybynder.user.models.Match")


@view_config(context="pynder_web.lib.factories.MatchFactory",
             renderer='pynder_web:templates/matches.mako')
@view_config(route_name='matches',
             renderer='pynder_web:templates/matches.mako')
def matches_template(request):
    return {'matches': session.matches}


@view_config(context="pynder.models.user.Match", name='messages',
             renderer="pynder_web:templates/message.mako")
def messages_for_match(request):
    messages = request.context.messages
    return {'match': request.context,
            'messages': messages}


@view_config(context="pynder.models.user.Match", name='full',
             renderer="pynder_web:templates/hopeful.mako")
def user(request):
    messages = request.context.messages
    return {'user': request.context.user,
            'messages': messages}


@view_config(context="pynder.models.user.Match", name='message',
             renderer='json')
def message_match(request):
    message = request.json_body.get('message')
    log.critical("Sending message {} to {}".format(message,
                                                   request.context.user.name))
    return {'id': 'sadf',
            'message': message}
