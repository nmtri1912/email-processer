from abc import ABC, abstractmethod
from mail_processer import *
from data_processer import *

class EmailFactory:
    @classmethod
    def get_factory(cls, type):
        if type == 'json':
            return JsonEmailFactory
        else:
            raise NotImplementedError

class EmailAbtractFactory(ABC):
    @abstractmethod
    def get_email_processer(cls):
        pass

    @abstractmethod
    def get_data_processer(cls):
        pass

class JsonEmailFactory(EmailAbtractFactory):

    @classmethod
    def get_email_processer(cls):
        return JsonEmailProcesser

    @classmethod
    def get_data_processer(cls):
        return JsonDataProcesser

class SMTPEmailFactory(EmailAbtractFactory):
    
    @classmethod
    def get_email_processer(cls):
        return SMTPEmailProcesser

    @classmethod
    def get_data_processer(cls):
        return SMTPDataProcesser
