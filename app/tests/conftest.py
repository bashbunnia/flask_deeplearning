"""
conftest.py: It contents fixture functions used in tests.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018-2023"


from app import create_app
import pytest

@pytest.fixture
def app():
    app = create