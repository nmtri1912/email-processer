from os import path
import pytest
from unittest.mock import patch
from mail_protocol import MailProtocolFactory
from mail_processer import JsonEmailProcesser
from data_processer import JsonDataProcesser

@pytest.fixture
def prepare_data():
	return [
        "Mrs,Michelle,Smith,michelle.smith@examle.com",
    {
        "from": "The Marketing Team<marketing@example.com",
        "subject": "A new product is being lauched soon",
        "mimeType": "text/plan",
        "body": "Hi {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}},\nToday, {{TODAY}}, we would like to tell you that... Sincerely, \nThe Marketing Team"
    }]

@patch.object(JsonEmailProcesser, 'send_email', autospec=True)
def test_process_send_mail(mock_send_mail, prepare_data):
    mail_protocol = MailProtocolFactory.get_factory('json')
    mail_protocol.output_path = "output_emails.json"
    mail_protocol.send_mail(prepare_data[0], prepare_data[1])

    mock_send_mail.assert_called_once()

@patch.object(JsonDataProcesser, 'process_data', autospec=True)
def test_process_data(mock_process_data, prepare_data):
    mail_protocol = MailProtocolFactory.get_factory('json')
    mail_protocol.output_path = "output_emails.json"
    mail_protocol.send_mail(prepare_data[0], prepare_data[1])

    mock_process_data.assert_called_once()