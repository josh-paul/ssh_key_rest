import falcon

from ssh_key.resources import KeyResource, FingerprintResource


class Service(falcon.API):
    '''
    Class that wraps up the full init of the API.
    '''
    def __init__(self):
        super().__init__()

        self.create_resources()
        self.setup_routes()

    def create_resources(self):
        '''
        Pull in all endpoints to class vars.
        '''
        self.key_res = KeyResource()
        self.fingerprint_res = FingerprintResource()

    def setup_routes(self):
        '''
        Map URI routes to the class vars for endpoints.
        '''
        self.add_route('/ssh/key', self.key_res)
        self.add_route('/ssh/key/fingerprint', self.fingerprint_res)
