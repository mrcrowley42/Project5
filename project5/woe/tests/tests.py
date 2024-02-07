from django.http import HttpResponse
from django.test import TestCase
import pytest
from django.core import serializers
# from project5.woe.models import Source, Observation


@pytest.fixture
def database():
    # data = serializers.serialize('json', Source.objects.all())
    # return HttpResponse(data, content_type='application/json')
    return "hello"


def test_what(database):
    assert database == "hello"
