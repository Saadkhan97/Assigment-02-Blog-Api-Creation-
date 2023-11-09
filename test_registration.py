import requests



def test_user_registration():
    # API endpoint URL
    registration_url = 'http://127.0.0.1:8000/api/register/'

    # Data to be sent in the request
    data = {
        'username': 'saadblog',
        'email': 'saad@example.com',
        'password': 'yourpassword@@'
    }

    # Make the POST request
    response = requests.post(registration_url, data=data)
    print(response.status_code)
    # Check the response status and content
    if response.status_code == 201:  # 201 Created status for successful registration
        print(True)
        return 'User registration successful'
    else:
        print(False)
        return {'User registration failed': {response.content}, 'status':response.status_code}
test_user_registration()
