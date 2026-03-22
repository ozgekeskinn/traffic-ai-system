def riskAnalyzer(traffic,time):
    riskLevel =  ""
    traffic = float(traffic)
    if traffic < 60:
        riskLevel = "LOW TRAFFIC RISK"
    elif traffic < 110:
        riskLevel  = "NORMAL TRAFFIC RISK"
    elif traffic < 150:
        riskLevel = "HIGH TRAFFIC RISK"
    else:
        riskLevel = "HEAVY TRAFFIC RISK"
    
    return f"{time} -> {riskLevel}"