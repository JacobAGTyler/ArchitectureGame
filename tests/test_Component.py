import pytest

from Component import Component


class TestComponent:
    def test_init(self):
        comp = Component(
            name='TestComponent',
            image='test_image',
            throughput=1,
            latency=1,
            cost=1,
            colour='#f38181'
        )

        assert isinstance(comp, Component)

        assert comp.name == 'TestComponent'
        assert comp.api_name == 'test_component'
        assert comp.image == 'test_image'
        assert comp.throughput == 1
        assert comp.latency == 1
        assert comp.cost == 1
        assert comp.colour == '#f38181'

    def test_post_init(self):
        comp = Component(
            name='TestComponent',
            image='test_image',
            throughput=1,
            latency=1,
            cost=1,
            colour='#f38181'
        )

        assert comp.api_name == 'test_component'

    def test_str(self):
        comp = Component(
            name='TestComponent',
            image='test_image',
            throughput=1,
            latency=1,
            cost=1,
            colour='#f38181'
        )

        assert str(comp) == 'TestComponent'
