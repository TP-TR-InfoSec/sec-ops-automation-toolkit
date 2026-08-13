# SecOps Automation Toolkit 🛡️

![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge&logo=github-actions)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Security Scanned](https://img.shields.io/badge/security-trufflehog%20passed-blueviolet?style=for-the-badge)

A curated collection of lightweight automation scripts, log parsers, and threat intelligence helpers designed for daily Security Operations Center (SOC) and DevSecOps tasks.

## 🚀 Modules

### 1. Log Analysis (`/log_analysis`)
Utility scripts to quickly identify anomalies, brute-force attempts, and high-frequency requesters from Web Server logs (Nginx, Apache).

### 2. Threat Intel Quick-Check (`/threat_intel`)
CLI tools to query public IP/Domain reputation APIs (VirusTotal, AbuseIPDB) directly from the terminal during incident triage.

### 3. DevSecOps Hooks (`/ci_cd_hooks`)
Pre-commit bash scripts to prevent accidental commits of high-entropy strings and credentials into internal codebases.

## 🛠️ Quick Start

```bash
# Clone the repository
git clone [https://github.com/TP-TR-InfoSec/sec-ops-automation-toolkit.git](https://github.com/TP-TR-InfoSec/sec-ops-automation-toolkit.git)

# Navigate to desired module
cd sec-ops-automation-toolkit/threat_intel

# Run IP reputation check
python check_ip_reputation.py 8.8.8.8
