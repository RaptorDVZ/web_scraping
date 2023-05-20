import os
import requests
from bs4 import BeautifulSoup
from docx import Document

def scrape_li_tags(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <div> element with id "post"
    post_div = soup.find('div', id='post')

    # Find all <li> tags inside the <div>
    li_tags = post_div.find_all('li')[:30]

    return li_tags

# Example usage
url = 'https://www.sarkariresult.com/admitcard/'  # Replace with the desired URL
li_tags = scrape_li_tags(url)

# Get the current directory
current_directory = os.getcwd()

# Specify the file path for saving the text file in the current directory
file_path = os.path.join(current_directory, 'admit_card.txt')

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write each <li> tag's text content to the file
    for li_tag in li_tags:
        text = li_tag.text.strip()
        file.write(text + '\n')

        # Find all <a> tags inside the <li> tag
        a_tags = li_tag.find_all('a')
        for a_tag in a_tags:
            file.write(a_tag.get('href') + '\n')

        file.write('---\n')
