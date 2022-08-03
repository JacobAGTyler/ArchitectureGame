import os

import pytest

from Component import Component
from render import draw_svg_card
from svg_testing import svg_file_validation


class TestSVGCard:
    def test_draw_svg_card_save(self):
        c = Component(
            name='TestComponent',
            image='test_image',
            throughput=1,
            latency=1,
            cost=1,
            colour='#f38181'
        )

        draw_svg_card(c)

        assert os.path.exists('output/test_component.svg')

        a, e = svg_file_validation('output/test_component.svg', 'tests/fixtures/component.fixture.svg')
        assert a == e
