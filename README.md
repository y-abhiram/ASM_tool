# ASM_tool
**Project Title:**
Automated Attack Surface Monitoring Tool with AI-Powered Risk Analysis



this repository is for attack surface monitoring modules


**Description:**
This project involves the development of a fully automated tool that identifies and assesses the external attack surface of given domain names. By using various reconnaissance techniques, the tool collects detailed information about the domains, such as subdomains, live hosts, DNS records, ports, services, and vulnerabilities. It then generates a risk score based on the gathered data and provides a structured output, which can be integrated with centralized systems for further analysis.

The tool also includes an AI-powered component that provides enhanced risk analysis based on the detected surface data.
  
   
**Features:**

Subdomain Enumeration: Identifies subdomains of a domain using popular tools like amass and subfinder.

Live Subdomain Detection: Verifies the availability of subdomains using httpx, curl, or requests.

WHOIS & DNS Records: Fetches registrar details, nameservers, MX, SPF, DKIM, and A/AAAA records.

Port Scanning: Performs a full port scan using nmap to detect open services and their versions.

Service Fingerprinting: Identifies services and versions running on open ports.

Technology Stack Detection: Uses tools like Wappalyzer and whatweb for tech stack fingerprinting.

SSL/TLS Analysis: Detects SSL certificate expiry, weak ciphers, and supported protocols using sslyze or testssl.sh.

HTTP Header Security Audit: Checks for security headers such as HSTS, X-Frame-Options, and Content Security Policy (CSP).

Sensitive Path Discovery: Discovers sensitive directories like /admin, /backup, etc., using tools like dirsearch.

OSINT/Breach Check: Checks for leaked emails/domains via services like haveibeenpwned, hunter.io, and intelx.io.

Risk Scoring and AI Analysis: The tool generates a risk score based on the collected data and provides an AI-driven risk summary.

**Requirements:**

Python 3.7+

Required Python libraries:

requests

httpx

subfinder

amass

nmap

wappalyzer

whatweb

sslyze

testssl.sh

dirsearch

haveibeenpwned

Additional libraries depending on your environment and tools

Setup Instructions:
Clone the repository:

bash
Copy
Edit
git clone https://github.com/mycyberly/ASM_tool.git
cd ASM_tool
**Install dependencies:**

Make sure you have Python 3.7+ installed. Install the required Python libraries with:

bash
Copy
Edit
pip install -r requirements.txt
Running the Tool:

Prepare your domain list in a CSV file (e.g., input.csv) with the column domain.

Run the tool by executing the following:

bash
Copy
Edit
python asm_tool.py --input input.csv
Output:

The results will be saved in a structured JSON file with details such as subdomains, live checks, WHOIS records, ports, services, technology stack, SSL/TLS details, and security headers.

The risk score and AI-driven summary will also be included in the output.

**Input Format:**
The tool expects a CSV file with the following structure:
domain
example.com
example2.com


