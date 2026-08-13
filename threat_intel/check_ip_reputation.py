import sys
import time

def check_ip_reputation(ip_address):
    print(f"[*] Querying Threat Intelligence feeds for IP: {ip_address}")
    time.sleep(1)  # Simulate API latency
    
    # Mock OSINT response
    print("[+] Checking AbuseIPDB... CLEAN (0% Confidence Score)")
    print("[+] Checking VirusTotal... 0/94 Security Vendors Flagged")
    print("[+] Checking AlienVault OTX... No Active Pulses Found")
    print(f"\n[RESULT] IP {ip_address} is considered LOW RISK.")

if __name__ == "__main__":
    ip = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    check_ip_reputation(ip)
