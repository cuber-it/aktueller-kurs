import os
import argparse

def rename_files(directory, bookname, start, dryrun):
    # List all files in the directory
    files = os.listdir(directory)

    # Filter out non-jpg files and sort the resulting list
    jpg_files = sorted([file for file in files if file.endswith(".jpg")])

    # Rename the files
    page_no = start
    for file in jpg_files:
        new_name = f"{bookname}_{page_no:03}.jpg"
        if dryrun:
            print(f"Would rename {file} to {new_name}")
        else:
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            print(f"Renamed {file} to {new_name}")
        page_no += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rename jpg files.')
    parser.add_argument('-d', '--directory', required=True, help='Directory to pick jpg files from')
    parser.add_argument('-b', '--bookname', required=True, help='Book name to use in the new filenames')
    parser.add_argument('-s', '--start', type=int, required=True, help='Starting page number')
    parser.add_argument('--dryrun', action='store_true', help='Do a dry run without renaming any files')
    args = parser.parse_args()

    rename_files(args.directory, args.bookname, args.start, args.dryrun)
