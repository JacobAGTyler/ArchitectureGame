import pytest

from Component import Component

@pytest.fixture
def component_kwargs():
    return {
        'name': 'TestComponent',
        'level': 1,
        'image': 'test_image',
        'throughput': 1,
        'latency': 1,
        'min_latency': 1,
        'base': 2,
        'cost': 1,
        'colour': '#f38181'
    }


class TestComponent:
    @pytest.mark.usefixtures('component_kwargs')
    def test_init(self, component_kwargs):
        comp = Component(**component_kwargs)
        assert isinstance(comp, Component)

        assert comp.name == 'TestComponent'
        assert comp.api_name == 'test_component'
        assert comp.image == 'test_image'
        assert comp.throughput == 1
        assert comp.latency == 1
        assert comp.price == 3
        assert comp.colour == '#f38181'

    @pytest.mark.usefixtures('component_kwargs')
    def test_post_init(self, component_kwargs):
        comp = Component(**component_kwargs)

        assert comp.api_name == 'test_component'

    @pytest.mark.usefixtures('component_kwargs')
    def test_str(self, component_kwargs):
        comp = Component(**component_kwargs)

        assert str(comp) == 'TestComponent - level 1 [L: 1ms T: 1m/s P: $3]'
