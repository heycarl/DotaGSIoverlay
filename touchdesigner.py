json_data = transfer.json_data

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


while True:
    print(json_data)

#print(getParametrFromPath("hero/team3/player5", json_data))

