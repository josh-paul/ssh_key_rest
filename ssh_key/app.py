import falcon

from ssh_key.resources import KeyResource


class Service(falcon.API):
    def __init__(self):
        super().__init__()

        self.create_resources()
        self.setup_routes()

    def create_resources(self):
        self.key_res = KeyResource()

    def setup_routes(self):
        self.add_route('/ssh/key', self.key_res)
