import requests


def check_website(url):
    """
    Checks website if its 200, 404 or error using request as and exercise
    I also add a try except block to practice nested loop
    """

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            print("Its good server running")
            print(response.text[:250])
        else:
            print(f"Server responded with status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print(
            "Failed to connect! The website URL might be wrong or your internet is down."
        )

    except requests.exceptions.RequestException as e:
        print(f"A general network issue occurred: {e}")


check_website("https://topmapsolutions.com/")
