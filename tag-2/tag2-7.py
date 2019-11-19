import sys
import argparse

def read_data(file_name):
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
    return data

def write_data(file_name, data):
    with open(file_name, "w") as f:
      f.write("\n".join(data))

def print_data(data):
    for n in data:
        print(n)

def extract_nutzdaten(daten):
    result = []

    return result


if __name__ == "__main__":
    data = read_data(r"D:\Kurse\python\b-germ-rt-dc-7.txt")
    data = extract_nutzdaten(data)
    print_data(data)