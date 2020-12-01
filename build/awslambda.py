import requests
def call_google(event=None, context=None):
    r = requests.get("https://www.google.com")
    if r.status_code == 200:
        return "This is done"