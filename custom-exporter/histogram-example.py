import time
import random

from prometheus_client import Histogram, start_http_server



# Create a histogram metric
request_duration_histogram = Histogram('request_duration_seconds', 'Duration of requests in seconds')

# Simulate a function that processes requests
def process_request():
    start_time = time.time()

    # Simulate some processing
    time.sleep(random.uniform(0.1, 0.5))  # Simulate variable processing time

    # Record the duration in the histogram
    request_duration_histogram.observe(time.time() - start_time)

# Expose metrics
if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)

    # Simulate requests and update metrics
    while True:
        process_request()
