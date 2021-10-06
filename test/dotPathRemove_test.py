"""Dot path cases

    Source Dict

    dictionary: Dict = {
        'a': 'value a',
        'b': ['element b1', 'element b2', 'element b3'],
        'c': {
            'c1': 'Value c1',
            'c2': 'Value c2',
            'c3': ['element C3-1', 'element C3-2', 'element C3-3'],
            'c4': {
                'c4_1': 'value c4_1',
                'c4_2': ['element c4_2-1', 'element c4_2-2', 'element c4_2-3'],
            }
        },
        'd': [
            {
                'd0_1': 'value d0_1',
                'd0_2': 'value d0_2',
            },
            {
                'd1_1': 'value d1_1',
                'd1_2': 'value d1_2',
                'd1_3': ['element d1_3-1', 'element d1_3-2', 'element d1_3-3']
            },
            {
                'd2_1': 'value d2_1',
                'd2_2': 'value d2_2',
                'd2_3': ['element d2_3-1', 'element d2_3-2', 'element d2_3-3'],
                'd2_4': {
                    'd2_4_1': 'value d2_4_1',
                    'd2_4_2': 'value d2_4_2'
                }
            },
        ],
        'e': {
            'e1': 'value e1',
            'e2': [
                {
                    'e2_0_1': 'value e2_1',
                    'e2_0_2': 'value e2_2',
                },
                {
                    'e2_1_1': 'value e2_1',
                    'e2_2_2': {
                        'e2_2_2_1': 'Value e2_2_2_1',
                        'e2_2_2_2': {
                            'e2_2_2_2_1': 'Value e2_2_2_2_1'
                        }
                    },
                }
            ],
        }
    }

    Success paths:
    [*] ''
    [*] 'a'
    [*] 'b[1]'
    [] 'b[]'
    [*] 'c.c1'
    [*] 'c.c3[0]'
    [] 'c.c3[]'
    [*] 'c.c4.c4_1'
    [*] 'c.c4.c4_2[2]'
    [] 'e.e2[0].e2_0_2'
    [] 'e.e2[1].e2_2_2.e2_2_2_2.e2_2_2_2_1'
    [] 'd[0].d0_2'
    [] 'd[1].d1_3[2]'
    [] 'd[2].d2_4.d2_4_2'

    Error paths:
    [] '[1]'
    [] 'b[ty]
    
    """

import pytest
from dot_path_remove.dot_path_remove import remove_path_dot


@pytest.fixture
def source_dict():
    """Retur the Dict t hat will be used remove key"""
    dictionary = {
        'a': 'value a',
        'b': ['element b1', 'element b2', 'element b3'],
        'c': {
            'c1': 'Value c1',
            'c2': 'Value c2',
            'c3': ['element C3-1', 'element C3-2', 'element C3-3'],
            'c4': {
                'c4_1': 'value c4_1',
                'c4_2': ['element c4_2-1', 'element c4_2-2', 'element c4_2-3'],
            }
        },
        'd': [
            {
                'd0_1': 'value d0_1',
                'd0_2': 'value d0_2',
            },
            {
                'd1_1': 'value d1_1',
                'd1_2': 'value d1_2',
                'd1_3': ['element d1_3-1', 'element d1_3-2', 'element d1_3-3']
            },
            {
                'd2_1': 'value d2_1',
                'd2_2': 'value d2_2',
                'd2_3': ['element d2_3-1', 'element d2_3-2', 'element d2_3-3'],
                'd2_4': {
                    'd2_4_1': 'value d2_4_1',
                    'd2_4_2': 'value d2_4_2'
                }
            },
        ],
        'e': {
            'e1': 'value e1',
            'e2': [
                {
                    'e2_0_1': 'value e2_1',
                    'e2_0_2': 'value e2_2',
                },
                {
                    'e2_1_1': 'value e2_1',
                    'e2_2_2': {
                        'e2_2_2_1': 'Value e2_2_2_1',
                        'e2_2_2_2': {
                            'e2_2_2_2_1': 'Value e2_2_2_2_1'
                        }
                    },
                }
            ],
        }
    }
    return dictionary


def test_remove_empty_path(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, '')

    assert updated_dict == source_dict


def test_remove_simple_spot_path(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, 'a')

    source_dict.pop('a')

    assert updated_dict == source_dict


def test_remove_item_from_array_spot_path(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, 'b[1]')

    source_dict['b'].pop(1)

    assert updated_dict == source_dict


def test_remove_simple_spot_nested_level_2(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, 'c.c4.c4_2[2]')

    source_dict['c']['c4']['c4_2'].pop(2)

    assert updated_dict == source_dict


def test_remove_simple_spot_nested_level_3(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, 'c.c4.c4_1')

    source_dict['c']['c4'].pop('c4_1')

    assert updated_dict == source_dict


def test_remove_item_from_array_spot_nested_level_2(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, 'c.c3[0]')

    source_dict['c']['c3'].pop(0)

    assert updated_dict == source_dict


def test_remove_item_from_array_spot_nested_level_3(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, 'c.c3[0]')

    source_dict['c']['c3'].pop(0)

    assert updated_dict == source_dict


def test_remove_spot_nested_insite_array_nested_level_2(source_dict) -> None:
    updated_dict = remove_path_dot(source_dict, 'e.e2[0].e2_0_2')

    source_dict['e']['e2'][0].pop('e2_0_2')

    assert updated_dict == source_dict
