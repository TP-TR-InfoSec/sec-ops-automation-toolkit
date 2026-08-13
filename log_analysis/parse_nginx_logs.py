import re
import sys
from collections import Counter

# Standard Nginx combined log format regex
LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'

def analyze_logs(log_file):
    print(f"[*] Parsing web server logs: {log_file}")
    ip_counter = Counter()
    status_counter = Counter()

    try:
        with open(log_file, 'r') as f:
            for line in f:
                match = re.match(LOG_PATTERN, line)
                if match:
                    ip, _, request, status, _ = match.groups()
                    ip_counter[ip] += 1
                    status_counter[status] += 1
    except FileNotFoundError:
        print(f"[!] File not found. Running demo mode with sample data...")
        ip_counter = Counter({"192.168.1.50": 142, "10.0.0.12": 89, "172.16.0.4": 34})
        status_counter = Counter({"200": 210, "404": 45, "500": 10})

    print("\n[+] Top Requesting IPs:")
    for ip, count in ip_counter.most_common(5):
        print(f"    - {ip}: {count} requests")

    print("\n[+] HTTP Status Code Summary:")
    for status, count in status_counter.items():
        print(f"    - Status {status}: {count} times")

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "access.log"
    analyze_logs(target_file)
