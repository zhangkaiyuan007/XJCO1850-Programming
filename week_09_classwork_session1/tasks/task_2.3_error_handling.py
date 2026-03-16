"""
Task 2.3: Handle Errors in API Requests

Goal: Learn to handle common API errors including 404s, timeouts, and invalid JSON.

Exercises:
- Handle 404 errors
- Handle timeout errors
- Handle invalid JSON responses
"""

import httpx

# Exercise 3.1: Handle 404 errors
url = "https://jsonplaceholder.typicode.com/posts/9999"
# TODO: Send GET request and handle 404 error
response = httpx.get(url)
if response.status_code == 404:
    print("Error: Post not found (404).")
else:
    print("Post found:", response.status_code)


# Exercise 3.2: Handle timeout errors
# TODO: Send GET request with a very short timeout and catch timeout exception
try:
    httpx.get("https://jsonplaceholder.typicode.com/posts", timeout=0.001)
    print("Request completed.")
except httpx.TimeoutException:
    print("Error: Request timed out.")


# Exercise 3.3: Handle invalid JSON responses
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Try parsing JSON and handle invalid JSON errors
response = httpx.get(url)
try:
    data = response.json()
    print(f"Fetched {len(data)} posts.")
except ValueError:
    print("Error: Invalid JSON received.")
