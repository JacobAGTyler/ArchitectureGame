import yaml

from Component import Component
from render import draw_svg_card


def main():
    with open('components.yml', 'r') as f:
        components: [dict] = yaml.safe_load(f)

    component: dict
    for component in components:
        c = Component(**component)
        draw_svg_card(c)
        print(c)


if __name__ == '__main__':
    main()
