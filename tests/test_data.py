import pytest
from data_processer import JsonDataProcesser
from data_processer import JsonDataProcesser
from mail_helper import EmailHelper
from freezegun import freeze_time

@pytest.fixture
def expected_data():
	return [{
        'TITLE': 'Mrs',
        'FIRST_NAME': 'Michelle',
        'LAST_NAME': 'Smith',
        'TO': 'michelle.smith@examle.com',
        'TODAY': '16 Nov 2021'
    },
    {
        "from": "The Marketing Team<marketing@example.com",
        "to": "{{TO}}",
        "subject": "A new product is being lauched soon",
        "mimeType": "text/plan",
        "body": "Hi {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}},\nToday, {{TODAY}}, we would like to tell you that... Sincerely, \nThe Marketing Team"
    }]

@freeze_time("2021-11-16")
def test_json_parse_customer_data(expected_data):
    customer_data = "Mrs,Michelle,Smith,michelle.smith@examle.com"
    customer = JsonDataProcesser.process_data(customer_data)
    assert(customer == expected_data[0])

@pytest.mark.parametrize("input, output",[("Mrs,Michelle,Smith,michelle.smith@examle.com", False),("Mrs,Michelle,Smith",True),("Mrs,Michelle,Smith,",True)])
def test_process_error_customer(input, output):
    assert EmailHelper.is_error_customer(input) == output

def test_prepare_mail_template(expected_data):
    mail_template = {
        "from": "The Marketing Team<marketing@example.com",
        "subject": "A new product is being lauched soon",
        "mimeType": "text/plan",
        "body": "Hi {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}},\nToday, {{TODAY}}, we would like to tell you that... Sincerely, \nThe Marketing Team"
    }
    template = EmailHelper.prepare_final_email_template(mail_template)
    assert(template == expected_data[1])
