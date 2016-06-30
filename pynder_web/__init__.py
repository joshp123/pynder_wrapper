import logging

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.response import Response

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from pynder_core.tinder import Tinder
from pynder_web.routes import setup_routes

session = None
db_session = None

private_mode = False

log = logging.getLogger(__name__)


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def user_profilefinder(login_username, request):
    from pynder_core.models.users import LoginUser
    login_user = db_session.query(LoginUser)\
        .filter(LoginUser.username == login_username).one()
    if login_user and login_user.profile:
        log.critical(login_user.profile)
        return [login_user.profile]


def main(config, **settings):
    global session
    session = Tinder()

    # Late imports requiring the session singleton
    # from pynder_web.lib.factories import RootFactory

    engine = engine_from_config(settings, 'sqlalchemy.')
    from pynder_core.models.users import Base
    Base.metadata.create_all(engine)

    PSQL_Session = sessionmaker(bind=engine)

    global private_mode
    private_mode = settings.get("private_mode", True)
    log.critical("Private mode on? {}".format(private_mode))

    global db_session  # yolo
    db_session = PSQL_Session()

    from pynder_web.lib.factories import RootFactory

    config = Configurator(root_factory=RootFactory,
                          settings=settings)
    setup_routes(config)
    config.set_authentication_policy(
        AuthTktAuthenticationPolicy(secret="fuckthepolice",
                                    callback=user_profilefinder))
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.include('pyramid_mako')
    config.add_route('hello', '/hello/{name}')
    config.add_route('login', '/login/')
    config.add_view(hello_world, route_name='hello')
    config.scan("pynder_web.handlers")
    app = config.make_wsgi_app()

    return app
