
class Signal(list):
    """Same as a list, but it is a signal"""
    pass


class Handler:
    """Built with a dict as argument, this dict connects signals
    to functions or methods"""
    def __init__(self, actions):
        self.actions = actions

    def handle(self, response):
        """return the apropriate action,
        and if so, a list of other signals as parameter"""
        if len(response) == 1:
            return self.actions[response[0]]()
        else:
            return self.actions[response[0]](response[1:])


def menucall(func, handler, signal):
    def wrapper(*args, **kwargs):
        handler.actions[signal] = func.__name__
        func(*args, **kwargs)
    return wrapper
