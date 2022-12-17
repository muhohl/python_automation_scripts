'''
Python script that transforms the '@...' markdown style citation into an org-roam node link,
if that node exists in your org-roam database.
If the node doesn't exist the markdown node is maintained

! Input .org file will be overwritten by the output. !

Workflow:
    1. Create org file from quarto .qmd notebook
    2. copy .org into notes directory
    3. cd terminal into notes directory
    4. run cite_key.py and enter .org file name when prompted
    5. Create seperate org-roam file with name of the paper
    6. Copy content from .org file created by python script into org-roam file in step 5

Once the node file is created I can just rerun the python script on that file, and new
citation links will be inserted.
'''

import os
import re

# read file
# Make this line interactive
print("Enter .org file")
file_name = input()
file1 = open(file_name, "r")

# load all my notes file names.
# path = "~/Dropbox/Zettelkasten/notes/"
path = os.getcwd()
path = path+"/"
dir_list = os.listdir(path)

# transforms file into str object.
textfile = file1.read()

# finds all citations in the manuscrip.
matches = re.findall("@\w+", textfile)

# remove @ for matching with lit notes file names.
for i in range(len(matches)):
    matches[i] = matches[i].replace("@", "")

# replaces citation with id from the lit notes.
for i in range(len(matches)):
    for j in range(len(dir_list)):
        if matches[i] in dir_list[j]:
            roam_path = path+dir_list[j]
            roam = open(roam_path)
            textroam = roam.read()
            splitroam = textroam.split()
            author = "@"+matches[i]
            for k in range(len(splitroam)):
                if splitroam[k] == ":ID:":
                    id_link = splitroam[k+1]
            id_link = "[[id:"+id_link+"]["+matches[i]+"]]"
            textfile = textfile.replace(author, str(id_link))

# remove cite key otherwise link for doesn't work if it includes
# citation that doesn't exist as a note yet.
textfile = textfile.replace("cite:", "")

# Save file as new org file
# Look at write and read option. Ideally I create the
# org-roam file first and add the textfile data after the
# header information, with 'w' option this might already
# work
# Prompt used for name of output file
new = open(file_name, "w")
new.write(textfile)
