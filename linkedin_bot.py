import argparse, time, urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def getPeopleLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if 'profile/view?id=' in url:
                links.append(url)
    return links

def getJobLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '/jobs' in url:
                links.append(url)
    return links

def bot(browser):
    time.sleep(5)
    page = BeautifulSoup(browser.page_source)
    people = getPeopleLinks(page)
    jobs = getJobLinks(page)
    for i in people:
        print i
    for j in jobs:
        print j
    print 'Bot exiting'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('email', help = 'linkedin email')
    parser.add_argument('password', help = 'linkedin password')
    args = parser.parse_args()

    browser = webdriver.Firefox()
    browser.get('https://linkedin.com/uas/login')

    emailElement = browser.find_element_by_id('session_key-login')
    emailElement.send_keys(args.email)

    passElement = browser.find_element_by_id('session_password-login')
    passElement.send_keys(args.password)
    passElement.submit()

    print '[+] Success Logged In'
    bot(browser)
    browser.close()

if __name__ == '__main__':
    main()
