from django.http import HttpResponse
from django.test import TestCase
import pytest
from django.core import serializers
# from project5 import logging_module
# from project5.woe.models import Source, Observation

# from project5.scripts.api_functions import retrieve_urls

@pytest.fixture
def database():
    # data = serializers.serialize('json', Source.objects.all()[-1])
    # print(data)
    return "hello"


def test_what(database):
    assert database == "hello2"


def test_api_to_db():
    """Test that json data from api source, is correctly recorded in database."""
    assert 1 == 0


def test_migration():
    """Test that the deduplicated json in data folder matches the serialized database following a migration."""
    assert 2 == 1


def test_filter_wmo():
    """Test that selecting a wmo on webpage correctly results in filtered data."""
    assert 3 == 2
