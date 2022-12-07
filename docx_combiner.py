from docxcompose.composer import Composer
from docx import Document as Document_compose
import os

def combine_all_docx(docx_list, directory, docx_combined, date):
    number_of_sections=len(docx_list)
    master = Document_compose(directory + "/" + docx_list[0])
    composer = Composer(master)
    for i in range(1, number_of_sections):
        doc_temp = Document_compose(directory + "/" + docx_list[i])
        composer.append(doc_temp)
    composer.save("." + "/" + date + "/" + docx_combined + ".docx")

directory_list = []

date = str(input("Date of analysis:"))

for name in os.listdir("." + "/" + date):
    if os.path.isdir(os.path.join("." + "/" + date, name)):
            directory_list.append(name)

for sample in directory_list:
    docx_list = []
    directory = "." + "/" + date + "/" + sample
    for docx_name in os.listdir(directory):
        if docx_name.endswith(".docx"):
            docx_list.append(docx_name)
    combine_all_docx(docx_list, directory, sample, date)



