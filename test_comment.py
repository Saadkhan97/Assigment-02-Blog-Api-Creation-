import requests


def test_create_comment(token, post_id):

    create_comment_url = f'http://127.0.0.1:8000/api/blog/post/{post_id}/comment/create/'


    data = {
        'text': 'This is a Saadblog comment.',
                'blog_post': post_id,
    }


    headers = {
        'Authorization': f'Token {token}'
    }


    response = requests.post(create_comment_url, json=data, headers=headers)
    print(response.text)

    if response.status_code == 201:
        print(True)
        return 'Comment creation successful'
    else:
        print(False)
        return {'Comment creation failed': response.content, 'status': response.status_code}

test_create_comment('2e00166b97c7abb0db51c25cc20c41960106213a', 3)
