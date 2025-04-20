import csv
import json
import os
from datetime import datetime

from modules.recon import get_domain_info
from modules.risk_score import calculate_risk_score
from modules.ai_analysis import generate_summary
# Set input and output paths
INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.csv")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "reports.json")

def read_domains_from_csv(file_path):
    domains = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                domain = row.get("domain")
                if domain:
                    domains.append(domain.strip())
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    return domains

def save_output_to_json(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"[✔] Results saved to {file_path}")
'''
def main():
    print("🚀 Starting Attack Surface Monitoring...\n")
    domains = read_domains_from_csv(INPUT_FILE)

    if not domains:
        print("[!] No domains found. Please check your input CSV.")
        return

    reports = []

    for domain in domains:
        print(f"🔍 Scanning domain: {domain}")
        result = {
            "domain": domain,
            "scan_date": datetime.now().strftime("%Y-%m-%d"),
        }

        # Reconnaissance
        recon_data = get_domain_info(domain)
        result.update(recon_data)

        # Risk Scoring , risk_summary
        risk_score = calculate_risk_score(recon_data)

        #risk_score = calculate_risk_score(recon_data)
        result["risk_score"] = risk_score

        # AI-Based Analysis
        summary = generate_summary(recon_data)
        result["risk_summary"] = summary
        report = {
        "domain": domain,
        "recon_data": recon_data,
        "risk_score": risk_score,
        #"risk_summary": risk_summary,
        "ai_summary": summary,
    }

        reports.append(result)
        print(f"✅ Completed: {domain} | Risk Score: {risk_score}\n")

    # Save all domain reports
    save_output_to_json(reports, OUTPUT_FILE)

if __name__ == "__main__":
    main()
'''
def main():
    print("🚀 Starting Attack Surface Monitoring...\n")
    domains = read_domains_from_csv(INPUT_FILE)

    if not domains:
        print("[!] No domains found. Please check your input CSV.")
        return

    reports = []

    for domain in domains:
        print(f"🔍 Scanning domain: {domain}")
        scan_date = datetime.now().strftime("%Y-%m-%d")

        # Reconnaissance
        recon_data = get_domain_info(domain)

        # Risk Score and Summary
        risk_score = calculate_risk_score(recon_data)
        risk_summary = generate_summary(recon_data)

        # Build clean JSON structure
        report = {
            "domain": domain,
            "scan_date": scan_date,
            "risk_score": risk_score,
            "risk_summary": risk_summary,
            "subdomains": recon_data.get("subdomains", []),
            "dns_records": recon_data.get("dns_records", {}),
            "open_ports": recon_data.get("open_ports", []),
            "tech_stack": recon_data.get("tech_stack", []),
            "headers": recon_data.get("headers", {}),
            "ssl_info": recon_data.get("ssl_info", {}),
            "osint_findings": recon_data.get("osint_findings", []),
            "sensitive_paths": recon_data.get("sensitive_paths", []),
        }

        reports.append(report)
        print(f"✅ Completed: {domain} | Risk Score: {risk_score}\n")

    # Save all domain reports
    save_output_to_json(reports, OUTPUT_FILE)
    
if __name__ == "__main__":
    main()

