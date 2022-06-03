"""
This script allows to create veeeery quicly a CLI

Example:

if __name__ == "__main__":
    cli.route(
        "This is a test, to try my new CLI toy\n",
        ("", main, "Launches the main programm"),
        ("-h", cli.help, "displays this help"),
        ("--help", cli.help, 'Idem'),
        ("see <int:a> <bool:> <str:> <float:>", see, "Show the arguments given in the CLI"),
        ("test 2", test2, "calls the test2 function"),
        ("multi <float:a> <float:b>", multi, "calculate arg_a x arg_b"),
        ("add <numbers>", add, "print the addition of the given numbers")
    )

Each route takes a path with or without parameters '<>', a callback
function that revieve the parameters if there are some, and an optionnal
description.

that's all !
note that cli.help is an auto-created help.
"""


import sys


class CLI_Error(Exception):
    pass


class CLI:
    def __call__(self):
        print(sys.argv)

    def route(self, *args, debug=False,):
        """
        CLI.route takes the place of an __init__ method,
        but is explicitly called.
        args are tuples like this:
        ("path", function)
        """
        self.routes = []
        self.description = "| "
        self.debug = debug

        for arg in args:
            self.set_route(arg)

        command = sys.argv
        self.decode_command(command)

    def set_route(self, arg):
        if type(arg) == str:
            self.description += arg
        elif type(arg) == tuple:
            path = arg[0]
            function = arg[1]
            if len(arg) >= 3:
                help = arg[2]
            else:
                help = None
            elems = path.strip().split(" ")
            actions = []
            arguments = []
            now_parameters = False
            for elem in elems:
                if elem.startswith("<"):
                    now_parameters = True
                    if elem.startswith("<int:"):
                        arguments.append(int)
                    elif elem.startswith("<float:"):
                        arguments.append(float)
                    elif elem.startswith("<bool:"):
                        arguments.append(bool)
                    else:
                        arguments.append(str)
                else:
                    if now_parameters:
                        raise CLI_Error("actions must not be set after parameters")
                    actions.append(elem)

            self.routes.append({
                'path': path.strip(),
                'actions': actions,
                'function': function,
                'arguments': arguments,
                'help': help,
                })

    def find_route(self, commands, routes, index=0):
        if len(commands) < index:
            if self.debug:
                raise CLI_Error("CLI route not found")
            else:
                print("Command not found")
                exit()
        if len(commands) == 0:
            routes = [route for route in routes if route['path'] == '']
            if len(routes) != 1:
                raise CLI_Error("Bad routing")
        if len(routes) == 1:
            return routes[0]

        best = []
        for route in routes:
            if len(route['actions']) > index and len(commands) > index:
                if route['actions'][index] == commands[index]:
                    best.append(route)
        index += 1

        return self.find_route(commands, best, index)

    def decode_command(self, command):
        commands = command[1:]
        routes = self.routes[:]

        route = self.find_route(commands, routes)

        index = len(route['actions'])
        args = commands[index:]
        if len(args) <= len(route['arguments']):
            min = len(args)
            max = None
        else:
            min = len(route['arguments'])
            max = len(args)

        params = []
        for i in range(min):
            if route['arguments'][i] == bool:
                params.append(route['arguments'][i](int(args[i])))
            else:
                params.append(route['arguments'][i](args[i]))

        if max is not None:
            params = [*params, *args[min:max]]

        return route['function'](*params)

    def help(self):
        message = "| ===         CLI options:                ===\n"
        message += self.description + "\n"
        for route in self.routes:
            if route['path'] == '':
                message += '| == Is executable without any option'
                if route['help'] is not None:
                    message += " : " + route['help']
                message += "\n"
            else:
                # descr = route['function'].__name__
                message += "| " + route['path']
                # message += " -> " + f"{descr}()"
                if route['help'] is not None:
                    message += " : " + route['help']
                message += "\n"
        print(message)


cli = CLI()
