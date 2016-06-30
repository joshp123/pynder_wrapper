import logging

from pyramid.view import view_config

from pynder_core.models.users import User
from pynder_web import db_session

log = logging.getLogger(__name__)

@view_config(context="pynder.models.user.User",
             renderer='pynder_web:templates/hopeful.mako', permission="view")
def display_hopeful_like(request):
    return {'user': request.context}


# TODO: fix factories

@view_config(context="pynder.models.user.Hopeful", name="like",
             renderer='json', request_method="POST")
def like(request):
    id = request.context.like()
    log.critical(id)
    _update_user_after_swipe(request, "yes")
    return {'liked': id}


@view_config(context="pynder.models.user.Hopeful", name="superlike",
             renderer='json', request_method="POST")
def superlike(request):
    id = request.context.superlike()
    _update_user_after_swipe(request, "superlike")
    log.critical(id)
    return {'superliked': id}


@view_config(context="pynder.models.user.Hopeful", name="nope",
             renderer='json', request_method="POST")
def nope(request):
    id = request.context.dislike()
    log.critical(id)
    _update_user_after_swipe(request, "nope")
    return {'disliked': id}


def _update_user_after_swipe(request, choice):
    log.critical("correct")
    user = db_session.query(User).get(request.context.id)
    user.liked = choice
    db_session.add(user)
    db_session.commit()
    return {'response': "this is faked"}
    # return {'response': request.context.like()}
