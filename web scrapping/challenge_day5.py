from requests import get

websites = ( "google.com", "airbnb.com", "https://twitter.com", "facebook.com", "https://tiktok.com")
  
results = {}

for website in websites: 
  if not website.startswith("https://"):
    website = f"https://{website}"

  response = get(website)

  if (response.status_code >= 100 and response.status_code < 200):
    results[website] = "Information responses"
  elif (response.status_code >= 200 and response.status_code < 300):
    results[website] = "Successful responses"
  elif (response.status_code >= 300 and response.status_code < 400):
    results[website] = "Redirection messages"
  elif (response.status_code >= 400 and response.status_code < 500):
    results[website] = "Client error responses"
  elif (response.status_code >= 500 and response.status_code < 600):
    results[website] = "Server error reponses"

print(results)