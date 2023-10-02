import requests

def load_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Example usage
url = "index.html"
page_content = load_page(url)
if page_content:
    print(page_content)
else:
    print("Failed to load the page.")
