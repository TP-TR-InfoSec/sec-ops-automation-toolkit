# Threat Intelligence Feed Aggregator 🛰️

![Feed Status](https://img.shields.io/badge/threat__feed-active-brightgreen?style=for-the-badge)
![Cron Sync](https://img.shields.io/badge/sync-daily%2002:00%20UTC-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Security Scanned](https://img.shields.io/badge/security-trufflehog%20passed-blueviolet?style=for-the-badge)

Automated OSINT threat intelligence collection tool that fetches, deduplicates, and formats public IOC (Indicators of Compromise) feeds for Firewall, Nginx, and SIEM ingestion.

## 📌 Features

- **Daily Auto-Sync:** Automated GitHub Actions cron job running daily feed aggregation at 02:00 UTC.
- **Multi-Source OSINT:** Aggregates indicators from public sources (Feodo Tracker, URLhaus, AbuseIPDB).
- **SIEM & Firewall Ready:** Formats raw outputs into clean blocklists compatible with Palo Alto, Fortinet, and Nginx.

## 📁 Repository Structure

```text
threat-intelligence-feed-aggregator/
├── .github/workflows/   # Daily automated sync action
├── collectors/          # Python scripts querying OSINT APIs
└── feeds/               # Formatted blocklists (IPs, Hashes, Domains)

## 🛠️ Usage
To manually trigger the feed collector and update local blocklists:
# Clone repository
git clone [https://github.com/TP-TR-InfoSec/threat-intelligence-feed-aggregator.git](https://github.com/TP-TR-InfoSec/threat-intelligence-feed-aggregator.git)

# Run collector script
python collectors/fetch_public_feeds.py
