json_data = []


def getParametrFromPath(path, dict):
    path = path.split("/")
    output = dict
    for path_item in path:
        try:
            output = output[path_item]
        except:
            output = "N/A"
            pass
    return str(output)