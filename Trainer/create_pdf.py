import img2pdf
import os
import argparse

def convert_images_to_pdf(directory, output_file):
    images = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".jpg"):
            images.append(os.path.join(directory, filename))
    with open(output_file,"wb") as f:
        f.write(img2pdf.convert(images))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert jpg images in a directory to a single pdf file.')
    parser.add_argument('directory', type=str, help='The directory containing jpg images.')
    parser.add_argument('output_file', type=str, help='The output pdf file name.')

    args = parser.parse_args()

    convert_images_to_pdf(args.directory, args.output_file)
