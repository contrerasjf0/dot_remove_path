import copy

from dot_path_remove.utills import get_parts_from_list_format, is_list_format


def remove_spot(source: dict, spot: str) -> dict:
    is_spot_list = is_list_format(spot)

    if not is_spot_list and spot in source:
        source.pop(spot)
    else:
        list_parts = get_parts_from_list_format(spot)
        list_spot = list_parts.get('spot')
        list_index = list_parts.get('index')

        if list_index == 'all':
            source.pop(list_spot)
        else:
            list_index = int(list_index)
            if list_spot in source and isinstance(source[list_spot], list):
                source[list_spot].pop(list_index)

    return source


def remove_path_dot(source: dict, paths: str) -> dict:
    if not isinstance(source, dict):
        raise TypeError("source must be dict")

    if paths == '':
        return source

    source_copy = copy.deepcopy(source)
    path_spots = paths.split('.')
    source_aux = source_copy

    for i, spot in enumerate(path_spots):

        if i == len(path_spots) - 1:
            remove_spot(source_aux, spot)
        else:
            is_spot_list = is_list_format(spot)

            if is_spot_list:
                list_spot_parts = get_parts_from_list_format(spot)
                list_spot = list_spot_parts.get('spot')
                list_index = list_spot_parts.get('index')

                if list_index == 'all':
                    source_aux = source_aux[list_spot]
                else:
                    list_index = int(list_index)
                    if list_spot in source_aux and isinstance(source_aux[list_spot], list):
                        source_aux = source_aux[list_spot][list_index]

            else:
                if spot in source_aux:
                    source_aux = source_aux[spot]

    return source_copy
