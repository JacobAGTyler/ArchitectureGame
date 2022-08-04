import os

import drawSvg as dS

from Component import Component
from ChanceCard import ChanceCard


class RoundedRectangle:
    def __init__(
            self,
            width: int,
            height: int,
            radius: int,
            colour: str,
            options: dict,
            x_offset: int = 0,
            y_offset: int = 0
    ):
        self.width = width
        self.height = height
        self.radius = radius
        self.x_offset = x_offset
        self.y_offset = y_offset

        self.x = (-self.width / 2) + self.x_offset
        self.y = (self.height / 2) + self.y_offset

        self.options = {'stroke': '#000000', 'stroke-width': 1} | options | {'fill': colour}

    def box_path(self) -> dS.Path:
        internal_x = self.width - (2 * self.radius)
        internal_y = self.height - (2 * self.radius)

        path = dS.Path(**self.options)
        path.M(self.x + self.radius, self.y)
        path.h(internal_x)
        path.a(rx=self.radius, ry=self.radius, rot=0, largeArc=0, sweep=1, ex=self.radius, ey=(-self.radius))
        path.v(-internal_y)
        path.a(rx=self.radius, ry=self.radius, rot=0, largeArc=0, sweep=1, ex=(-self.radius), ey=(-self.radius))
        path.h(-internal_x)
        path.a(rx=self.radius, ry=self.radius, rot=0, largeArc=0, sweep=1, ex=(-self.radius), ey=self.radius)
        path.v(internal_y)
        path.a(rx=self.radius, ry=self.radius, rot=0, largeArc=0, sweep=1, ex=self.radius, ey=self.radius)

        return path


class TextBlock:
    def __init__(
            self,
            text: str,
            options: dict,
            width: int = None,
            x_offset: int = 0,
            y_offset: int = 0,
            text_size: int = 12,
            text_colour: str = '#000000'
    ):
        self.text = text
        self.width = width
        self.options = options

        self.x_offset = x_offset
        self.y_offset = y_offset
        self.text_size = text_size

        self.options['fill'] = text_colour
        self.options['font-family'] = 'Verdana'
        self.options['text-anchor'] = 'middle'

        self.options['x'] = self.x_offset
        self.options['y'] = self.y_offset + (self.text_size / 2)

    def text_path(self) -> dS.Text:
        path = dS.Text(
            text=self.text,
            fontSize=self.text_size,
            **self.options
        )
        return path


class Heading(TextBlock):
    def __init__(
            self,
            text: str,
            width: int,
            options: dict,
            x_offset: int = 0,
            y_offset: int = 0,
            text_size: int = 12,
            text_colour: str = '#000000'
    ):

        self.text = text
        self.width = width
        self.options = options

        self.x_offset = x_offset
        self.y_offset = y_offset
        self.text_size = text_size

        self.options['lengthAdjust'] = 'spacingAndGlyphs'
        self.options['textLength'] = self.width

        self.options['x'] = self.x_offset
        self.options['y'] = self.y_offset + (self.text_size / 2)

        super().__init__(
            self.text, self.options, self.width, self.x_offset, self.y_offset, self.text_size, text_colour
        )

    def text_path(self) -> dS.Text:
        path = dS.Text(
            text=self.text,
            fontSize=self.text_size,
            **self.options
        )
        return path


card_x = 400
card_y = 500

margin = 20
padding = 25

canvas_x = card_x + (margin * 2)
canvas_y = card_y + (margin * 2)

half_x_card = round(card_x / 2)
half_y_card = round(card_y / 2)
quarter_x_card = round(card_x / 4)
quarter_y_card = round(card_y / 4)


