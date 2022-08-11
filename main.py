import os

import falcon
import uvloop
import uvicorn

from client import resource, middleware, exceptions, ConfigProvider


_DEFAULT_CONFIG_PATH = 'config.gpu.yml'


def get_config():
    """
    Config reader
    """
    config_path = os.environ.get('ASGI_CONFIG_PATH') or _DEFAULT_CONFIG_PATH
    return ConfigProvider.from_yaml(config_path)


def create_app():
    """
    Application factory
    """
    # Initialize services and providers here
    config = get_config()
     # The app instance is a callable
    app = falcon.App(
        cors_enable=True,
        middleware=[
            middleware.RequireContentTypeMiddleware(),
            middleware.ResponseMarshalMiddleware(),
            middleware.NetVersionMiddleware(),
        ]
    )
    # Initialize resources here
    home_resource = resource.HomeResource(config)

    # Initialize routes here
    app.add_route('/', home_resource)

    # Initialize handlers here
    app.set_error_serializer(exceptions.serializer)
    app.add_error_handler(Exception, exceptions.BaseServerError.handle)
    app.add_error_handler(exceptions.ServerError, exceptions.ServerError.handle)
    app.add_error_handler(exceptions.ReadContentError, exceptions.ReadContentError.handle)
    app.add_error_handler(exceptions.ContentHandlerError, exceptions.ContentHandlerError.handle)

    return app


def _main():
    """
    Dev-only entry point
    """

    uvloop.install()
    config = get_config()
    uvicorn.run(
        'main:create_app',
        host=config.ASGI_HOST,
        port=config.ASGI_PORT,
        reload=True,
        factory=True,
        loop='uvloop',
        log_level='info')


if __name__ == '__main__':
    _main()
