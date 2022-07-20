"""REMINDER:

pip install pytest
pip install coverage
pip install pytest-cov

pytest -vs --cov=flamewok

"""

import pytest

from flamewok.form import Form
from flamewok.validators import check_type


@pytest.fixture
def form():
    form = Form([
        ("name", "What's your name"),
        ("age", "how old are you", lambda x: check_type(x, int))
    ])
    yield form
