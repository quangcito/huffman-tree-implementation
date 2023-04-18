from Node import Node
from collections import defaultdict

def create_dictionary(text):
  text_list = list(text)
  text_dict = defaultdict(int)

  for c in text_list:
    text_dict[c] += 1

  text_dict = dict(sorted(text_dict.items(), key=lambda x:x[1], reverse=True))
  return text_dict

# print(create_dictionary("Hello"))

def huffman_encode(text):
  huffman_dict = create_dictionary(text)
  nodes = []
  huffman_nodes = []
  for c in huffman_dict.keys():
    nodes.append(Node(c, huffman_dict.get(c)))

  while not nodes and len(nodes) > 0:
    left_node = nodes.pop()
    right_node = nodes.pop()

    left_node.code = 0
    right_node.code = 1

    combined_node = Node(left_node.character + right_node.character, left_node.occurences + right_node.occurences, left_node, right_node)
    huffman_nodes.append(combined_node)

  huffman_nodes.append(nodes[0])

  return nodes
  print(repr(nodes))

print(huffman_encode("hello"))

for node in huffman_encode("hello"):
  print(node.character, node.occurences)

print(huffman_encode("hello").pop().character)
