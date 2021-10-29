from bs4 import BeautifulSoup
import shutil
import os

## Parses a mission's name from source html
with open('***.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    with open("countryname.txt", "w", encoding='utf-8') as file:
        file.write(str(soup.find_all("h4", class_="text-primary")))

## Filter's it for HTML junk

infile = "countryname.txt"
outfile = "nation.txt"

delete_list = ['<p>', '</p>', '<strong>', '</strong>', '[<p  class ="h6">', '<p class="h6">','[', ']', ',', '<h4 class="text-primary">', '</h4>']
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
       line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

# Parses a list of accredited diplomats

with open('***.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')
   
    with open("output1.txt", "a", encoding='utf-8') as file:
        file.write(str(soup.find_all("p", class_="h6")))

# Deletes the undersired first line.

with open(r"output1.txt", 'r+') as fp:
    lines = fp.readlines()
    fp.seek(0)
    fp.truncate()
    fp.writelines(lines[1:])



# Filters output1.txt for useless html contet
infile = "output1.txt"
outfile = "cleaned_file.txt"

delete_list = ['<p>', '</p>', '<strong>', '</strong>', '[<p  class ="h6">', '<p class="h6">','[', ']', ',']
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
       line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

# Appends the list of diplomats to the mission name
with open('***.txt','wb') as wfd:
    for f in ['nation.txt','cleaned_file.txt']:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd, wfd.write(b"\n"))


## Clears the file mess
if os.path.exists("nation.txt"):
    os.remove("nation.txt")

if os.path.exists("cleaned_file.txt"):
    os.remove("cleaned_file.txt")

if os.path.exists("output1.txt"):
    os.remove("output1.txt")

if os.path.exists("countryname.txt"):
    os.remove("countryname.txt")
