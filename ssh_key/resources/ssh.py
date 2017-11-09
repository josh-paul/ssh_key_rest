import base64
import binascii
import hashlib
import logging

import falcon

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from falcon.media.validators import jsonschema

logging = logging.getLogger(__name__)


post_schema = {
    'type': 'object',
    'properties': {
        'publicKey': {
            'description': 'the public key in OpenSSH format',
            'type': 'string'
        }
    },
    'required': ['publicKey']
}


class KeyResource(object):
    def fingerprint(self, key):
        '''
        Returns the md5 fingerprint of the passed in key.
        '''
        digest = hashlib.md5(key).hexdigest()
        return ':'.join(a + b for a, b in zip(digest[::2], digest[1::2]))

    def on_get(self, request, response):
        '''
        Generate and return a private and public key for use with OpenSSH. Uses a key size of 2048.
        '''
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        response.media = {
            'privateKey': key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ).decode('utf-8'),
            'publicKey': key.public_key().public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            ).decode('utf-8')
        }
        response.status = falcon.HTTP_200

    @jsonschema.validate(post_schema)
    def on_post(self, request, response):
        '''
        Read in json body. For publicKey, validate, then return OpenSSH fingerprint and the EC2
        MD5 fingerprint.

        Fingerprint differences discussed in:

        EC2:
        http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

        OpenSSH
        https://tools.ietf.org/html/rfc4716#section-4
        '''
        try:
            key = serialization.load_ssh_public_key(
                request.media.get('publicKey').encode('utf-8'),
                backend=default_backend()
            )
            valid = key.public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            )
            response.media = {
                'ec2': self.fingerprint(
                    key.public_bytes(
                        encoding=serialization.Encoding.DER,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo
                    )
                ),
                'openSSH': self.fingerprint(
                    base64.b64decode(valid.decode('utf-8').split()[1].encode('ascii'))
                )
            }
            response.status = falcon.HTTP_200
        except (binascii.Error, ValueError):
            response.media = {'error': 'Key is not in the proper format or contains extra data.'}
            response.status = falcon.HTTP_422
