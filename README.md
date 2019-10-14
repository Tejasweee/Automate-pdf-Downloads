# Automate-pdf-Downloads
This python script allows to automate PDF downloads from web-pages and html files. It automatically searches all the PDF links from the given URL page and starts downloading them. It can automatically use up to Four Threads if there are more number of PDF files and helps in fast download.

# Requirements:
This script uses all the built-in libraries provided by python except for two libraries which are beautifulsoup and requests. They can be installed through pip using the command 'pip install beautifulsoup4' and 'pip install requests'. These can also be installed by running the requirements.py file which is present in this repository by running 'python requirements.py'.

# Using the Script:
- From Command Line Argument:

python getpdf.py, url

python getpdf.py, url1, url2, url3....

python getpdf.py, afile.html

python getpdf.py, afile1.html, afile2.html, afile3.html...

- Passing argument after running the script:
python getpdf.py

-- Now arguments can be passed in the input prompt

This script needs 'pandas' library to run. If pandas library is not installed this script will automatically try to install pandas first using pip.
