def solution(text):
    text = text.strip()


result = ""
for i, c in enumerate(text):
 if c in ",.?!:":
 if i == 0 or text[i-1] == " ":
result = result[:-1]
result += c
if i != len(text) - 1:
result += " "
else:
result += c
return result
