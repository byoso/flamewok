
import flamewok
from flamewok.cli import cli

infos = f"""
=============================  flamewok  ===============================

Very tiny framework to quickly build python terminal applications.

version {flamewok.__version__}
home page: https://github.com/byoso/flamewok
pypi: https://pypi.org/project/flamewok/

"""


def cmd():
    print(infos)


if __name__ == "__main__":
    cli.route(
        ("", cmd, "show this help"),
        ("-h", cmd, "show this help"),
        ("--help", cmd, "show this help"),
    )