def calculate_risk_score(data):
    score = 0
    
    # Open ports risk: Each open port adds 2 points
    score += len(data.get("open_ports", [])) * 2
    
    # Check for Strict-Transport-Security (HSTS) header absence
    if not data.get("headers", {}).get("Strict-Transport-Security"):
        score += 15
    
    # Check if SSL certificate is expired
    if data.get("ssl_info", {}).get("expired", False):
        score += 20
    
    # Return score, ensuring it's capped at 100
    return min(score, 100)
