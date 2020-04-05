import random
import re
import requests

from IPython import embed
from time import sleep
from bs4 import BeautifulSoup

BASE_URL = "http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com"

def debug_input_output(function):
    
    def wrapper(*args, **kwargs):
        print(f"[START: {function.__name__}]")
        
        output = function(*args, **kwargs)

        print(f"[END: {function.__name__}]")

        return output

    return wrapper

# @debug_input_output
def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def get_random_number():
    return random.randint(1, 3)

# @debug_input_output
def extract_html_content(target_url):
    print(f"Downloading HTML content of {target_url}")
    response = requests.get(target_url)

    return response.text

# @debug_input_output
def extract_target_value_from_page(html_string, selector, cond={}):
    soup = BeautifulSoup(html_string, "html.parser")
    elements = soup.find_all(selector, cond)

    return elements

def main():
    page = "/group3/target.html"
    target_page = BASE_URL + page

    html_content = extract_html_content(target_page)
    target_values = extract_target_value_from_page(html_content, "li")

    for target_value in target_values:
        clean_text = target_value.get_text()
        clean_text = clean_text.strip().replace("\n", "")
        clean_text = re.sub(' +', ' ', clean_text)

        print(clean_text + "\n")


if __name__ == "__main__":
    main()
