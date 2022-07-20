
import sys

from flamewok import color as c


class Route:
    def __init__(self, definition):
        self.actions = []
        self.expected = []
        self.callback = definition[1]
        self.validity = 0
        self.is_valid = True

        self.split_definition(definition[0])

    def __str__(self):
        return (
            "<Route- "
            f"Actions: {self.actions} "
            f"Expected: {self.expected} "
            f"Callback: {self.callback.__name__} "
            f"validity: {self.is_valid}-{self.validity} "
            ">")

    def split_definition(self, elements):
        elems = elements.strip().split(" ")
        for elem in elems:
            if elem.startswith("<"):
                if elem.startswith("<int:"):
                    self.expected.append("int")
                elif elem.startswith("<float:"):
                    self.expected.append("float")
                elif elem.startswith("<bool:"):
                    self.expected.append("bool")
                else:
                    self.expected.append("str")
            else:
                self.actions.append(elem)
        if len(self.actions) == 0:
            self.actions.append("")


class CLI:

    def route(self, *definitions):
        self.routes = []
        self.help_content = "| ==========    CLI options    ===========\n"
        for definition in definitions:
            self.build_help_content(definition)
            self.build_routes(definition)
        if len(sys.argv) == 1:
            self.commands = [""]
        else:
            self.commands = sys.argv[1:]
        self.find_route()

    def build_help_content(self, definition):
        if type(definition) == str:
            self.help_content += f"* {definition}"
        else:
            if definition[0] == "":
                self.help_content += "| [no option]"
            else:
                self.help_content += f"| {definition[0]}"
            if len(definition) > 2:
                self.help_content += f" : {definition[2]}"
        self.help_content += "\n"

    def build_routes(self, definition):
        if type(definition) != str:
            route = Route(definition)
            self.routes.append(route)

    def help(self):
        print(self.help_content)

    def find_route(self):
        possibles = []
        for route in self.routes:
            possibles.append(self.valid_route(route))
        possibles = [possible for possible in possibles if possible.is_valid]
        if len(possibles) >= 1:
            self.compare_validity_scores(possibles)
        else:
            only_arg = [route for route in self.routes if route.actions[0] == "" and len(route.expected) > 0]
            if len(only_arg) == 1:
                self.execute_route(only_arg[0])
            else:
                print(f"{c.warning}Command not found{c.end}")
                exit()

    def valid_route(self, route):
        len_actions = len(route.actions)
        len_command = len(self.commands)
        if len_actions > len_command:
            route.is_valid = False
        else:
            index = 0
            route.validity += 1
            for action in route.actions:
                if route.is_valid:
                    if action != self.commands[index]:
                        route.is_valid = False
                    route.validity += 1
                index += 1

        return route

    def sort_scores(self, routes):
        """Keep only the routes with the best score"""
        routes = sorted(routes, key=lambda x: x.validity, reverse=True)
        max_validity = routes[0].validity
        routes = [possible for possible in routes if possible.validity == max_validity]
        return routes

    def compare_validity_scores(self, possibles):
        possibles = self.sort_scores(possibles)
        if len(possibles) > 1:
            for route in possibles:
                if len(self.commands) == len(route.actions) and \
                        len(route.expected) == 0:
                    route.validity += 1
                if len(self.commands) > len(route.actions) and \
                        len(route.expected) > 0:
                    route.validity += 1

            possibles = self.sort_scores(possibles)
            if len(possibles) > 1:
                if possibles[0].validity == possibles[1].validity:
                    print(f"{c.warning}CLI route conflict !{c.end}")
                    exit()
        self.execute_route(possibles[0])

    def convert_arguments(self, route, arguments):
        # print(route.expected, arguments)
        converted = []
        if len(route.expected) > len(arguments):
            index = len(arguments)
        else:
            index = len(route.expected)
        if index == 0:
            return arguments

        for i in range(index):
            if route.expected[i] == "int":
                try:
                    converted.append(int(arguments[i]))
                except ValueError:
                    print(f"{c.warning}Aborted !{c.end}")
                    print(
                        f"{c.warning}Expected 'int' type,"
                        f" received: {arguments[i]}{c.end}")
                    exit()

            if route.expected[i] == "float":
                try:
                    converted.append(float(arguments[i]))
                except ValueError:
                    print(f"{c.warning}Aborted !{c.end}")
                    print(
                        f"{c.warning}Expected 'float' type,"
                        f" received: {arguments[i]}{c.end}")
                    exit()
            if route.expected[i] == "bool":
                try:
                    converted.append(bool(int(arguments[i])))
                except ValueError:
                    print(f"{c.warning}Aborted !{c.end}")
                    print(
                        f"{c.warning}Expected 'bool' type (0 or 1),"
                        f" received: {arguments[i]}{c.end}")
                    exit()
            if route.expected[i] == "str":
                converted.append(arguments[i])

        if len(route.expected) < len(arguments):
            converted = [*converted, *arguments[index:]]

        return converted

    def execute_route(self, route):
        callback = route.callback
        if route.actions[0] == "":
            index = 0
        else:
            index = len(route.actions)
        arguments = self.commands[index:]
        # values convertions
        if len(arguments) == 0 or arguments[0] != "":
            arguments = self.convert_arguments(route, arguments)
            callback(*arguments)
        else:
            callback()


cli = CLI()
