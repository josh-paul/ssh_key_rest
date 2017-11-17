import json

import cryptography
import pytest

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from falcon import testing
from ssh_key.app import Service


@pytest.fixture()
def client():
    return testing.TestClient(Service())


def test_fingerprinting(client):
    '''
    Verify that with a given public key, the specified fingerprints are returned.
    '''
    body = json.dumps(
        {
            'publicKey':
                'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHJjgmgwcn4BPlteCkt8UPGdzjTS8SA2RAGQqCDiBIh'
                'ZKJvea3J3feXF/98bvWJkMJuXYtmUNSY+fUCBIYXnuSWvSmDjrR+G9GsMUMgvIXlfNp+8177J1XayVa1z'
                'K8CWZLt5N0zQNcmCS6iOBDhueu1oC9PI3hWQhYxUSosOBSMLWRJW/qnhGVCKG3vVQOAXyYYuLyvF1Rt1c'
                'x+uOJnb7604uL8dclGF5tNs6oRwk+HxBPx9E4qx620zMuzQtLtmoEbNLup81fp1rFG05ECRlbJHrkDshb'
                '4f0ykw6LKjzn394AHssFJrVZPl2PLNjt51qcR07rOhjo6pzcDVQ96oRj'
        }
    )

    response = client.simulate_post('/ssh/key/fingerprint', body=body)

    fingerprints = {
        'ec2': '0c:9e:f7:f3:48:f5:5f:69:13:7e:7d:a9:e2:46:c2:12',
        'openSSH': '71:0e:7a:6d:fd:5d:82:a7:74:ed:6b:e6:f6:19:ae:0f'
    }
    assert response.json == fingerprints


def test_invalid_fingerprint_payload(client):
    '''
    Test for invalid keys passed in.
    '''
    body1 = json.dumps(
        {'publicKey': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBiujz7D4ecEOM9V7objCVDQErZucSKWK'}
    )

    body2 = json.dumps({'publicKey': ''})

    response1 = client.simulate_post('/ssh/key/fingerprint', body=body1)
    response2 = client.simulate_post('/ssh/key/fingerprint', body=body2)

    invalid_key = {'error': 'Key is not in the proper format or contains extra data.'}
    assert response1.json == invalid_key
    assert response2.json == invalid_key


def test_invalid_payload_validation(client):
    '''
    Test for schema validation behavior.
    '''
    body = json.dumps(
        {
            'twiddle-me-this': 'twiddle-me-that'
        }
    )

    response = client.simulate_post('/ssh/key/fingerprint', body=body)

    validation_response = {
        'title': 'Failed data validation',
        'description': '\'publicKey\' is a required property'
    }
    assert response.json == validation_response


def test_key_creation(client):
    '''
    Verify that the returned keys can be loaded as valid keys by cryptography.
    '''
    response1 = client.simulate_post('/ssh/key')

    private_key1 = serialization.load_pem_private_key(
        response1.json['privateKey'].encode('utf-8'),
        password=None,
        backend=default_backend()
    )
    public_key1 = serialization.load_ssh_public_key(
        response1.json['publicKey'].encode('utf-8'),
        backend=default_backend()
    )

    response2 = client.simulate_post('/ssh/key', query_string='keySize=4096')

    private_key2 = serialization.load_pem_private_key(
        response2.json['privateKey'].encode('utf-8'),
        password=None,
        backend=default_backend()
    )
    public_key2 = serialization.load_ssh_public_key(
        response2.json['publicKey'].encode('utf-8'),
        backend=default_backend()
    )

    assert isinstance(private_key1, cryptography.hazmat.backends.openssl.rsa._RSAPrivateKey)
    assert isinstance(public_key1, cryptography.hazmat.backends.openssl.rsa._RSAPublicKey)
    assert isinstance(private_key2, cryptography.hazmat.backends.openssl.rsa._RSAPrivateKey)
    assert isinstance(public_key2, cryptography.hazmat.backends.openssl.rsa._RSAPublicKey)


def test_too_small_key_size(client):
    '''
    Test for too small key size passed in. RSA keys have minimum 768 size.
    '''
    response = client.simulate_post('/ssh/key', query_string='keySize=512')

    too_small = {
        'title': 'Invalid parameter',
        'description': 'The "keySize" parameter is invalid. The value must be at least 768'
    }
    assert response.json == too_small
