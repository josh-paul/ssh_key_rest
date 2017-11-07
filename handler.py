import logging

from falcon_lambda import wsgi

from ssh_key.app import Service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api = Service()


def lambda_handler(event, context):
    logger.debug(event)
    resp = wsgi.adapter(api, event, context)
    logger.debug(resp)
    return resp