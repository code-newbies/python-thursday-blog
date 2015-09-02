import pytest
from big_snake.views import HomeView

class Test_HomeView:
    v = HomeView()
    assert v.template_name == "index.html"
