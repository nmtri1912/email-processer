import argparse
from mail_protocol import MailProtocolFactory
from mail_helper import EmailHelper as helper

parser = argparse.ArgumentParser(description='Process mail')
parser.add_argument('path_to_mail_template_json')
parser.add_argument('path_to_customer_csv')
parser.add_argument('path_to_output_json')
parser.add_argument('path_to_error_csv')

mail_template_path, customer_path, output_path, error_path = helper.get_path_to_resource(parser)

customer_reader = open(customer_path, 'r')
customer_title = customer_reader.readline()

error_reader = open(error_path, 'w')
error_reader.write(customer_title.rstrip("\n"))

customer = customer_reader.readline()

email_type = helper.get_email_type()
email_template = helper.get_template(mail_template_path)
output_reader = open(output_path, 'a')

if email_type == 'json':
    mail_protocol = MailProtocolFactory.get_factory('json')
    mail_protocol.output_reader = output_reader
else:
    raise NotImplementedError

while customer:
    if helper.is_error_customer(customer):
        helper.process_error_customer_data(error_reader, customer)
    else:
        mail_protocol.send_mail(customer, email_template)
    customer = customer_reader.readline()

error_reader.close()
customer_reader.close()
output_reader.close()
