import re
def same(word, target):
    count = 0
    for (w, t) in zip(word, target):
        if w == t:
            count += 1
    return count

def build(pattern, words, choices, seen):
    result = []
    for word in words:
        if re.search(pattern,word) and word not in seen.keys() and word not in choices:
            result.append(word)
    return result

def find(word, words, choices, seen,target):
    list = []
    for i in range(len(word)):
        if words[i] != target[i]:
            list += build(word[:i] + "." + word[i+1:], words, choices, seen)
    print(list)
    if list == []:
        return False
    if target in list:
        return True
    list = sorted([(same(w, target), w) for w in list], reverse = True)
    for (c,item) in list:
        choices.append(item)
        seen[item] = True
        if find(item, words, choices, seen, target):
            return True
        choices.pop()
        seen[item] = False
    return False

words = []
while True:
       start = input("Enter start word:")
       file = open("Dictionary.txt")
       lines = file.readlines()
       for line in lines:
           line = line.rstrip()
           if len(line) == len(start):
               words.append(line)
       if start not in words:
           print(start + "is not in the dictionary")
           continue
       target = input("Enter target word:")
       if len(target) != len(start):
           print("Words must be same length")
           continue
       if target not in words:
           print(target + "not in the dictionary")
           continue
       break
choices  = []
seen = {}
choices.append(start)
seen[start] = True
if find(start, words, choices, seen,target):
    choices.append(target)
    print(len(choices), choices)
else:
    print("No ladder found")