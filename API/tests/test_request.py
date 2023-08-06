import pytest
from ApiApp.models import Requests

@pytest.fixture()
def request_creation():
    return Requests.objects.create(
        date='2023-08-06',
        method='PUT',
        consult='https://jsonplaceholder.typicode.com/users',
        dataReturn='[{"id":1, "name":"Leanne Graham"}]'
    )

@pytest.mark.django_db
def test_request_creation_date(request_creation):
    assert request_creation.date == '2023-08-06'

@pytest.mark.django_db
def test_request_creation_method(request_creation):
    assert request_creation.method == 'PUT'

@pytest.mark.django_db
def test_request_creation_consult(request_creation):
    assert request_creation.consult == 'https://jsonplaceholder.typicode.com/users'

@pytest.mark.django_db
def test_request_creation_dataReturn(request_creation):
    assert request_creation.dataReturn == '[{"id":1, "name":"Leanne Graham"}]'


@pytest.mark.django_db
def test_request_creation_fail():
    with pytest.raises(Exception):
        Requests.objects.create(
            method='PUT',
            dataReturn='[{"id":1, "name":"Leanne Graham"}]'
        )




