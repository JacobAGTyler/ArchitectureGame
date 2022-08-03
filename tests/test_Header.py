import drawSvg as dS
import pytest

from render import Heading
from tests.svg_testing import svg_validation


@pytest.fixture
def init_heading():
    return Heading(text='test', width=250, text_size=40, options={})


class TestHeader:
    @pytest.mark.usefixtures('init_heading')
    def test_init(self, init_heading):
        assert isinstance(init_heading, Heading)
        assert init_heading.text == 'test'
        assert init_heading.width == 250
        assert init_heading.text_size == 40
        assert init_heading.options == {
            'fill': '#000000',
            'font-family': 'Verdana',
            'lengthAdjust': 'spacingAndGlyphs',
            'text-anchor': 'middle',
            'textLength': 250,
            'x': 0,
            'y': 20.0,
        }

    @pytest.mark.usefixtures('init_heading')
    def test_text_path(self, init_heading):
        path = init_heading.text_path()

        assert isinstance(path, dS.Text)
        a, e = svg_validation('output/test_Heading.svg', path, 'tests/fixtures/heading.fixture.svg')
        assert a == e


