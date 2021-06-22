def validate_position_data(attrs):
    if "name" in attrs and len(attrs.get("name")) <= 1:
        return "Name field is required"
    elif "name" in attrs and len(attrs.get("name")) >= 100:
        return "Name max length not more than 100"
    else:
        return None
