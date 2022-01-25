### BIA 660 Team 1

Submission Files:
1. data_scientist_scraper.py
2. software_engineer_scraper.py
3. classifier.py
4. data_scientist.csv
5. software_enginner.csv
6. test.csv
7. README.txt

Part 1 - Scrapping Scripts Execution:

Step 1: Open data_scientist_scraper.py and software_engineer_scraper.py

Step 2: Install python fake-useragent libray using 'pip install fake-useragent'. Also make sure you have all other libraries from import

Step 3: Default url for indeed.com Data Scientist and Software Engineer job titles already defined in line 89 for both scraper files

Step 4: Use the same url or provide a different one of same structure

Step 5: Make sure chromedriver is in the same folder as scripts

Step 6: Run the scripts

Step 7: Selenium Web driver will scrape Job Title and Text for multiple pages

Step 8: Scraped Data for Job title and Text will be stored in data_scientist.csv and software_engineer.csv accordingly


Part 2 - Classification Script Execution:

Step 1: Open the classifier.py file 

Step 2: Change path for external input test file at line 50 or use the default test.csv file

Step 3: Make sure you have all the libraries from import

Step 4: Default test.csv file consists of 6 data scientist + 6 software engineer job descriptions

Step 5: Input test file should NOT include any header

Step 6: Run the classifier.py script, it takes about 3-4 min

Step 7: Accuracy for scraped testing data will be displayed on console

Step 8: Project_Predicted_Job_Title.csv will be generated consisting of header and predicted job title for external input test file