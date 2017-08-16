import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])
#for (c,t) in zip(item, target):
#  if c == t:
#    return c

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]
#for word in words:
#  if re.search(pattern, word) and word not in seen.keys() and word not in list:
#    return word

def sfind(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    if word[i] != target[i]:# this will reduce the words in list
      list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False # if cannot find any word like the target word, there is no such a path
  if target in list:# this will make the search more efficient
    return True # this will make the search more efficient
  list = sorted([(same(w, target), w) for w in list], reverse=True) # sorted in decrease order so that it is easier to choose the shorest way.
  for (match, item) in list:
       if match >= len(target) - 1: #if not the same and there is one or more letters different.
         if match == len(target) - 1: #if only one word
            path.append(item) # add this word to path
         return True
       seen[item] = True
  for (match, item) in list:
    path.append(item)
 #   seen[item] = True # move to this place: after adding the word to path
    if find(item, words, seen, target, path):
      return True
    path.pop() # if not delete this word from path and go back to upper level

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

while True:
     fname = input("Enter dictionary name: ")
     file = open(fname)
     lines = file.readlines()
     start = input("Enter start word:")
     words = []
     for line in lines:
        word = line.rstrip()
        if len(word) == len(start):
          words.append(word)
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
choice1 = input('Are there any words you dont want in the path?')
if choice1 == 'Yes' or choice1 == 'yes':
    print("Please type one word in one line and type 0 in the end:")
    delete = input()
    while delete != 0:
        words.remove(delete)
        delete = input()
        break
path = [start]
seen = {start : True} # have already seen this word
choice2 = input("Do you want the shorest way?")
if choice2 == 'Yes' or choice2 == 'yes':
    if sfind(start, words, seen, target, path):
      path.append(target)
      print(len(path) - 1, path)
    else:
      print("No path found")
else:
    if sfind(start, words, seen, target, path):
          path.append(target)
          print(len(path) - 1, path)
    else:
          print("No path found")