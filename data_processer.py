from abc import ABC, abstractmethod
import datetime

class DataProcesser(ABC):
    @abstractmethod
    def process_data(cls):
        pass
    
class JsonDataProcesser(DataProcesser):

    @classmethod
    def process_data(cls, customer):
        datas = customer.split(',')
        return {
            'TITLE': datas[0],
            'FIRST_NAME': datas[1],
            'LAST_NAME': datas[2],
            'TO': datas[3].rstrip("\n"),
            'TODAY': datetime.datetime.now().strftime("%d %b %Y")
        }

class SMTPDataProcesser(DataProcesser):

    @classmethod
    def process_data(cls):
        raise NotImplementedError
