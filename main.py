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
response = requests.post(pixela_endpoint, json=user_parameters)
print(response.text)
