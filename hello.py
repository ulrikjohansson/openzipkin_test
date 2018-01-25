from py_zipkin.zipkin import zipkin_span
from flask import Flask
import requests
import logging

from time import sleep




app = Flask(__name__)
app.logger.setLevel(logging.INFO)  # use the native logger of flask
app.logger.disabled = False

def http_transport(encoded_span):
    # The collector expects a thrift-encoded list of spans.
    r = requests.post(
        'http://192.168.99.100:9411/api/v1/spans',
        data=encoded_span,
        headers={'Content-Type': 'application/x-thrift'},
    )


@app.route('/')
def hello():
    with zipkin_span(
        service_name='my_service',
        span_name='my_span_name',
        transport_handler=http_transport,
        port=42,
        sample_rate=100, # Value between 0.0 and 100.0
    ) as span:
        sleep(0.05)
        with zipkin_span(
            service_name='my_service',
            span_name='call_tjo',
        ):
            sleep(0.3)
            r = requests.get('http://localhost:8000/tjo', timeout=2)

        sleep(0.1)
        return r.text

@app.route('/tjo')
def tjo():
    return "ok"

