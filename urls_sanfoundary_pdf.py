# read urls.txt file that contains urls in list format 
# Using requests module to get html with urls
# Using BeautifulSoup to parse html
# find element with class name "entry-content" now in this element
# edit html such 
# this type of tags <div id="target-id613a2aa9470de" class="collapseomatic_content " style="display: none;">
# style attribute is removed
# use regular expression to find all div tags with class attribute
# Using pdfkit to convert html to pdf

import requests
import re
from bs4 import BeautifulSoup
import pdfkit

urls = []
with open('urls.txt', 'r') as f:
    for line in f:
        urls.append(line)

# function to get html from url
def get_html(url):
    response = requests.get(url)
    return response.text

# function to get all div tags with class attribute
def get_div_tags(html):
    soup = BeautifulSoup(html, "lxml")
    main_div = soup.find('div', class_='entry-content')
    div_tags = main_div.find_all("div", class_="collapseomatic_content")
    # change style attribute to none for each div tag
    for div in div_tags:
        div.attrs['style'] = None
    return main_div

# function to convert html to pdf
def convert_html_to_pdf(html, filename):
    pdfkit.from_string(str(html), filename)


# main function
def main():
    for url in urls:
        html = get_html(url)
        html = get_div_tags(html)
        convert_html_to_pdf(html, 'output.pdf')
        break

# run main function
if __name__ == '__main__':
    main()

