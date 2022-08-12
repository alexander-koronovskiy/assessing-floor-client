import abc


class Resource(abc.ABC):
    """
    Base resource class that requires a ConfigProvider
    instance to be passed into constructor
    """

    def __init__(self, config):
        """
        :param server.ConfigProvider config: Service configuration
        """
        self._config = config


class HomeResource(Resource):
    @staticmethod
    async def on_get(_req, resp):
        resp.context.result = 'Welcome to ML-service!'


class SendImageResource(Resource):
    @staticmethod
    async def on_get(_req, resp):
        resp.content_type = 'text/html'
        with open('templates/index.html', 'r') as f:
            resp.body = f.read()
