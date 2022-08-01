import drawSvg as dS

from Component import Component


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
            self.text, self.width, self.options, self.x_offset, self.y_offset, self.text_size, text_colour
        )

    def text_path(self) -> dS.Text:
        path = dS.Text(
            text=self.text,
            fontSize=self.text_size,
            **self.options
        )
        return path


def draw_svg_card(component: Component):
    card_x = 400
    card_y = 500

    margin = 20
    padding = 25

    canvas_x = card_x + (margin * 2)
    canvas_y = card_y + (margin * 2)

    card = dS.Drawing(canvas_x, canvas_y, origin="center", displayInline=False)

    # Card Outline
    card.append(RoundedRectangle(card_x, card_y, 6, colour=component.colour, options={'id': 'card-outline'}).box_path())

    # Component Image
    image_x = round(card_x - (padding * 1.5))
    image_y = round((card_y / 2) - (padding * 2))
    card.append(RoundedRectangle(image_x, image_y, 6, colour='#fff', options={'id': 'image'}).box_path())

    half_x_card = round(card_x / 2)
    half_y_card = round(card_y / 2)
    # quarter_x_card = round(card_x / 4)
    quarter_y_card = round(card_y / 4)

    metric_x = round(half_x_card - (padding * 1.5))
    metric_y = quarter_y_card - padding
    metric_x_offset = round((half_x_card / 2) - (padding / 4))
    metric_y_offset = round(half_y_card - (quarter_y_card / 2) - (padding / 2))

    text_x = metric_x - (padding * 2)

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
            text_colour=component.colour,
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
            text_colour=component.colour,
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

    # Header
    header_x = card_x - (padding * 2)
    heading = Heading(
        text=component.name,
        text_size=40,
        width=header_x,
        options={'id': 'header'},
        text_colour='#fff',
        y_offset=metric_y_offset
    )
    card.append(heading.text_path())

    file_name = f'output/{component.api_name}.svg'
    card.saveSvg(file_name)

# d = dS.Drawing(200, 100, origin='center', displayInline=False)
#
# # Draw an irregular polygon
# d.append(dS.Lines(-80, -45,
#                   70, -49,
#                   95, 49,
#                   -90, 40,
#                   close=False,
#                   fill='#eeee00',
#                   stroke='black'))
#
# # Draw a rectangle
# r = dS.Rectangle(-80, 0, 40, 50, fill='#1248ff')
# r.appendTitle("Our first rectangle")  # Add a tooltip
# d.append(r)
#
# # Draw a circle
# d.append(dS.Circle(-40, -10, 30,
#                    fill='red', stroke_width=2, stroke='black'))
#
# # Draw an arbitrary path (a triangle in this case)
# p = dS.Path(stroke_width=2, stroke='lime',
#             fill='black', fill_opacity=0.2)
# p.M(-10, 20)  # Start path at point (-10, 20)
# p.C(30, -10, 30, 50, 70, 20)  # Draw a curve to (70, 20)
# d.append(p)
#
# # Draw text
# d.append(dS.Text('Basic text', 8, -10, 35, fill='blue'))  # Text with font size 8
# d.append(dS.Text('Path text', 8, path=p, text_anchor='start', valign='middle'))
# d.append(dS.Text(['Multi-line', 'text'], 8, path=p, text_anchor='end'))
#
# # Draw multiple circular arcs
# d.append(dS.ArcLine(60, -20, 20, 60, 270,
#                     stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
# d.append(dS.Arc(60, -20, 20, 60, 270, cw=False,
#                 stroke='green', stroke_width=3, fill='none'))
# d.append(dS.Arc(60, -20, 20, 270, 60, cw=True,
#                 stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))
#
# # Draw arrows
# arrow = dS.Marker(-0.1, -0.5, 0.9, 0.5, scale=4, orient='auto')
# arrow.append(dS.Lines(-0.1, -0.5, -0.1, 0.5, 0.9, 0, fill='red', close=True))
# p = dS.Path(stroke='red', stroke_width=2, fill='none',
#             marker_end=arrow)  # Add an arrow to the end of a path
# p.M(20, -40).L(20, -27).L(0, -20)  # Chain multiple path operations
# d.append(p)
# d.append(dS.Line(30, -20, 0, -10,
#                  stroke='red', stroke_width=2, fill='none',
#                  marker_end=arrow))  # Add an arrow to the end of a line
#
# d.setPixelScale(2)  # Set number of pixels per geometry unit
# # d.setRenderSize(400,200)  # Alternative to setPixelScale
# d.saveSvg('example.svg')
# # d.savePng('example.png')