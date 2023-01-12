from bs4 import BeautifulSoup

#셀레니엄으로 웹봇이 아닌 브라우저임을 인식시키기 (indeed 페이지에서 봇인지 체크함)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


#페이지 건수 추출
def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs?q="

  browser = webdriver.Chrome(options=options)
  browser.get(f"{base_url}{keyword}")
  print("browser : ", f"{base_url}{keyword}")

  soup = BeautifulSoup(browser.page_source, "html.parser")

  pagination = soup.find("nav", role="navigation")

  if pagination == None:
    return 1

  pages = pagination.find_all("div", recursive=False)
  lastOne = pagination.select_one("div a svg")

  # 페이지가 5개 이하인 경우 고려
  if len(lastOne) >= 1:
    count = len(pages) - 1
  else:
    count = len(pages)

  return count


#Web scrapping
def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  print("Found", pages, " pages")

  results = []

  for page in range(pages):

    print("Cycle : ", page)

    base_url = "https://kr.indeed.com/jobs"
    final_url = f"{base_url}?q={keyword}&start={page*10}"
    print("Requesting Site = ", final_url)

    browser = webdriver.Chrome(options=options)
    browser.get(final_url)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all("li", recursive=False)

    #한 페이지에 총 18개 li있지만 3개는 불필요한 요소 >> 한 페이지에 15개
    print("How many of jobs : ", len(jobs))

    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")

      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")

        job_data = {
          'link': f"https://kr.indeed.com{link}",
          'company': company.string.replace(",", " "),
          'position': title.replace(",", " "),
          'location': location.string.replace(",", " ")
        }

        results.append(job_data)

    #print("Result of scrapping : ", results, "\n")
  return results


#호출
#extract_indeed_jobs("flask")
