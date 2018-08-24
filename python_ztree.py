def dict_format(old, new=[]):
    """

    :param old: 从MongoDB取到的json数据
    :param new:
    :return: {"name": "your_name", "children": new} 返回ztree标准格式
    """
    if isinstance(old, dict):
        for i, (key, value) in enumerate(old.items()):
            new.append({"name": key, "children": []})
            if isinstance(value, dict):
                dict_format(value, new[i]["children"])
            elif isinstance(value, list):
                newdict = dict(zip(range(len(value)), value))
                dict_format(newdict, new[i]["children"])
            else:
                new[i]["children"].append({"name": value})
    return {"name": "your_name", "children": new}
