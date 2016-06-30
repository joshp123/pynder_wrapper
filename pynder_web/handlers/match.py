import logging
from functools import partial
from time import sleep

from pyramid.view import view_config
from pynder_web import session, private_mode

log = logging.getLogger(__name__)

match_view = partial(view_config, context="pybynder.user.models.Match")


@view_config(context="pynder_web.lib.factories.MatchFactory",
             renderer='pynder_web:templates/matches.mako', permission="view")
@view_config(route_name='matches',
             renderer='pynder_web:templates/matches.mako', permission="view")
def matches_template(request):
    return {'matches': session.matches[::-1]}


@view_config(context="pynder.models.user.Match", name='messages',
             renderer="pynder_web:templates/message.mako", permission="admin")
def messages_for_match(request):
    session.refresh()
    messages = request.context.messages
    return {'match': request.context,
            'messages': messages}


@view_config(context="pynder.models.user.Match", name='full',
             renderer="pynder_web:templates/expanded_user.mako",
             permission="admin")
def user(request):
    return {'user': request.context.user}


@view_config(context="pynder.models.user.Match", name='message',
             renderer='json', permission="admin")
def message_match(request):
    if private_mode:
        pass
        # log.critical("private mode on, not sending message")
        # return {"disabled": "temporary"}

    message = request.json_body.get('message')
    log.critical("Sending message {} to {}".format(message,
                                                   request.context.user.name))
    sleep(5)
    response = request.context.message(message)
    log.critical(type(response))
    log.critical(response)
    session.refresh()
    return {'id': 'this is faked',
            'message': message}
