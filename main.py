import requests
from datetime import datetime
USERNAME = 'unknown0perator'
TOKEN = 'SomethingRandom'
pixela_endpoint = 'https://pixe.la/v1/users'
user_parameters = {
    'token': USERNAME,
    'username': TOKEN,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
headers = {
    'X-USER-TOKEN': TOKEN
}
graph_config = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'momiji',
    }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today_date = datetime.now()
pixel_data = {
    'date': today_date.strftime('%Y%m%d'),
    'quantity': '5',
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
