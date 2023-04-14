import BSTClass
from collections import defaultdict

def encode_text():
  text = input()
  text_list =  list(text)

  text_dict = defaultdict(int)

  for c in text_list:
    text_dict[c] += 1


  return text_dict

print(encode_text())
