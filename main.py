import yaml

from Component import Component
from ChanceCard import ChanceCard
from render import draw_svg_component, draw_svg_chance_card


def main():
    with open('components.yml', 'r') as f:
        components: [dict] = yaml.safe_load(f)

    component: dict
    for component in components:
        for level in range(1, 6):
            component['level'] = level
            c = Component(**component)
            draw_svg_component(c)
            print(c)

    with open('chance-cards.yml', 'r') as f:
        chance_cards: [dict] = yaml.safe_load(f)

    chance_card: dict
    for chance_card in chance_cards:
        c = ChanceCard(**chance_card)
        draw_svg_chance_card(c)
        print(c)


if __name__ == '__main__':
    main()
