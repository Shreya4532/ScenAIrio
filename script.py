import csv
from datetime import datetime, timedelta
import random

# Sample data
source_ips = [
    "192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.15",
    "192.168.1.20", "192.168.1.22", "192.168.1.25", "192.168.1.30",
    "192.168.1.33", "192.168.1.35", "192.168.1.40", "192.168.1.45",
    "192.168.1.50", "192.168.1.51", "192.168.1.52", "192.168.1.55",
    "192.168.1.60", "192.168.1.62", "192.168.1.70", "192.168.1.75",
    "192.168.1.80", "192.168.1.85"
]
destination_ip = "172.16.0.5"
request_types = ["GET", "POST"]
status_codes = [200, 401, 403, 404, 500]
user_agents = ["Mozilla/5.0", "Chrome/58.0", "Safari/537.36"]

# Anomalies and attacks
anomalies = [
    ("Multiple requests per second from the same IP", "DDoS Attack"),
    ("High volume of POST requests", "DDoS Attack"),
    ("Malformed SQL query in the request", "SQL Injection"),
    ("SQL keywords detected in URL", "SQL Injection"),
    ("Multiple failed login attempts", "Brute Force Attack"),
    ("Unusual number of authentication failures", "Brute Force Attack"),
    ("Presence of OR 1=1 in query", "SQL Injection"),
    ("Suspected flooding attack", "DDoS Attack"),
    ("Accessing non-existent pages", None),
    ("Repeated login attempts with different usernames", "Brute Force Attack"),
    ("SQL syntax error in request", "SQL Injection")
]

# Create a CSV file to store the data
filename = "network_log_dataset.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Source IP", "Destination IP", "Request Type", "Status Code",
                     "Bytes Transferred", "User Agent", "Anomaly Detected", "Attack Type"])

    # Initialize the timestamp
    timestamp = datetime(2024, 8, 31, 10, 15, 0)

    # Generate 4000 rows with anomalies
    for _ in range(2500):
        source_ip = random.choice(source_ips)
        request_type = random.choice(request_types)
        status_code = random.choice(status_codes)
        bytes_transferred = random.randint(512, 4096)
        user_agent = random.choice(user_agents)

        # Choose an anomaly
        anomaly, attack_type = random.choice(anomalies)

        # Write the row to the CSV file
        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            source_ip,
            destination_ip,
            request_type,
            status_code,
            bytes_transferred,
            user_agent,
            anomaly,
            attack_type
        ])

        # Increment the timestamp by a random number of seconds
        timestamp += timedelta(seconds=random.randint(5, 15))

    # Generate 1000 rows without anomalies
    for _ in range(2500):
        source_ip = random.choice(source_ips)
        request_type = random.choice(request_types)
        status_code = random.choice(status_codes)
        bytes_transferred = random.randint(512, 4096)
        user_agent = random.choice(user_agents)

        # No anomaly for these rows
        anomaly, attack_type = None, None

        # Write the row to the CSV file
        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            source_ip,
            destination_ip,
            request_type,
            status_code,
            bytes_transferred,
            user_agent,
            anomaly,
            attack_type
        ])

        # Increment the timestamp by a random number of seconds
        timestamp += timedelta(seconds=random.randint(5, 15))

print(f"5000 rows of network log data have been generated and saved in '{filename}'.")
