import os

def fsize(root):
    result = 0
    for dirName, subdirList, fileList in os.walk(root):
        for fname in fileList:
            try:
                result += os.path.getsize(
                    os.path.join(
                        dirName,
                        fname))
            except BaseException as err:
                print("{}".format(err.msg))
    return result

print("{}".format(fsize(r"d:/") / 1024))