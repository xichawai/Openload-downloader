import os,time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import argparse
from argparse import ArgumentDefaultsHelpFormatter

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_options.add_argument('--disable-gpu')

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.set_page_load_timeout(200)


parser = argparse.ArgumentParser(prog="Spider", description='parse arg', formatter_class=ArgumentDefaultsHelpFormatter)

parser.add_argument('-u', dest='url', action='store', required=True, help='the file url')

print parser.parse_args()
url = parser.parse_args().url

try:
    chrome.get(url)
    print chrome.title
    elem =chrome.find_element_by_id("btnDl")
    elem.click()
    time.sleep(5)
    elem2 = chrome.find_element_by_id("downloadTimer")
    elem2.click()
    content = chrome.page_source
    tree = etree.HTML(content)
    download_url = tree.xpath("//span[@id='streamurl']/text()")
    print download_url
    chrome.quit()
except Exception as e:
    chrome.quit()
    print e