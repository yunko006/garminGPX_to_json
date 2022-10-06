from src.tcx.tcx_to_json import *


def test_create_nested_dict():
    nested_dict = create_nested_dict('a', 'b', 'c')
    test = {'a': {}, 'b': {}, 'c': {}}
    assert nested_dict == test