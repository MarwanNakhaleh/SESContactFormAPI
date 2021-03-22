import pytest
from SESClient import SESClient

@pytest.fixture
def ses_test(ses_client):
    yield

def test_send_email(ses_client, ses_test):
    my_client = SESClient()
    response = my_client.send_the_email("mnakhaleh@gmail.com", "utf-8", "Body", "mnakhaleh@gmail.com", "Subject")
    assert response["MessageId"] != None
    