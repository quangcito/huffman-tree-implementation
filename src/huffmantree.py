import BSTClass
from collections import defaultdict

def create_dictionary():
  text = input()
  text_list = list(text)
  text_dict = defaultdict(int)

  for c in text_list:
    text_dict[c] += 1
  return text_dict

print(create_dictionary())

def create_node(c):
  return
