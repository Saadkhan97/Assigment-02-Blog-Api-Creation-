import requests



def test_create_blog_post(token):

    create_blog_post_url = 'http://127.0.0.1:8000/api/blog/post/create/'  # Replace with the actual blog post creation API endpoint


    data = {
        'title': 'Sample Blog Post from saadBlog',
        'content': 'This is the content of saadBlog.'
    }


    headers = {
        'Authorization': f'Token {token}'
    }


    response = requests.post(create_blog_post_url, data=data, headers=headers)
    print(response.content)


    if response.status_code == 201:
        print(True)
        return 'Blog post creation successful'
    else:
        print(False)
        return {'Blog post creation failed': response.content, 'status': response.status_code}


test_create_blog_post('2e00166b97c7abb0db51c25cc20c41960106213a')
