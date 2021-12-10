from mail_helper import EmailHelper as helper
from mail_processer import JsonEmailProcesser
from data_processer import JsonDataProcesser


def test_get_email_and_data_processer():
    email_processer, data_processer = helper.get_processer('json')
    assert(type(email_processer) == type(JsonEmailProcesser))
    assert(type(data_processer) ==  type(JsonDataProcesser))
