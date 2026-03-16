"""
Task 2.2: Send Data Using POST Requests

Goal: Learn to send data to an API using POST requests.

Exercises:
- Create a new post
- Add a new comment to a post
- Create a new user
"""

import httpx

# Exercise 2.1: Create a new post
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Define new post data and send POST request
new_post = {
    "title": "Learning APIs with httpx",
    "body": "This is a test post created for the API exercise.",
    "userId": 1
}
response = httpx.post(url, json=new_post)
print("Create post response:")
print(response.json())


# Exercise 2.2: Add a new comment to a post
url = "https://jsonplaceholder.typicode.com/comments"
# TODO: Define new comment data and send POST request
new_comment = {
    "postId": 1,
    "name": "API Exercise",
    "email": "student@example.com",
    "body": "This is a test comment."
}
response = httpx.post(url, json=new_comment)
print("\nCreate comment response:")
print(response.json())


# Exercise 2.3: Create a new user
url = "https://jsonplaceholder.typicode.com/users"
# TODO: Define new user data and send POST request
new_user = {
    "name": "Charlie Davis",
    "username": "charlied",
    "email": "charlie.davis@example.com"
}
response = httpx.post(url, json=new_user)
print("\nCreate user response:")
print(response.json())
