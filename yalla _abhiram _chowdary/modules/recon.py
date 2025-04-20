import socket

def get_subdomains(domain):
    # Dummy implementation
    return [f"www.{domain}", f"mail.{domain}"]

def get_dns_records(domain):
    try:
        return {
            "A": socket.gethostbyname(domain),
            "MX": "mx.example.com",
            "NS": "ns1.example.com",
            "SPF": "v=spf1 include:_spf.google.com ~all"
        }
    except Exception:
        return {}

def get_open_ports(domain):
    return [80, 443]

def detect_tech_stack(domain):
    return ["Apache", "PHP", "WordPress"]

def get_http_headers(domain):
    return {
        "Strict-Transport-Security": "max-age=63072000",
        "X-Frame-Options": "SAMEORIGIN",
        "Content-Security-Policy": "default-src 'self'"
    }

def get_ssl_info(domain):
    return {
        "cert_expiry": "2025-12-31",
        "protocols": ["TLS 1.2", "TLS 1.3"],
        "weak_ciphers": []
    }

def discover_sensitive_paths(domain):
    return ["/admin", "/login", "/backup"]

def get_osint_data(domain):
    return ["Possible credential leak on GitHub", "Domain found in breach database"]

# ✅ Unified function to return all recon info
def get_domain_info(domain):
    return {
        "subdomains": get_subdomains(domain),
        "dns_records": get_dns_records(domain),
        "open_ports": get_open_ports(domain),
        "tech_stack": detect_tech_stack(domain),
        "headers": get_http_headers(domain),
        "ssl_info": get_ssl_info(domain),
        "sensitive_paths": discover_sensitive_paths(domain),
        "osint_findings": get_osint_data(domain)
    }
    
    
    

