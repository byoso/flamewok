
class Handler:
    """Built with a dict as argument, this dict connects signals
    to functions or methods"""
    handlers = []

    def __init__(self, actions=None):
        if actions:
            self.actions = actions
        else:
            self.actions = {}
        self.handlers.append(self)

    def ___str__(self):
        return print(f"<Handler: {len(self.actions)} signals>")

    def __repr__(self):
        return str(self)

    def handle(self, response):
        """return the apropriate action,
        and if so, a list of other signals as parameter"""

        print("\n===self.handler.actions :")
        for action in self.actions:
            print(action)

        if len(response) == 1:
            return self.actions[response[0]]()
        else:
            return self.actions[response[0]](response[1:])

    def connect(self, connexions):
        for connexion in connexions:
            self.actions[connexion[0]] = connexion[1]
