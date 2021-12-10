FROM python:3.9

RUN pip3 install --no-cache-dir jinja2
RUN pip3 install --no-cache-dir pytest
RUN pip3 install --no-cache-dir freezegun

