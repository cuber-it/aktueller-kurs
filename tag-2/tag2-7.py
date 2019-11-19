import sys
import re
import argparse

def read_data(file_name):
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
    return data

def write_data(file_name, data):
    with open(file_name, "w") as f:
      f.write("\n".join(data))

def print_data(data):
    for k, v in data.items():
        print("{} -> {}".format(k, v))

def extract_nutzdaten(data):
    result = {}
    im_interface = False
    interface_name = ""
    for zeile in data:
        zeile = zeile.strip("\n")
        if zeile.startswith("interface"):
            im_interface = True
            interface_name = zeile.replace("interface ", "")
            result[interface_name] = {}
        elif zeile.startswith("!"):
            im_interface = False
        elif im_interface == True:
            if "ipv4" in zeile:
                zeile = zeile.split()
                result[interface_name]["ipv4"] = [zeile[-2], zeile[-1]]
    return result


if __name__ == "__main__":
    roh_daten = read_data(r"D:\Kurse\python\b-germ-rt-dc-7.txt")
    nutz_daten = extract_nutzdaten(roh_daten)
    print_data(nutz_daten)