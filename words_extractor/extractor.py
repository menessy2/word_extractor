import re
from bs4 import BeautifulSoup
from collections import Counter
import urllib.request
from security.html_sanitizer import sanitize_html
import requests



def return_words_from_remote_url_page(url):
    f = requests.get(url)
    soup = BeautifulSoup(f.text,"lxml")
    all_text = sanitize_html(soup.get_text())
    words = re.findall(r'\w+', all_text)                                       #This finds words in the document
    cap_words = [word.upper() for word in words if word.isalpha()]            #capitalizes all the words
    word_counts = Counter(cap_words)                        #counts the number each time a word appears
    return word_counts



def return_most_frequent_n(counter_obj, number):
    return counter_obj.most_common(number)