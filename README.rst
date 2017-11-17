SSH Key Rest API
================
.. image:: https://travis-ci.org/josh-paul/ssh_key_rest.svg?branch=master
    :target: https://travis-ci.org/josh-paul/ssh_key_rest

.. image:: https://api.codeclimate.com/v1/badges/85faf1df776c781f83f6/maintainability
   :target: https://codeclimate.com/github/josh-paul/ssh_key_rest/maintainability
   :alt: Maintainability

.. image:: https://codecov.io/gh/josh-paul/ssh_key_rest/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/josh-paul/ssh_key_rest

A simple RESTful API for obtaining a new SSH keypair and fingerprinting an existing SSH public key.

This repository is a sample of using the yolo utility (http://yolocli.readthedocs.io/en/latest/) to 
deploy a stateless REST service running on AWS via API-Gateway and Lambda. Everything needed to 
work with service is contained in the repository.

It uses CloudFormation to define the resources required outside of API-Gateway and Lambda. Then 
the yolo utility builds the Lambda source files and can deploy them.

The choice of Falcon for the HTTP framework is done to make the application very portable. Due to
the routing being handled in the application layer and API-Gateway serving as a proxy, this
application can be ported very easily to be run in Docker or on dedicated systems. This also comes
in handy for testing things locally. You can simply start the web server via any WSGI application.
The sample here uses gunicorn.
::

    $ gunicorn --reload handler:api
    [2017-11-07 21:31:19 -0800] [55964] [INFO] Starting gunicorn 19.7.1
    [2017-11-07 21:31:19 -0800] [55964] [INFO] Listening at: http://127.0.0.1:8000 (55964)
    [2017-11-07 21:31:19 -0800] [55964] [INFO] Using worker: sync
    [2017-11-07 21:31:19 -0800] [55967] [INFO] Booting worker with pid: 55967

Running the above command starts the server on localhost:8000. Since the routing is in the
application, this will work the same way as when it is running in AWS via API-Gateway and Lambda.

Sample usage of the API.
::

    In [1]: import requests

    In [2]: base_url = 'https://16jtpla2ek.execute-api.us-east-1.amazonaws.com/josh'

    In [3]: key = requests.post(f'{base_url}/ssh/key?keySize=4096')

    In [4]: key.json()
    Out[4]:
    {'privateKey': 
        '-----BEGIN RSA PRIVATE KEY-----\n
        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\n
        -----END RSA PRIVATE KEY-----\n',
     'publicKey': 
        'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDxk5cWC4Je4In9to9ysbG5nta/VO
        ryGSWDhKvjyShNBwL/c/rfwV23grJQJsktRGM6yst9SqOtHj6dssKXn+w6Bo+mzSUGZ
        M4WkgUsq7xQPCEFhT8OAv4eraXOsGkH4ZeSWIWBnqpCcuxfyhyR6xtzyWki48V1ZFwJ
        sznooy69CXxUHd4Rq7eWpIaWgtOhUQZHJBrVuCLnXRepZqfRSzawbiQ/QDZTsmMALyA
        IwKM6xLwvczDHZPPg7SBNAaxUaRa/UfbfjmiOFX2nBT3a1VymVDwV+kCYywBLYo4t6/
        /B5RXz5/ZKQNZODGpc8Zv+//kq3iIOFdBoupP8tLPEbU0wGRgvseJEXzOQ9w57jjFIz
        MNz2UgXqTz9V9ve3C7WdeWcju38ri/u3HjZ5HC8p+fRZjx0VUkrFEjE+9wJm7K6KKG3
        hi/wPw1vdSyP1Bi8vz2B0F/CVVnDPFBhyNqkqrW5nwHy5b80VuWrCB9814fXhfY5ARq
        LxXpVOew60aUOTuZV5pZOCshExBdrbi8tlOaBMQhWAqZlvMWm5Jgl1tFx8iCn5IyH4H
        /XUYstbSJLBmrHC5VqnXam1zBYiansEePqE9LT70iUKCXTPxjZoahE+35TVkj9oHHh9
        VLtpZ/rHl3RoNSvZjQ73Rd5Ufl8diYIGoWdr8o0OZ20/lPbRCp7UQ=='
    }

    In [5]: data = {'publicKey': key.json()['publicKey']}

    In [6]: fingerprint = requests.post(f'{base_url}/ssh/key/fingerprint', json=data)

    In [7]: fingerprint.json()
    Out[7]:
    {'ec2': 'a8:9b:9b:71:85:d8:5a:1d:57:87:5d:ea:28:0f:35:14',
     'openSSH': 'df:13:e9:f0:1d:22:08:73:18:1e:a9:a4:f9:69:cd:82'}

Sample usage of the yolo utility to deploy the infra / build/deploy the lambda service.

Specifiy the profile with your account credentials for AWS
::

    $ export AWS_PROFILE_NAME='personal'

Deploy the account level cloudformation stack. These are resources that will rarely change.
::

    $ yolo deploy-infra --account main
    checking for bucket ssh-key-rest-957704715687...
    uploading s3://ssh-key-rest-957704715687/templates/account/2017-11-07_23-09-54-484093/master.yaml...
    stack "ssh-key-rest-BASELINE-957704715687" does not exist
    creating stack "arn:aws:cloudformation:us-east-1:957704715687:stack/ssh-key-rest-BASELINE-957704715687/c4d8c1b0-c410-11e7-8095-50d5cd24fac6"...
    Still creating stack, please be patient...
    stack "ssh-key-rest-BASELINE-957704715687" created.

Deploy the stage level cloudformation stack.  These are resources that are unique to each stage.
::

    $ yolo deploy-infra --stage josh
    checking for bucket ssh-key-rest-957704715687...
    uploading s3://ssh-key-rest-957704715687/templates/stages/josh/2017-11-07_23-10-39-964428/master.yaml...
    stack "ssh-key-rest-957704715687-josh" does not exist
    creating stack "arn:aws:cloudformation:us-east-1:957704715687:stack/ssh-key-rest-957704715687-josh/dfe92990-c410-11e7-9814-500c286014fd"...
    Still creating stack, please be patient...
    stack "ssh-key-rest-957704715687-josh" created.

Build your lambda code into the zip that will be uploaded to AWS.
::

    $ yolo build-lambda --service ssh-key-rest --stage josh
    Building ssh-key-rest for stage "josh"
    2017-11-07 15:11:32 [WARNING] [yolo.build.python_build_lambda_function:59]: Checking dependencies cache...
    2017-11-07 15:11:32 [WARNING] [yolo.build.python_build_lambda_function:65]: Existing build cache version is c24cb50b103ba1142cece949a20ac9cbf18a7f85
    2017-11-07 15:11:33 [WARNING] [yolo.build.python_build_lambda_function:91]: Build container started, waiting for completion (ID: 2e314b0879)
    2017-11-07 15:11:43 [WARNING] [yolo.build.python_build_lambda_function:94]: Build finished.
    2017-11-07 15:11:43 [WARNING] [yolo.build.remove_container:143]: Removing build container

Deploy the lambda code and apply the API-Gateway settings.
::

    $ yolo deploy-lambda --service ssh-key-rest --stage josh --from-local
    checking for bucket ssh-key-rest-957704715687...
    Deploying ssh-key-rest from local to stage "josh"...
    Function "ssh-key-rest" already exists. Updating...
    Function "ssh-key-rest" updated (version "17").
    Function alias for stage "josh" already exists. Updating...
    Function alias for stage "josh" updated.
    Updating API "ssh-key-rest"...
    Deploying API integrations...
    Creating integration for resource "ANY /{proxy+}"...
    Deploying API to stage "josh"...
    Configuring API Gateway/Lambda base path mapping...
    Domain name is empty, skipping base path mapping.
    Done!

That is it. The service is now up and running.