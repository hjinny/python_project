#from extractor.wwr import extract_wwr_jobs
from extractor.indeed import extract_indeed_jobs
from file import save_to_file

keyword = input("What do you want to search for? ")

indeed = extract_indeed_jobs(keyword)
#wwr = extract_wwr_jobs(keyword)
jobs = indeed  # + wwr

save_to_file(keyword, jobs)