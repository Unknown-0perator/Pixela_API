import requests
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
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
