def validation_inventory_data(attrs):
    if "name" in attrs and len(attrs.get("name")) < 1:
        return "name field is required"
    elif "category_name" is None:
        return "please must have category name"
    elif "stock_from" in attrs and len(attrs.get("stock_from")):
        return "please must have stock name"
    else:
        return "Please provide valid options"
