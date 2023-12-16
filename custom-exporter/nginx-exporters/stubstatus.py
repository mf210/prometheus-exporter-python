from prometheus_client import start_http_server, Gauge
import requests
import time

# NGINX stub_status URL
NGINX_STATUS_URL = 'http://nginx:8080/nginx_status'

# Prometheus metrics
active_connections = Gauge('nginx_active_connections', 'Number of active connections')
accepted_connections = Gauge('nginx_accepted_connections', 'Total number of accepted connections')
handled_connections = Gauge('nginx_handled_connections', 'Total number of handled connections')
total_requests = Gauge('nginx_total_requests', 'Total number of requests')
reading_connections = Gauge('nginx_reading_connections', 'Number of connections in reading state')
writing_connections = Gauge('nginx_writing_connections', 'Number of connections in writing state')
waiting_connections = Gauge('nginx_waiting_connections', 'Number of connections in waiting state')

def collect_metrics():
    try:
        # Fetch NGINX stub_status page
        response = requests.get(NGINX_STATUS_URL)
        data = response.text.split('\n')
        # data = ['Active connections: 3 ', 'server accepts handled requests', ' 4 4 3 ', 'Reading: 0 Writing: 1 Waiting: 2 ', '']

        # Extract values from stub_status
        active_connections.set(int(data[0].split()[-1]))
        accepted_connections.set(int(data[2].split()[0]))
        handled_connections.set(int(data[2].split()[1]))
        total_requests.set(int(data[2].split()[2]))
        reading_connections.set(int(data[3].split()[1]))
        writing_connections.set(int(data[3].split()[3]))
        waiting_connections.set(int(data[3].split()[5]))
    except Exception as e:
        print(f"Error fetching or parsing NGINX status: {e}")

if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)

    # Periodically collect metrics from NGINX stub_status
    while True:
        collect_metrics()

        # Collect every 10 seconds (adjust as needed)
        time.sleep(10)
