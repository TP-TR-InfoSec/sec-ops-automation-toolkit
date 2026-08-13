#!/bin/bash
# Pre-commit hook for detecting potential hardcoded credentials

echo "[*] Running DevSecOps Pre-commit Secret Scanner..."

# Common high-entropy secret keywords
PATTERNS="api_key|secret_key|private_key|aws_secret|token|password"

# Scan staged git files
STAGED_FILES=$(git diff --cached --name-only)

if [ -z "$STAGED_FILES" ]; then
    echo "[+] No staged files to scan."
    exit 0
fi

SECRETS_FOUND=0

for file in $STAGED_FILES; do
    if git diff --cached "$file" | grep -E -i "$PATTERNS" > /dev/null; then
        echo "[!] WARNING: Potential sensitive keyword found in: $file"
        SECRETS_FOUND=1
    fi
done

if [ $SECRETS_FOUND -eq 1 ]; then
    echo "[!] Commit blocked. Please verify no credentials are hardcoded."
    exit 1
else
    echo "[+] Secret scan passed successfully. Safe to commit."
    exit 0
fi
