import requests

# BASE_URL = 'https://smartmark01.herokuapp.com'
BASE_URL = 'http://localhost:8000'


def main():
    # WRITE DATA
    response = requests.post(BASE_URL + '/get_on_from_app', data={'switch_state': 1})
    print(response.content)

    # READ DATA from Server
    response = requests.get(BASE_URL + '/send_raspberry_bright')
    print(response.content)


if __name__ == "__main__":
    main()