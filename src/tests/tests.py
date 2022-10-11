# append les paths ensemble
import sys
sys.path.append('../')  
# marche dans le power shell
import pytest
from pathlib import Path

from tcx.tcx_to_json import *


@pytest.fixture()
def get_file():
    """ Return le path du fichier .tcx pour les tests."""
    path = Path('test_data.tcx')
    return path


@pytest.fixture()
def create_dict():
    """ Créé la fixture qui return un nested dict pour les tests."""
    nested_dict = create_nested_dict('Time')
    return nested_dict


def test_create_nested_dict(create_dict):
    """ Test la fonction create_nested_dict avec la fixture create_dict. """
    assert create_dict == {'Time': {}}


def test_clean_line():
    """ Test de la fonction clean_line """
    line = "        <Time>2021-11-08T15:48:52.000Z</Time>      "
    suffix = "Time"

    test_variable = clean_line(line, suffix)
    should_equal = "2021-11-08T15:48:52.000Z"
    assert test_variable == should_equal
    

def test_append_data_to_dict(get_file, create_dict):
    """ Utilise les fixtures get_file et create_dict pour tester la fonction 
    append_data_to_dict. """
    test_fct = append_data_to_dict(create_dict, get_file)
    assert test_fct == {'Time': {0: '2021-11-08T15:48:52.000Z'}}