def draw_svg_component(component: Component):
    card = dS.Drawing(canvas_x, canvas_y, origin="center", displayInline=False)

    # Card Outline
    card.append(RoundedRectangle(card_x, card_y, 6, colour=component.colour, options={'id': 'card-outline'}).box_path())

    # Component Image
    image_x = round(card_x - (padding * 1.5))
    image_y = round((card_y / 2) - (padding * 2))
    card.append(RoundedRectangle(image_x, image_y, 6, colour='#fff', options={'id': 'image'}).box_path())

    image_include_x = round(image_x - (padding * 2))
    image_include_y = round(image_y - (padding * 2))

    img = dS.Image(
        x=0 - (image_include_x / 2), y=0 - (image_include_y / 2),
        width=image_include_x,
        height=image_include_y,
        path=f'icons/{component.image}',
        embed=True,
        options={'id': 'image-image'}
    )
    card.append(img)

    metric_x = round(half_x_card - (padding * 1.5))
    metric_y = quarter_y_card - padding
    metric_x_offset = round((half_x_card / 2) - (padding / 4))
    metric_y_offset = round(half_y_card - (quarter_y_card / 2) - (padding / 2))

    text_x = metric_x - (padding * 2)

    # Header
    header_x = card_x - (padding * 2)
    heading = Heading(
        text=component.name,
        text_size=40,
        width=header_x,
        options={'id': 'header'},
        text_colour='#000',
        y_offset=metric_y_offset
    )
    card.append(heading.text_path())

    level_x = round(card_x / 4)
    level_heading = TextBlock(
        text=f'LEVEL {component.level}',
        text_size=30,
        options={'id': 'level'},
        text_colour='#000',
        y_offset=quarter_y_card,
        x_offset=-level_x
    )
    card.append(level_heading.text_path())

    price = TextBlock(
        text=f'${component.price}.00',
        text_size=30,
        options={'id': 'price'},
        y_offset=quarter_y_card,
        x_offset=level_x,
        text_colour='#000',
    )
    card.append(price.text_path())

    # Latency
    card.append(
        RoundedRectangle(
            metric_x,
            metric_y,
            6,
            colour='#fff',
            options={'id': 'latency'},
            x_offset=-metric_x_offset,
            y_offset=-metric_y_offset
        ).box_path()
    )
    card.append(
        Heading(
            text=f'{component.latency} ms',
            width=text_x,
            x_offset=-metric_x_offset,
            y_offset=-(half_y_card - round(metric_y / 2)),
            text_colour='#000',
            text_size=40,
            options={'id': 'latency-text'}
        ).text_path()
    )
    card.append(
        Heading(
            text=f'LATENCY',
            width=text_x,
            x_offset=-metric_x_offset,
            y_offset=-(half_y_card - round(padding * 1.25)),
            text_colour='#888',
            text_size=20,
            options={'id': 'latency-title'}
        ).text_path()
    )

    # Throughput
    card.append(
        RoundedRectangle(
            metric_x,
            metric_y,
            6,
            colour='#fff',
            options={'id': 'throughput'},
            x_offset=metric_x_offset,
            y_offset=-metric_y_offset
        ).box_path()
    )
    card.append(
        Heading(
            text=f'{component.throughput} m/s',
            width=text_x,
            x_offset=metric_x_offset,
            y_offset=-(half_y_card - round(metric_y / 2)),
            text_colour='#000',
            text_size=40,
            options={'id': 'throughput-text'}
        ).text_path()
    )
    card.append(
        Heading(
            text=f'THROUGHPUT',
            width=text_x,
            x_offset=metric_x_offset,
            y_offset=-(half_y_card - round(padding * 1.25)),
            text_colour='#888',
            text_size=20,
            options={'id': 'throughput-title'}
        ).text_path()
    )

    file_name = f'output/{component.api_name}-L{component.level}.svg'
    card.setPixelScale(2)
    card.saveSvg(file_name)
    # card.savePng(f'output/{component.api_name}-L{component.level}.png')


def draw_svg_chance_card(chance_card: ChanceCard):
    chance_colour = '#ffa500'
    card = dS.Drawing(canvas_y, canvas_x, origin="center", displayInline=False)

    # Card Outline
    card.append(RoundedRectangle(card_y, card_x, 6, colour=chance_colour, options={'id': 'card-outline'}).box_path())

    # Component Image
    image_x = round(card_y - (padding * 2))
    image_y = round((card_x / 1.5) - (padding * 2))
    card.append(RoundedRectangle(image_x, image_y, 6, colour=chance_colour, options={'id': 'image-box'}).box_path())

    image_include_x = round(image_x - (padding * 2))
    image_include_y = round(image_y - (padding * 2))

    img = dS.Image(
        x=0 - (image_include_x / 2), y=0 - (image_include_y / 2),
        width=image_include_x,
        height=image_include_y,
        path=f'icons/direction.png',
        embed=True,
        options={'id': 'image-image'}
    )
    card.append(img)

    # Header
    text_y = round(half_x_card - (quarter_x_card / 2) - (padding / 2))
    title = TextBlock(
        text=chance_card.title,
        text_size=40,
        options={'id': 'header'},
        text_colour='#000',
        y_offset=text_y - padding
    )
    card.append(title.text_path())

    text_list = chance_card.text.split()
    first_line = ' '.join(text_list[:len(text_list) // 2])
    second_line = ' '.join(text_list[len(text_list) // 2:])

    text = TextBlock(
        text=first_line,
        text_size=20,
        options={'id': 'text-l-1'},
        text_colour='#000',
        y_offset=-text_y - padding
    )
    card.append(text.text_path())
    text = TextBlock(
        text=second_line,
        text_size=20,
        options={'id': 'text-l-2'},
        text_colour='#000',
        y_offset=-text_y - (padding * 2)
    )
    card.append(text.text_path())

    if not os.path.exists('output/chance/'):
        os.mkdir('output/chance/')

    file_name = f'output/chance/{chance_card.title}.svg'
    card.setPixelScale(2)
    card.saveSvg(file_name)
    # card.savePng(f'output/{component.api_name}-L{component.level}.png')
