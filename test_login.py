import requests



def test_user_login():
    # API endpoint URL
    login_url = 'http://127.0.0.1:8000/api/login/'  # Replace with the actual login API endpoint

    # Data to be sent in the request
    data = {
        'username': 'saadblog',  # Use the email you registered with
        'password': 'yourpassword@@'  # Use the corresponding password
    }

    # Make the POST request
    response = requests.post(login_url, data=data)
    print(response.content)


    if response.status_code == 200:  # 200 OK status for successful login
        token = response.json().get('token')
        if token:
            print(True)
            #returns jwt token
            return f'User login successful. Token: {token}'
    else:
        print(False)
        return {'User login failed': response.content, 'status': response.status_code}

test_user_login()
