#!/usr/bin/env python3

letter: str = input('Enter your letter: ')
fonts = list()


def main():
    with open('fonts.txt') as f:
        for line in f:
            fonts.append(line.rstrip())
    with open(f"output/{letter}.svg", 'w') as f:
        f.write(style())


colors = [
    '#000000', '#808080', '#A6AAAE', '#ffffff', '#fffac8', '#ffd8b1',
    '#f58231', '#ffe119', '#bcf60c', '#3cb44b', '#aaffc3', '#46f0f0',
    '#008080', '#0086A7', '#4363d8', '#911eb4', '#f032e6', '#e6beff']


def get_color():
    for color in colors:
        yield color


def svg(func):
    size = 64
    head = f"""<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink">"""
    tail = "</svg>"

    def body():
        result = []
        for i in range(len(fonts)):
            result.append(f'<use xlink:href="#letter" class="fnt{i}" />\n')
        return ''.join(result)

    def wrapped():
        return f"{head}\n{func()}\n{body()}{tail}"
    return wrapped


def defs(func):
    defs_o = "<defs><style>"
    style_o = "svg {background-color: white; font-size: 1.6em;}"
    style_c = "</style>"
    text = f"""<text id="letter" text-anchor="middle" x="32" y="32">{letter}
            </text>"""
    defs_c = "</defs>"

    def wrapped():
        return f"{defs_o}\n{style_o}\n{func()}{style_c}\n{text}\n{defs_c}"
    return wrapped


@svg
@defs
def style():
    result = []
    color = get_color()
    i = 1
    for value in fonts:
        result.append(
            f'.fnt{i} {{font-family: "{value}"; fill: {next(color)}; fill-opacity: 0.12;}}\n')
        i += 1
    return ''.join(result)


if __name__ == "__main__":
    main()
