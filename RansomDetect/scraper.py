# Download all the reports of the submited urls
# sometimes ther is something wrong with network or the website 
# use the script specific_scraper.py to get missing reports

import os, time
from socket import timeout 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# add your github token
os.environ['GH_TOKEN'] = ""

options = webdriver.FirefoxOptions()
#options.add_argument('--headless')
options.set_preference("browser.helperApps.alwaysAsk.force", False)
options.set_preference("browser.download.manager.showWhenStarting",False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-7z-compressed;application/x-rar-compressed;application/zip")

browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

base_url = "https://cuckoo.cert.ee"
submit_urls = [
    "https://cuckoo.cert.ee/submit/post/3520337",
    "https://cuckoo.cert.ee/submit/post/3520348"
    ]
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }


total_reports_fetched = 0
# to handle the problems of the network or the website
timeout = 30
sleep_time = 300
timeSLeep = 10

for submit_url in submit_urls:
    reports_not_fetched = 0
    browser.get(submit_url)

    table_body = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.clickable:nth-child(1)")))
    table_body = table_body.find_element(By.XPATH,'..')
    reports = table_body.find_elements(By.CSS_SELECTOR, "tr > td:nth-child(1)")

    reports_id = list(map(lambda element: element.get_attribute('innerHTML'), reports))

    print("\n[INFO] submit:", submit_url)
    print('[INFO] fetching', len(reports_id) , 'reports')

    for report_id in range(len(reports_id)):
        print("[INFO] getting report of : " + reports_id[report_id])
        browser.get(base_url + '/analysis/'+ reports_id[report_id] +'/export/')
        try:
            WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
            download_button = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
            if(timeSLeep > 5):
                timeSLeep = timeSLeep - 1
            time.sleep(timeSLeep)
            download_button.click()
            if(sleep_time > 10):
                sleep_time = sleep_time - 40
            if(sleep_time < 0 ):
                sleep_time = 10
            time.sleep(sleep_time)
        except:
            print("[ERROR] couldn't download report :", reports_id[report_id])
            reports_not_fetched = reports_not_fetched + 1
        time.sleep(1)

    print('[SUCCESS]: fetched', len(reports_id)-reports_not_fetched, 'reports')
    total_reports_fetched = total_reports_fetched + len(reports_id)-reports_not_fetched

while(input("[WARNING] type 'YES' when the download has finished: ") != "YES"):
    continue
print('[SUCCESS]: total reports fetched', total_reports_fetched)
#browser.quit()
