title = input()
words = [word for word in title.lower().split()]
slug = ""
for word in words:
  if word == "a" or word == "the":
    words.remove(word)

for word in words:
  for character in word:
    if character == ":" or character == ",":
      word = word[0:len(word)-1]
  slug += word + "-"

if len(slug) >= 25:
  slug = slug[0:25]
else:
  slug = slug[0:-1]

print(f"Slug = {slug}")