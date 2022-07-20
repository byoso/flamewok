"""Use it with pytest:

pytest -v --cov=flamewok
"""


from flamewok import color as c
from flamewok.validators import check_type
from flamewok.menu import (
    TextBox,
    ActionBox,
    Menu,
)
from flamewok.cli import CLI
from flamewok import cmd


class TestForm:

    def test_response(self, form, monkeypatch):
        """tests Response, then also Form and Field"""

        # creating iterator object
        answers = iter(['mike', '13'])

        # using lambda statement for mocking
        monkeypatch.setattr('builtins.input', lambda x: next(answers))
        monkeypatch.setattr('builtins.input', lambda x: next(answers))

        response = form.ask()
        assert response.name == 'mike'
        assert response.age == '13'

        with_bad_answer = iter(['jane', 'twenty', '20'])
        monkeypatch.setattr('builtins.input', lambda x: next(with_bad_answer))
        monkeypatch.setattr('builtins.input', lambda x: next(with_bad_answer))
        response_2 = form.ask()
        assert response_2.name == 'jane'
        assert response_2.age == '20'
        assert 'jane' in str(response_2)


class TestValidators:
    def test_check_type(self):
        assert check_type("text", str) is True
        assert check_type("8", int) is True
        assert check_type("text", int) is False
        assert check_type("true", bool) is True
        assert check_type("True", bool) is True
        assert check_type("text", bool) is False


class TestColor:
    def test_color(self):
        text = f"{c.danger}text{c.end}"
        assert text == "\x1b[0;30;31mtext\x1b[0m"

    def test_palette(self, capsys):
        c.palette()
        captured = capsys.readouterr()
        assert "0;30;41" in captured.out


class TestMenu:
    def test_text_box(self):
        box = TextBox("text")
        assert box.label == "text"

    def test_action_box(self):
        box = ActionBox("p", "show", print)
        assert box.choice == "p"
        assert box.label == "show"
        assert box.func == print

    def test_menu(self, monkeypatch, capsys):
        menu = Menu()
        def mock_func():
            print("test_func")
        menu.add_boxes([
            "text_box\n",
            ("x", "exit", mock_func)
        ])
        assert menu.boxes[0].label == "text_box\n"
        assert menu.boxes[1].choice == "x"
        assert menu.boxes[1].label == "exit"
        assert menu.boxes[1].func == mock_func

        # creating iterator object
        answers = iter(['x'])

        # using lambda statement for mocking
        monkeypatch.setattr('builtins.input', lambda x: next(answers))
        menu.ask()
        captured = capsys.readouterr()

        print(captured.out)
        assert captured.out.startswith('text_box\nx')
        assert captured.out.endswith('test_func\n')


class TestCli:
    def test_cli(self, capsys):
        def mock_func():
            # print("===== mock func")
            print("test_func")

        my_cli = CLI()
        my_cli.routes = []
        my_cli.help_content = ""
        definition = "HELP"
        definition_2 = ('test', mock_func, "mock_func")
        my_cli.build_routes(definition)
        my_cli.build_help_content(definition)
        my_cli.build_routes(definition_2)
        my_cli.build_help_content(definition_2)
        assert my_cli.help_content.startswith("* HELP")
        my_cli.commands = ["test"]
        my_cli.find_route()
        captured = capsys.readouterr()
        assert captured.out == "test_func\n"
