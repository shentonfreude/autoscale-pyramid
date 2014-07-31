from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def _factorial(number):
    # TODO: Should sanity check number < 1 and raise Exception
    # Recursive solution exceeded max depth between 500 and 1000, iterate.
    result = number
    for n in range (2, number):
        result *= n
    return result

    # TODO return JSON view

def factorial(request):
    # TODO: Sanity check number is int
    number = int(request.matchdict['number'])
    return Response('Factorial of %d is %d' % (number, _factorial(number)))

def _squareroot(number):
    # Newton's method
    DELTA = 1e-16
    prev = 1.0
    z = 1.0
    steps = 0
    while True:
        z -= (z * z - number) / (2 * z)
        if abs(prev - z) < DELTA:
            break
        prev = z
        steps += 1
    return z, steps

def squareroot(request):
    number = int(request.matchdict['number'])
    sr, steps = _squareroot(number)
    return Response('Squareroot of %d is %f in %d steps' %
                    (number, sr, steps))

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('factorial', '/factorial/{number}')
    config.add_view(factorial, route_name='factorial')
    config.add_route('squareroot', '/squareroot/{number}')
    config.add_view(squareroot, route_name='squareroot')
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

# invoke as .../bin/python app.py



