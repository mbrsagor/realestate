def validation_category_data(attrs):
    if "name" in attrs and len(attrs.get("name")) < 1:
        return "name field is required"
    else:
        return "Please provide valid options"
