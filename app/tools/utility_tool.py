from datetime import datetime

def get_current_timestamp():
    """
    Returns the current timestamp in the format YYYY-MM-DD HH:MM:SS.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_risk(score):
    """
    Calculates the risk level based on the given score.
    
    Args:
        score (float): The risk score.
        
    Returns:
        str: The risk level ('Low', 'Medium', 'High').
    """
    if score >=80:
        return "Low"
    
    elif score >= 50:
        return "Medium"
    else:
        return "High"