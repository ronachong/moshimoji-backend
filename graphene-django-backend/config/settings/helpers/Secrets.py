import os

class Secrets(object):
    '''
    This constructor is used to populate SECRETS as Secrets(sdir).dict in
    inheriting modules.
    '''
    def __init__(self, sdir):
        self.dir = sdir
        self.list = [
            'DJANGO',
            'DB_USERNAME',
            'DB_PASSWORD',
            'DB_ENDPOINT',
            'DB_NAME',
            ]
        self.dict = self.get_dict()

    def read_secret(self, sname):
        with open(os.path.join(self.dir, sname), 'r') as secret:
            return secret.read().rstrip()

    def get_dict(self):
        return { sname: self.read_secret(sname) for sname in self.list }
