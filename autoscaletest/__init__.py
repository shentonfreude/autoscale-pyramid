import platform
import logging

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def _metadata():
    return {'metadata': {'node': platform.node()}}

def metadata(request):
    return _metadata()

def _factorial(number):
    # TODO: sanity check number < 1 and raise Exception
    # Recursive solution exceeded max depth between 500 and 1000, iterate.
    result = number
    for n in range (2, number):
        result *= n
    return result

def factorial(request):
    # TODO: Sanity check number is int
    number = int(request.matchdict['number'])
    md = _metadata()
    md.update({'number': number, 'factorial': _factorial(number)})
    return md

def _squareroot(number):
    # Newton's method
    DELTA = 1e-16
    steps = 0
    prev = 0                    # anything but z
    z = 1.0
    while abs(prev - z) > DELTA:
        prev = z
        steps += 1
        z -= (z * z - number) / (2 * z)
    return z, steps

def squareroot(request):
    number = int(request.matchdict['number'])
    sr, steps = _squareroot(number)
    md = _metadata()
    md.update({'number': number, 'squareroot': sr, 'steps': steps})
    return md

def home(request):
    return {'methods': ['/', '/metadata/{n}', '/squareroot/{n}', '/hello/{name}']}

def hello_world(request):
    md = _metadata()
    md.update({'msg': 'Hello %(name)s!' % request.matchdict})
    return md

def main(global_config, **settings):
    config = Configurator()

    config.add_route('home',       '/')
    config.add_route('metadata',   '/metadata')
    config.add_route('factorial',  '/factorial/{number}')
    config.add_route('squareroot', '/squareroot/{number}')
    config.add_route('hello',      '/hello/{name}')

    config.add_view(home,        route_name='home',       renderer='json')
    config.add_view(metadata,    route_name='metadata',   renderer='json')
    config.add_view(factorial,   route_name='factorial',  renderer='json')
    config.add_view(squareroot,  route_name='squareroot', renderer='json')
    config.add_view(hello_world, route_name='hello')

    app = config.make_wsgi_app()
    return app


# Invoke as $virtualenv/bin/python autoscaletest/__init__.py

if __name__ == '__main__':
    app = main(None)
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

