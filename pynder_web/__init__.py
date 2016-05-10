import logging

from pyramid.config import Configurator
from pyramid.response import Response
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from pynder_core.tinder import Tinder
from pynder_web.routes import setup_routes

session = None
db_session = None

private_mode = True

log = logging.getLogger(__name__)


def hello_world(request):
    from pynder_core.models.users import User
    for m in session.matches:
        u = User(user_obj=m.user)
        db_session.add(u)
    db_session.commit()
    return Response('Hello %(name)s!' % request.matchdict)


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
    config.include('pyramid_mako')
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    config.scan("pynder_web.handlers")
    app = config.make_wsgi_app()

    return app
