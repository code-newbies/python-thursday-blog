import pytest
import ./views

class Test_HomeView:
    v = views.HomeView()
    assert v.template_name == "index.html"
