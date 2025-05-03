
# validates listing submitted to database
def validate_listing(data):
    try:
        if not(0 < len(data["title"]) < 100):
            return False, "Invalid title: between 1 and 100 characters"
        if len(data["description"]) > 1000:
            return False, "Invalid description length"
        if float(data["rent"]) < 0:
            return False, "Invalid input for Rent"
        if len(data["address"]) > 200:
            return False, "Invalid address length"
        if int(data["rooms"]) < 1:
            return False, "Invalid room amount"
        if len(data["contact_info"]) > 250:
            return False, "Invalid contact info length"
        
        return True, ""
    except Exception as e:
        return False, f"validation error: {str(e)}"