# DailyCoding 29
def encode(s):
  length = len(s)
  i = 0
  encoded = ''

  while i < length:
    current = previous = s[i]
    j = i
    count = 0
    while current == previous:
      count += 1
      j += 1
      if j > len(s) - 1:
        break
      previous = current
      current = s[j]
    encoded += f"{count}{s[i]}"
    i = j

  return encoded

def decode(s):
  letters = s[1::2]
  numbers = s[0::2]
  decoded = ''

  for i in range(len(letters)):
    decoded += int(numbers[i]) * letters[i]

  return decoded

s = "AAAABBBCCDAA"
encoded = encode(s)
decoded = decode(encoded)
assert s == decode(encode(s))