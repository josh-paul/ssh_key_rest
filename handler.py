import logging

from falcon_lambda import wsgi

from ssh_key.app import Service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Init the Falcon API
api = Service()


def lambda_handler(event, context):
    '''
    Wrap the Falcon API with a WSGI handler built to handle traffic from API-Gateway to Lambda.
    This is the entrypoint to be used in the Lambda conofiguration. handler.lambda_handler
    '''
    logger.debug(event)
    resp = wsgi.adapter(api, event, context)
    logger.debug(resp)
    return resp
