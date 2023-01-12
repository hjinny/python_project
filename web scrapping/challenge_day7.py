from bs4 import BeautifulSoup

#방법1. 셀레니엄으로 웹봇이 아닌 브라우저임을 인식시키기
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

base_url    = "https://remoteok.com/"
search_term = "python"

browser = webdriver.Chrome(options=options)
browser.get(f"{base_url}{search_term}")

print(browser.page_source)


#방법2. 503 error (userAgent 지정)
"""
from requests import get

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


#response = get(f"{base_url}remote-{search_term}-jobs", headers=header)
response = get("https://remoteok.com/remote-engineer+python-jobs?benefits=401k&min_salary=140000", headers=header)
if response.status_code != 200:
  print("Can't request website")

  
else:
  results = []

  soup = BeautifulSoup(response.text, "html.parser")
  jobs_tables = soup.find('table', id="jobsboard")
  #jobs_table = jobs_tables.find_all('tr', data-offset)
  
  #print(jobs)
"""