def svg(*items):
    """ Відкриваємо та закриваємо тіло svg файлу
        та заповнюємо нутрощі елементами.
    """
    ret = '<svg>'
    for i in items:
        ret += i
    return ret + '</svg>'


def rect(x, y, w, h, fill):
    """ Вставляємо значення зі змінних у прямокутник.
    """
    return '<rect x="{}" y="{}" width="{}" height="{}" fill="{}"/>'.format(x, y,
                                                                           w, h,
                                                                           fill)


def circ(x, y, r, fill='black'):
    """ Вставляємо значення зі змінних у коло.
    """
    return '<circle cx="{}" cy="{}" r="{}" fill="{}"/>'.format(x, y, r, fill)


def group(*items, fill='', stroke='', transform=''):
    ret = '<g fill="{}" stroke="{}" transform="{}">'
    for i in items:
        ret += i
    ret += '</g>'
    return ret.format(fill, stroke, transform)


svg(group(circ(120, 120, 40, 'red'),
          rect(80, 80, 25, 60, 'green'),
          fill='black',
          transform='rotate(30)'))

# => '<svg><g fill="black" stroke="" transform="rotate(30)"><circle cx="120" cy="120" r="40" fill="red"/><rect x="80" y="80" width="25" height="60" fill="green"/></g></svg>'
