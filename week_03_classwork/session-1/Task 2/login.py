username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()

if username and password:
  print("Login successful!")
else:
  print("Both username and password are required.")

# we need at least four test cases
# we don't need title() because we user usually type exactly they set 