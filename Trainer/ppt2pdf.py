import os
import argparse
import comtypes.client

def convert_pptx_to_pdf(pptx_directory):
    # Initialize PowerPoint
    ppt = comtypes.client.CreateObject("PowerPoint.Application")
    ppt.Visible = 1

    # Go through each .pptx file in the directory
    for filename in os.listdir(pptx_directory):
        if filename.endswith('.pptx'):
            path_to_pptx = os.path.join(pptx_directory, filename)
            path_to_pdf = os.path.splitext(path_to_pptx)[0] + '.pdf'

            # Open the pptx file
            presentation = ppt.Presentations.Open(path_to_pptx)

            # Save as PDF (formatType = 32)
            presentation.SaveAs(path_to_pdf, 32)

            # Close the presentation
            presentation.Close()

    # Quit PowerPoint
    ppt.Quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert all .pptx files in a directory to .pdf')
    parser.add_argument('directory', type=str, help='Directory containing .pptx files')

    args = parser.parse_args()
    convert_pptx_to_pdf(args.directory)
