# mission-parser
A python HTML parser to mine data on foreign diplomatic missions in Australia
------------------------------------------------------------------------------------------------

INTRODUCTION

This code is a simple implementation of python’s BeautifulSoup library to mine data about   diplomatic missions in Australia. It processes a HTML input in order to parse for the desired data.

You can use it to calculate the number of accredited diplomats a given country has in Australia, its consulates, contact numbers, staff details and pretty much any other desired public information made available by the Department of Foreign Affairs and Trade (DFAT).

This has been the backbone of a project entitled “Diplomacy Down Under”, which you can check on https://diplomacydownunder.com.au

DISCLOSURE

The sole purpose of this program is to facilitate the analysis of foreign diplomatic activity in Australia. It exclusively makes use of public information disclosed by DFAT.

Any miss-use of this code is not my responsibility and entirely attributable to he/she who modified it in order to achieve any objective that is slightly divergent from its original purpose, that of generating knowledge for International Relations academics and professionals.


USAGE

DFAT’s protocol portal blocks the use of web-crawlers in order to preserve server resources and ensure a greater level of security. For this reason, you would ideally download the HTML of the diplomatic mission you wish to parse for information with wget or a similar tool from:

https://protocol.dfat.gov.au/Public/MissionsInAustralia

Once you have the HTML containing the data you wish to parse, modify the mission-parser.py input and output file settings (lines 6, 32 and 66). A guide on parsing multiple files is available further down.

To use the program, simply execute it with:

python3 mission-parser.py

Be sure to have the HTML file(s) you wish to parse in the same folder. The output will be a .txt file containing the mission’s name and its diplomats with each entry on a new line. In order to make it easy to append the output with that of other missions, there’s also line jump in the first line. 

If you wish to extract data from multiple missions, you can use the Py-multiplier.py to generate a individual python parser for each mission. For that, you first need the HTML file of each mission you wish to parse. In DFAT’s protocol portal, each mission’s page is named as number.html (e.g.: 30.html), so if you don’t change its name, your file will likely be named number.html.

After that, you need to edit the Py-multiplier in order to inform it which missions should be processed. For that, you need to modify the ListF function in Py-multipler (line 4) and add the desired mission numbers:

ListF = [X]

As an example, if you wish to parse three files, it should look something like this:

ListF = [11, 24, 38]

Again, be sure to have their respective files in the same directory (11.html, 24.html and 38.html). 

Execute the program with:

python3 Py-multiplier.py

You will now have a .py file for each number in ListF, which able to parse its respective source HTML for the desired data.

These files can be executed individually or all at once with a simple bash script. You will now have multiple .txt files containing the parsed data. You can easily unify them with bash by doing:

cat *txt >> newfile.txt

Alternatively, you can orchestrate your own way to import this data to other file formats.
