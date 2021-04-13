# DailyCoding 7
mapping = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5,
  'f': 6,
  'g': 7,
  'h': 8,
  'i': 9,
  'j': 10,
  'k': 11,
  'l': 12,
  'm': 13,
  'n': 14,
  'o': 15,
  'p': 16,
  'q': 17,
  'r': 18,
  's': 19,
  't': 20,
  'u': 21,
  'v': 22,
  'w': 23,
  'x': 24,
  'y': 25,
  'z': 26
} # Given from exercise, but not used

invMapping = {str(v): k for k, v in mapping.items()}

def validateCut(cut):
  for string in cut:
    if int(string) > 26:
      return False
  return True

def insertDecoded(dic, arr):
  decoded = ''

  for item in arr:
    decoded += invMapping[item]
  if decoded in dic:
    return False
  else:
    dic[decoded] = 1
    return True

def decodeSentence(s):
  possibilities = 0
  savePossibles = []
  possibleDecodings = {}

  for length in range(1, 3): # O(1)
    for i in range(0, len(s) - length + 1): # O(n)
      cut = [s[:i], s[i:i+length],  s[i+length:]]
      cut = list(filter(lambda i: i != '', cut))
      if validateCut(cut) and insertDecoded(possibleDecodings, cut):
        possibilities += 1

  print(f'Possible decodings of {s}: {possibleDecodings}')
  return possibilities

print("RESULT: ", decodeSentence('111'))