import requests

def get_latest_repo(username: str):
    print("Github Tool Called")

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    repos = response.json()

    latest = sorted(
        repos,
        key=lambda repo: repo["created_at"],
        reverse=True
    )[0]

    return {
        "name": latest["name"],
        "url": latest["html_url"],
        "description": latest["description"],
        "stars": latest["stargazers_count"]
    }