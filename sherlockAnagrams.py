# HackerRank
def isAnagram(s1, s2):
  return s1 == s2

def sortedString(s):
  return ''.join(sorted(s))

def sherlockAndAnagrams(s):
  anagrams = {}

  for length in range(1, len(s)):
      for i in range(len(s) - 1):
        for j in range(i + 1, len(s) - length + 1):
          s1 = sortedString(s[i:i+length])
          s2 = sortedString(s[j:j+length])

          if s1 not in anagrams:
            anagrams[s1] = 0
          if isAnagram(s1, s2):
            anagrams[s1] += 1
          # print(f'S1: {s1}, S2: {s2}')
          # print("Dict:", anagrams)
          # print("\n\n")
  return sum(anagrams.values())
if __name__ == '__main__':
  s = input()
  result = sherlockAndAnagrams(s)
  print("RESULT: ", result)


# k k k k
# a b c d
# len = 4