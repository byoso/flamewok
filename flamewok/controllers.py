
class Handler:
    """Built with a dict as argument, this dict connects signals
    to functions or methods"""

    def __init__(self, actions=None):
        if actions:
            self.actions = actions
        else:
            self.actions = {}

    def ___str__(self):
        return print(f"<Handler: {len(self.actions)} signals>")

    def __repr__(self):
        return str(self)

    def handle(self, response):
        """return the apropriate action,
        and if so, a list of other signals as parameter"""
        return self.actions[response]()

    def connect(self, connexions):
        """connexions must be a list of tuples"""
        for connexion in connexions:
            self.actions[connexion[0]] = connexion[1]
