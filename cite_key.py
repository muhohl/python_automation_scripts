'''
Needs a little bit more testing. But I'm quiet optimistic that most of it should work.
But the current algorithm is quiet slow, with a three fold nested for loop.
'''

import os
import re

# read file
# Make this line interactive
file1 = open("test.org", "r")

# load all my notes file names.
path = "../../../../Dropbox/Zettelkasten/notes/"
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
new = open("test_lit.org", "w")
new.write(textfile)
