# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:30:17 2021
TEAM 1
author : Mugdha
script for scrapping software engineer job title and description
"""

from selenium import webdriver
import time
import csv
import re
import random
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

def scrape(url):
    #write job description and title to file
    fw = open('software_engineer.csv', 'a', encoding='utf8')
    writer = csv.writer(fw, lineterminator = '\n')
    writer.writerow(['jobtitle', 'text'])
    
    pageUrl = url + "&start="
    
    page = 0
    
    while True:
        options = Options()
        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)
        options.add_argument(f'user-agent={userAgent}')
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

        if page == 2000:
            break

        currentUrl = pageUrl + str(page)
        driver.get(currentUrl)

        time.sleep(3)
        
        jobsPerPage = driver.find_elements_by_class_name('jobsearch-SerpJobCard.unifiedRow.row.result.clickcard')
        
        for jobCard in jobsPerPage:
            try:
                jobTitleList = jobCard.find_element_by_class_name('title').text
                jobTitle = jobTitleList.splitlines()[0]
                jobTitle = re.sub(r'[^A-Za-z ]+', ' ', jobTitle)
            except:
                print('error fetching job title')

            try:    
                #get job description url from jobcard
                linkElement = jobCard.find_element_by_css_selector('a[data-tn-element="jobTitle"]')
                jobDescrUrl = linkElement.get_attribute('href')

                # Open a new window
                driver.execute_script("window.open('');")
                # Switch to the new window and open job description URL
                driver.switch_to.window(driver.window_handles[1])
                driver.get(jobDescrUrl)

                time.sleep(random.randint(2,5))

                jobDescription = driver.find_element_by_css_selector('div[id="jobDescriptionText"]').text

                #keep only text and spaces
                jobDescription = re.sub(r'[^A-Za-z ]+', ' ', jobDescription)

                # if no jobTitle, get it from job description page
                if jobTitle:
                    jobTitle = driver.find_element_by_class_name('icl-u-xs-mb--xs.icl-u-xs-mt--none.jobsearch-JobInfoHeader-title').text
                    jobTitle = re.sub(r'[^A-Za-z ]+', ' ', jobTitle)
                # Close the tab with URL B
                driver.close()
                # Switch back to the first tab with URL A
                driver.switch_to.window(driver.window_handles[0])
                
            except:
                print('error fetching job description')
            
            if jobTitle and jobDescription:
                writer.writerow([jobTitle, jobDescription])

        page += 10
        
    fw.close()

url = "https://www.indeed.com/jobs?q=Software+Engineer&l=San+Diego%2C+CA"
scrape(url)