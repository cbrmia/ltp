import requests

class MyApp:
    def __init__(self, name=None):
        if not name:
            rq = requests.get("https://randomuser.me/api/").json()
            self.name = rq["results"][0]["name"]["first"]
        else:
            self.name = name

    def __str__(self):
        return f"Hello, this is the {self.name} LTP app. (DEV)"
