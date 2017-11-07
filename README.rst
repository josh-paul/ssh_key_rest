SSH Key Rest API
================

A simple RESTful API for get a new SSH keypair and fingerprinting an existing SSH public key.

This repository is a sample of using the yolo utility (http://yolocli.readthedocs.io/en/latest/) to 
deploy a stateless REST service running on AWS via API-Gateway and Lambda. Everything needed to 
work with service is contained in the repository.

It uses CloudFormation to define the resources required outside of API-Gateway and Lambda. Then 
the yolo utility builds the Lambda source files and can deploy them.

Sample usage of the API.
::

    In [1]: import requests

    In [2]: url = 'https://ne6vxja6h7.execute-api.us-east-1.amazonaws.com/josh/ssh/key'

    In [3]: get = requests.get(url)

    In [4]: get.json()
    Out[4]:
    {'privateKey': 
        '-----BEGIN RSA PRIVATE KEY-----\n
        MIIEpQIBAAKCAQEA9YNLdHlF+/4L2Lcwa1tTam8iRxFIE2ylkmH9MrrCalaQrjze\n
        l3FJD1TqkrEf0dDUtTmcQuEgGJnavfs17k5rUCb0y5fQnkqN4erN/RW9rtuGx5Wt\n
        weuSSuCodW0Hq7yq5x81YTA+v52cbdmshRXxyLlvjJPkPQL0bwDffnbQul2Q1QW/\n
        X4oOkotNzt0y9FEbrZpNRZyDYwFHDu2PJkV0FI47eLt+NG+heD3qsav8UG7IP9dv\n
        gBIBqMwSGuuJqADOgEHrWYk7U6Vyv8hYylctYz/9im9UZgRDHaWJDBEqV+dxx1hF\n
        NC/1Ki6vdnxW7m9Qqi19QPUO4QQfIyB4vEyVQwIDAQABAoIBAQC+AX7EBZdEDrjc\n
        X+n5LBTCqn+8wIMnhU4em/d461DLO3N9ZV5fli0U0IM6RBp8J0J3fr6Qg+pzH59K\n
        qMB0Tfx/a6bIahXqa4ii7zW8SLckPIFytURkcAwoJvY46silAL7DYEPPk6b8ZN5L\n
        pcr+tJ0K23iZM1vQXBkQT3yoQwwHLh54A4OSDS+ih5W37AoS7DhtmZ+/WEH/rzyJ\n
        RgvawpE64vqEqyW+1kg1ds6mIb7niVhW/sgmo0Cn4gZpR1Zo6bU8cfdxk52feQ3r\n
        hN/STQ7qDbYmTH257HetH5OHhDPsc3OU4/ZipVjuwX0GdUMQrC3xR/SMuhiKv2hv\n
        XyjuqIIBAoGBAP0F5qrwVQrJbkA91cxunlrN08prEl2TdtGItOgjLrb9ffTko7VL\n
        FnUJOHTu4NYg6kW4+ta4bwQwrRaZBHGDLfopLuLVBZYLhD3CQPMsIc3uGHg7AD7t\n
        xo2fjU3LXvCAC4wHrtEheCl9L0HZQ7XQHFyMP5m51/kcGClfJa23sW/pAoGBAPhm\n
        xfI+/cS3Os+MLLM/KmDN6vIsJQh0rtGgDO/Z1HURTv8mjsSpaKSz1NLO/GK04v8N\n
        cqXVytjpKtzDPx8Bxj2dx/2ETAIOWszKZUKdLKUdeB2EZbIbKEzdG/FnqbBPgPb9\n
        FHr8IKQA2g8WlmvJ78p1hVwTEo9dboc3Gde1NuxLAoGBAJShvMi5eRtnDE7MhCUc\n
        7gTlV/5WO2mg0HFx3uNml3CDJFSRYuGChGSnz/RQxt7CYxwl96Pen8hUV7kolgWg\n
        S4fiXVp+TFPB3CLzU3gFeq4fqVwnPJO61aIoEbebOeAJN79AXB8ZjB7DHNmPqUjK\n
        QX7UHCBPnWEGceMLs3SCrcbRAoGBAJkYfpe3SyCa7ZxNgJ9ZJv1S7KMlog18HOMG\n
        CfMqBk/AwzduxD9hSiV40Iq9F8CeS+l2mFqtUcAutUQq8hRiO5RuUnxltZLu1fey\n
        JobP6Fw7tXQ7zZHgOw5kmHxIr8UCuzF++chy7IsoGz2BZmQ4qZnWpMMC3kWOCDk+\n
        NKdGAPvRAoGAV20eiTYeyQYCaA2lznF2UHpn/gcJq5mGEpczl4YeEoI4PBIGP8sa\n
        9oZI5GqqcQAnPrTWNSFqOn2GlWuRNOGu+VFVJvI4mV5ruwcMCZj3F+BAG5H4QA28\n
        eFcAhSbOFVtb7beORGQEcAxhLvCfL2TbbkG+hPjnW9b3aFxAk3wm7xs=\n
        -----END RSA PRIVATE KEY-----\n',
     'publicKey': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD1g0t0eUX7/gvYtzB
        rW1NqbyJHEUgTbKWSYf0yusJqVpCuPN6XcUkPVOqSsR/R0NS1OZxC4SAYmdq9+zXuT
        mtQJvTLl9CeSo3h6s39Fb2u24bHla3B65JK4Kh1bQervKrnHzVhMD6/nZxt2ayFFfH
        IuW+Mk+Q9AvRvAN9+dtC6XZDVBb9fig6Si03O3TL0URutmk1FnINjAUcO7Y8mRXQUj
        jt4u340b6F4Peqxq/xQbsg/12+AEgGozBIa64moAM6AQetZiTtTpXK/yFjKVy1jP/2
        Kb1RmBEMdpYkMESpX53HHWEU0L/UqLq92fFbub1CqLX1A9Q7hBB8jIHi8TJVD'
    }

    In [5]: data = {'publicKey': get.json()['publicKey']}

    In [6]: post = requests.post(url, json=data)

    In [7]: post.json()
    Out[7]:
    {'ec2': 'd9:f9:ee:6b:f4:8f:9b:b1:7a:fd:9e:53:34:86:0e:ca',
     'openSSH': '71:99:3f:4d:bc:83:0a:a1:ce:4f:d4:be:bd:4a:89:11'}

Sample usage of the yolo utility to deploy the infra / build/deploy the lambda service.
::

    $ export AWS_PROFILE_NAME='personal'
    $ yolo deploy-infra --account main
    checking for bucket ssh-key-rest-957704715687...
    uploading s3://ssh-key-rest-957704715687/templates/account/2017-11-07_23-09-54-484093/master.yaml...
    stack "ssh-key-rest-BASELINE-957704715687" does not exist
    creating stack "arn:aws:cloudformation:us-east-1:957704715687:stack/ssh-key-rest-BASELINE-957704715687/c4d8c1b0-c410-11e7-8095-50d5cd24fac6"...
    Still creating stack, please be patient...
    stack "ssh-key-rest-BASELINE-957704715687" created.
    $ yolo deploy-infra --stage josh
    checking for bucket ssh-key-rest-957704715687...
    uploading s3://ssh-key-rest-957704715687/templates/stages/josh/2017-11-07_23-10-39-964428/master.yaml...
    stack "ssh-key-rest-957704715687-josh" does not exist
    creating stack "arn:aws:cloudformation:us-east-1:957704715687:stack/ssh-key-rest-957704715687-josh/dfe92990-c410-11e7-9814-500c286014fd"...
    Still creating stack, please be patient...
    stack "ssh-key-rest-957704715687-josh" created.
    $ yolo build-lambda --service ssh-key-rest --stage josh
    Building ssh-key-rest for stage "josh"
    2017-11-07 15:11:32 [WARNING] [yolo.build.python_build_lambda_function:59]: Checking dependencies cache...
    2017-11-07 15:11:32 [WARNING] [yolo.build.python_build_lambda_function:65]: Existing build cache version is c24cb50b103ba1142cece949a20ac9cbf18a7f85
    2017-11-07 15:11:33 [WARNING] [yolo.build.python_build_lambda_function:91]: Build container started, waiting for completion (ID: 2e314b0879)
    2017-11-07 15:11:43 [WARNING] [yolo.build.python_build_lambda_function:94]: Build finished.
    2017-11-07 15:11:43 [WARNING] [yolo.build.remove_container:143]: Removing build container
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
