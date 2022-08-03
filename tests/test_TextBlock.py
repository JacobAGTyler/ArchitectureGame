import drawSvg as dS
import pytest

from render import TextBlock
from tests.svg_testing import svg_validation


@pytest.fixture
def init_text_block():
    return TextBlock(text='test', width=100, text_size=12, options={})


class TestTextBlock:
    @pytest.mark.usefixtures('init_text_block')
    def test_init(self, init_text_block):
        assert isinstance(init_text_block, TextBlock)
        assert init_text_block.text == 'test'
        assert init_text_block.width == 100
        assert init_text_block.text_size == 12
        assert init_text_block.options == {
            'fill': '#000000',
            'font-family': 'Verdana',
            'text-anchor': 'middle',
            'x': 0,
            'y': 6,
        }

    @pytest.mark.usefixtures('init_text_block')
    def test_text_path(self, init_text_block):
        path = init_text_block.text_path()

        assert isinstance(path, dS.Text)
        a, e = svg_validation('output/test_TextBlock.svg', path, 'tests/fixtures/text_block.fixture.svg')
        assert a == e


