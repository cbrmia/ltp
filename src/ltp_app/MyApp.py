import requests

class MyApp:
    def __init__(self):
        rq = requests.get("https://randomuser.me/api/").json()
        self.name = rq["results"][0]["name"]["first"]

    def __str__(self):
        return f"Hello, this is the {self.name} LTP app."
