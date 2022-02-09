def quantity_keys(data: dict, list):
    keys_list = data.keys()
    excede_keys = [key for key in keys_list if key not in list]

    if len(keys_list) > 4:
        for key in excede_keys:
            del data[key]
    
    return data