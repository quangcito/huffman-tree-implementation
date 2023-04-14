import Node
from collections import defaultdict

def create_dictionary(text):
  text_list = list(text)
  text_dict = defaultdict(int)

  for c in text_list:
    text_dict[c] += 1
  return text_dict

print(create_dictionary("Hello"))

def huffman_encode():
  huffman_dict = create_dictionary()
  nodes = []
  for c in huffman_dict:
    nodes.append(Node(c, huffman_dict.get(c)))
  
