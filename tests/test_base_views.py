import pytest
from big_snake.views import HomeView

def test_template_name():
    v = HomeView()
    assert v.template_name == "index.html"
