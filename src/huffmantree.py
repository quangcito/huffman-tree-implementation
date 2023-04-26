from Node import Node
from collections import defaultdict
import heapq

def create_dictionary(text):
  text_list = list(text)
  text_dict = defaultdict(int)

  for c in text_list:
    text_dict[c] += 1

  text_dict = dict(sorted(text_dict.items(), key=lambda x:x[1], reverse=True))
  return text_dict

def huffman_encode(text):
  huffman_dict = create_dictionary(text)
  nodes = []
  for c in huffman_dict.keys():
    # nodes.append(Node(c, huffman_dict.get(c)))
    heapq.heappush(nodes, (c, huffman_dict.get(c)))

  while len(nodes) > 1:
    # left_node = nodes.pop()
    # right_node = nodes.pop()
    left_node = heapq.heappop(nodes)
    right_node = heapq.heappop(nodes)

    left_node.code = 0
    right_node.code = 1

    combined_node = Node(left_node.character + right_node.character, left_node.occurences + right_node.occurences, left_node, right_node)
    # nodes.append(combined_node)
    heapq.heappush(nodes, combined_node)
    # sorted(nodes, key=lambda node:node.occurences, reverse=True)
    # sorted(nodes, key=lambda node:node.occurences)

  return nodes[0]


# print(huffman_encode("hello"))

# node = huffman_encode("hello")

# print(node)

# print(node.left.left.code)

# print(node.right.code)

# def get_code(node):
#   while not node.left and not node.right:

encoded_dict = {}
def get_huffman_code(node, code=''):

  new_code = code + str(node.code)
  if node.left:
    get_huffman_code(node.left, new_code)
  if node.right:
    get_huffman_code(node.right, new_code)
  if (not node.right and not node.left):
    encoded_dict.update({node.character: new_code})
  return encoded_dict

def encode_text_from_dict(text,dict):
  encoded_text = ""
  for c in text:
      if c in dict:
        encoded_text += dict.get(c)
      else:
        return "Your input string is not applicable with the huffman tree constructed from your encoded string"
  return encoded_text

def ask_question():
  print("Type in a string you want to encode: \n")
  encoded_string = input()
  huffman_tree_dict = get_huffman_code(huffman_encode(encoded_string))
  print("Would you like to encode a text or decode a binary string? (encode/decode)\n")
  answer = input()
  if answer == 'encode':
    print("Type in a text you want to encode: \n")
    text = input()
    print(huffman_encode(encoded_string))
    print(huffman_tree_dict)
    print(encode_text_from_dict(text, huffman_tree_dict))

    # Helper method to check if all characters of the text is in the huffman tree
  if answer == 'decode':
    print("Type in a binary string you want to decode: \n")
    binary_string = input()

# print(get_huffman_code(node))

ask_question()
