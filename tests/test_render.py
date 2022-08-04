import os

import pytest

from Component import Component
from render import draw_svg_component
from svg_testing import svg_file_validation


class TestSVGCard:
    def test_draw_svg_card_save(self):
        c = Component(
            name='TestComponent',
            level=1,
            image='firewall.png',
            throughput=1,
            latency=1,
            cost=1,
            base=0,
            colour='#f38181'
        )

        draw_svg_component(c)

        assert os.path.exists('output/test_component-L1.svg')

        a, e = svg_file_validation('output/test_component-L1.svg', 'tests/fixtures/component.fixture.svg')
        assert a == e
