from pyramid.config import Configurator
from pyramid.response import Response

from pynder_core.tinder import Tinder

from pynder_web.routes import setup_routes

session = None


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def main(config, **settings):
    global session
    session = Tinder()

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
