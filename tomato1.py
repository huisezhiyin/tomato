import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def initialize(self, *args, **kwargs):
        self.a = kwargs.get("a")
        self.b = kwargs.get("b")

    def get(self):
        self.write("hello world! {0} {1}".format(self.a, self.b))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler, {"a": 1, "b": 2}),
    ])
