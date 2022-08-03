import os

import drawSvg as dS


def svg_validation(test_file_path: str, drawing_object: dS.DrawingBasicElement, fixture_file_path: str):
    drawing = dS.Drawing(width=200, height=200)

    with open(test_file_path, 'w') as f:
        drawing.append(drawing_object)
        drawing.asSvg(f)

    return svg_file_validation(test_file_path, fixture_file_path)


def svg_file_validation(test_file_path: str, fixture_file_path: str):
    with open(fixture_file_path, 'r') as fixture_file:
        fixture_svg = fixture_file.read()

    with open(test_file_path, 'r') as f:
        svg = f.read()

    os.remove(test_file_path)

    return svg, fixture_svg
