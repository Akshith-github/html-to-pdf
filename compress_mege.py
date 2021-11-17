# code to extract all zip files in this folder
# and select all pdf files and merge them into one pdf file
import os
import zipfile
import glob
import PyPDF2

# define the path to the folder
path = 'C:/Users/akshi/Desktop/temp/zips/'
# list all zip folders in the path
zip_folders = glob.glob(os.path.join(path, '*.zip'))

# loop through all zip folders
for k,zip_folder in enumerate(zip_folders):
    print(zip_folder)
    # extract all zip files in the zip folder
    zip_ref = zipfile.ZipFile(zip_folder, 'r')
    zip_ref.extractall(path)
    zip_ref.close()

# list all pdf files in the zip folder
pdf_files = glob.glob(os.path.join(path, '*.pdf'))
# create a pdf writer object
pdf_writer = PyPDF2.PdfFileWriter()
# loop through all pdf files
for pdf_file in pdf_files:
    if "all_pdfs" in pdf_file:
        continue
    # open the pdf file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    # loop through all pages in the pdf file
    for page_num in range(pdf_reader.numPages):
        # add each page to the pdf writer object
        pdf_writer.addPage(pdf_reader.getPage(page_num))

# save the pdf file
with open('all_pdfs.pdf', 'wb') as f:
    pdf_writer.write(f)

# remove all pdf files in the zip folder
for pdf_file in pdf_files:
    if "all_pdfs" not in pdf_file:
        os.remove(pdf_file)

# remove the zip folder
# os.remove(zip_folder)
    
# remove all zip files in the path
# zip_files = glob.glob(os.path.join(path, '*.zip'))
# for zip_file in zip_files:
#     os.remove(zip_file)

