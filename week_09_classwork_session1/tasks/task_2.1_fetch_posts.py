"""
Task 2.1: Fetch and Display Posts Using GET Request

Goal: Learn to make GET requests to an API and display the results.

Exercises:
- Fetch and display all posts (first 5)
- Fetch a single post by ID
- Fetch users and display their names
"""

import httpx

# Exercise 1.1: Fetch and display all posts (first 5)
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Send GET request and display first 5 posts
response = httpx.get(url)
if response.status_code == 200:
    posts = response.json()
    print("First 5 posts:")
    for post in posts[:5]:
        print(f"- ({post['id']}) {post['title']}")
else:
    print(f"Error fetching posts: {response.status_code}")


# Exercise 1.2: Fetch a single post by ID
url = "https://jsonplaceholder.typicode.com/posts/1"
# TODO: Send GET request and display the post details
response = httpx.get(url)
if response.status_code == 200:
    post = response.json()
    print("\nPost #1:")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
else:
    print(f"Error fetching post: {response.status_code}")


# Exercise 1.3: Fetch users and display their names
url = "https://jsonplaceholder.typicode.com/users"
# TODO: Send GET request and display user names
response = httpx.get(url)
if response.status_code == 200:
    users = response.json()
    print("\nUser names:")
    for user in users:
        print(f"- {user['name']}")
else:
    print(f"Error fetching users: {response.status_code}")
