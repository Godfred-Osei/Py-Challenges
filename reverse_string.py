text = "Hello, I'm Jappy-Lappy-Happy"
new_text = ''.join(filter(str.isalnum, text)).lower()
reversed_text = new_text[::-1]

print(reversed_text)
