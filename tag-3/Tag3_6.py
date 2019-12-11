import json

#with open("config.json") as fd:
#    config = json.load(fd)

def compare_object(a, b):
    if type(a) != type(b):
        return False
    elif type(a) is dict:
        return compare_dict(a, b)
    elif type(a) is list:
        return compare_list(a, b)
    else:
        return a == b


def compare_dict(a, b):
    if len(a) != len(b):
        return False
    else:
        for k, v in a.items():
            if not k in b:
                return False
            else:
                if not compare_object(v, b[k]):
                    return False
    return True


def compare_list(a, b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if not compare_object(a[i], b[i]):
                return False
    return True

config = json.load(open("config.json"))
print(config)
print(type(config))
