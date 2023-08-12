"""
Simple prometheus-client example
"""

from prometheus_client import start_http_server, Summary
import random
import time
from datetime import datetime

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
# Summary is one of the metric types supported by prometheus-client. The other ones are: Counter, Gauge, Histogram

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time.
    This emulates request processing."""
    time.sleep(t)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] - Processed request in {t} seconds")

if __name__ == '__main__':
    # Start up the server to expose the metrics in the port 8000.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.randint(1, 5))