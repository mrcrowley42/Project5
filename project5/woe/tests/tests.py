import pytest
import json
# from django.http import HttpResponse
# from django.test import TestCase
# from django.core import serializers
# from project5.logging_module import logging_script
from project5.woe.models import Source, Observation
# from project5.scripts.api_functions import retrieve_urls


@pytest.fixture
def database():
    # data = serializers.serialize('json', Source.objects.all()[-1])
    # print(data)
    return "hello"


def test_what(database):
    assert database == "hello2"


def test_api_to_db():
    """Test that json data is correctly recorded in database."""
    with open('tests/data/dummy.json') as fh:
        data = json.load(fh)
    api_data = [line for line in data['observations']['data']][0]
    assert 1 == api_data


def test_filter_wmo():
    """Test that selecting a wmo on webpage correctly results in filtered data."""
    assert 3 == 2
