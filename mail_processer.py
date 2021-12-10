from abc import ABC, abstractmethod
from jinja2 import Template
 
class EmailProcesser(ABC):
    @abstractmethod
    def send_email(cls, email_template: dict, customer: dict):
        pass

class JsonEmailProcesser(EmailProcesser):
    output_reader: any
    
    @classmethod
    def send_email(cls, email_template: str, customer: dict):
        jinja2_template = Template(email_template)
        output_template = jinja2_template.render(**customer)
        cls.output_reader.write(output_template)
    
class SMTPEmailProcesser(EmailProcesser):

    @classmethod
    def send_email(cls, email_template: dict, customer: dict):
        raise NotImplementedError
    
class RestAPIEmailProcesser(EmailProcesser):

    @classmethod
    def send_email(cls, email_template: dict, customer: dict):
        raise NotImplementedError
    

