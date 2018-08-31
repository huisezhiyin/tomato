from tornado import ioloop
from tomato1 import make_app


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()
