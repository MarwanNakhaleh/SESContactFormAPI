import boto3
import os
import pytest

from moto import mock_ses


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"

@pytest.fixture
def ses_client(aws_credentials):
    with mock_ses():
        conn = boto3.client("ses", region_name="us-east-1")
        conn.verify_email_identity(EmailAddress="mnakhaleh@gmail.com")
        yield conn
        