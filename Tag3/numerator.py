def numerate(filename, start=1):
    with open(filename) as fd:
        text = []
        for znr, zeile in enumerate(fd.readlines(), start):
            text.append(f"{znr}:{zeile}")
    return text

if __name__ == '__main__':
    import sys
    fname = sys.argv[1]

    text = numerate(fname)
    for zeile in text:
        print(zeile, end = '')