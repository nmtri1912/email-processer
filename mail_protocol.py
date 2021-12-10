import json
from abc import ABC, abstractmethod
from mail_helper import EmailHelper as helper

class MailProtocolFactory:
    @classmethod
    def get_factory(cls, type):
        if type == 'json':
            return JsonMailProtocol
        else:
            raise NotImplementedError

class MailProtocol(ABC):
    @abstractmethod
    def send_mail(cls):
        pass
    
class JsonMailProtocol(MailProtocol):
    email_processer, data_processer = helper.get_processer('json')
    output_reader: any
    
    @classmethod
    def send_mail(cls, customer, email_template):
        customer_data = cls.data_processer.process_data(customer)
        final_template = json.dumps(helper.prepare_final_email_template(email_template), indent=4)
        cls.email_processer.output_reader = cls.output_reader
        cls.email_processer.send_email(final_template, customer_data)

class SMTPMailProtocol(MailProtocol):

    @classmethod
    def send_mail(cls, customer, email_template):
        raise NotImplementedError
