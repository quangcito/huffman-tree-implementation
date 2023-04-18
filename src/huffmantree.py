from Node import Node
from collections import defaultdict

def create_dictionary(text):
  text_list = list(text)
  text_dict = defaultdict(int)

  for c in text_list:
    text_dict[c] += 1

  text_dict = dict(sorted(text_dict.items(), key=lambda x:x[1]))
  return text_dict

# print(create_dictionary("Hello"))

def huffman_encode(text):
  huffman_dict = create_dictionary(text)
  nodes = []
  for c in huffman_dict.keys():
    nodes.append(Node(c, huffman_dict.get(c)))
  print(repr(nodes))

print(huffman_encode("hello"))
