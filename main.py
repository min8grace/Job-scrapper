from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
  results = []
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('td', class_="company position company_and_position")
    jobs.pop(0)
    for job in jobs:
      title = job.find(attrs={"itemprop": "title"})
      name = job.find(attrs={"itemprop": "name"})
      location = job.find('div', class_="location")

      job_data = {
        'title': title.string,
        'name': name.string,
        'location': location.string
      }
      results.append(job_data)

    for result in results:
      print(result)
      print("----------------------------------")
  else:
    print("Can't get jobs.")


extract_jobs("python")
