import json
import re
from enum import Enum
from factory import EmailFactory

class EmailType(Enum):
    json_type = 'json'
    smtp_type = 'smtp'

class EmailHelper:

    @classmethod
    def get_processer(cls, type):
        email_factory = EmailFactory.get_factory(type)
        email_processer = email_factory.get_email_processer()
        data_processer = email_factory.get_data_processer()
        return email_processer, data_processer

    @classmethod
    def process_error_customer_data(cls, reader, customer):
        reader.write('\n' + customer.rstrip("\n"))

    @classmethod
    def prepare_final_email_template(cls, email_template):
        return {
            "from": email_template['from'],
            "to": "{{TO}}",
            "subject": email_template['subject'],
            "mimeType": email_template['mimeType'],
            "body": email_template['body']
        }
    
    @classmethod
    def get_path_to_resource(cls, parser):
        args = parser.parse_args()
        return args.path_to_mail_template_json, args.path_to_customer_csv, args.path_to_output_json, args.path_to_error_csv

    @classmethod
    def get_email_type(cls):
        return EmailType.json_type.value

    @classmethod
    def get_template(cls, mail_template_path):
        with open(mail_template_path) as f:
            email_template = json.load(f)
        return email_template

    @classmethod
    def is_error_customer(cls, customer):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        customer_data = customer.split(',')
        if len(customer_data) != 4 or any(not c.rstrip("\n") for c in customer_data):
            return True
        if re.fullmatch(regex, customer[3]):
            return True
        return False
