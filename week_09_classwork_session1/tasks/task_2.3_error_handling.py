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


# Exercise 3.2: Handle timeout errors
# TODO: Send GET request with a very short timeout and catch timeout exception


# Exercise 3.3: Handle invalid JSON responses
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Try parsing JSON and handle invalid JSON errors
