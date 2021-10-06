import re


def is_list_format(spot: str) -> bool:
    pattern = r'^.*\[\d*\]$'
    m = re.match(pattern, spot)

    return m != None


def get_parts_from_list_format(spot: str) -> dict:
    pattern = r'^(?P<spot>.+)\[(?P<index>\d+)\]$'
    m = re.match(pattern, spot)

    parts = {}

    if m != None:
        parts = m.groupdict()
    else:
        raise ValueError('spot is not valid as list')

    return parts
