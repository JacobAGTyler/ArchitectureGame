import os

import pytest
import drawSvg as dS

from render import RoundedRectangle
from tests.svg_testing import svg_validation


@pytest.fixture
def options_fixture() -> dict:
    return {'stroke': '#222333', 'stroke-width': 9, 'fill': '#888888'}


class TestRoundedRectangle:
    @pytest.mark.usefixtures('options_fixture')
    def test_init(self, options_fixture):
        rr = RoundedRectangle(
            width=100,
            height=100,
            radius=10,
            colour='#888888',
            options=options_fixture,
            x_offset=0,
            y_offset=0
        )

        assert rr.width == 100
        assert rr.height == 100
        assert rr.radius == 10
        assert rr.x_offset == 0
        assert rr.y_offset == 0
        assert rr.x == (-100 / 2) + 0
        assert rr.y == (100 / 2) + 0
        assert rr.options == options_fixture

    @pytest.mark.usefixtures('options_fixture')
    def test_box_path(self, options_fixture):
        rr = RoundedRectangle(
            width=100,
            height=100,
            radius=10,
            colour='#888888',
            options=options_fixture,
            x_offset=0,
            y_offset=0
        )

        path: dS.Path = rr.box_path()
        a, e = svg_validation('output/test_RoundedRectangle.svg', path, 'tests/fixtures/rounded_rectangle.fixture.svg')
        assert a == e
