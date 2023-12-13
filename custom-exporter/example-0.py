import time
import random

import prometheus_client as prom
from prometheus_client import start_http_server, Gauge


# Unregister default collectors
prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
prom.REGISTRY.unregister(prom.GC_COLLECTOR)


# Create prometheus metrics
total_request = Gauge('total_requests', 'Total number of requests')
error_counts = Gauge('error_counts', 'Number of error')

# Simulate a function to processes requests
def process_request():
    time.sleep(0.1)

    if random.random() < 0.1:
        error_counts.inc()
    
    total_request.inc()

# Expose metrics
if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)

    # Simulate requests and update metrics
    while True:
        process_request()
    
