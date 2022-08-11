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
    def on_get(_req, resp):
        resp.context.result = 'Welcome to ML-service!'
