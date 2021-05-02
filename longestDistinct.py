# DailyCoding 13

def solution(s, k):
  longestSubstringLength = -1
  substrings = []
  for i in range(len(s)):
    substring = s[i]
    distinct = 1
    for j in range(i+1, len(s)):
      if s[j] not in substring:
        distinct += 1
      if distinct <= k:
        substring += s[j]
        longestSubstringLength = max(longestSubstringLength, len(substring))
        substrings.append(substring)
      else:
        break
  print(max(substrings, key=len))
  return longestSubstringLength

print(solution('aaaaaaaaabc', 2))