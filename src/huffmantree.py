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
    heapq.heappush(nodes, Node(c, huffman_dict.get(c)))

  while len(nodes) > 1:
    left_node = heapq.heappop(nodes)
    right_node = heapq.heappop(nodes)

    left_node.code = 0
    right_node.code = 1

    combined_node = Node(left_node.character + right_node.character, left_node.occurences + right_node.occurences, left_node, right_node)
    heapq.heappush(nodes, combined_node)

  return nodes[0]

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


def traverseTree(node, binaryString):
  for i in range(len(binaryString) + 1):
    if (not node.left and not node.right):
      binaryString = binaryString[i:]
      return [node.character, binaryString]
    elif binaryString[i] == "0" and node.left:
      node = node.left
    elif binaryString[i] == "1" and node.right:
      node = node.right

def decodeText(node, binaryString):
  decodedText = ""
  while binaryString:
    traversal_result = traverseTree(node, binaryString)
    decodedText += traversal_result[0]
    binaryString = traversal_result[1]
  return decodedText


def encode_text_from_dict(text,dict):
  encoded_text = ""
  for c in text:
      if c in dict:
        encoded_text += dict.get(c)
      else:
        return "Your input string is not applicable with the huffman tree constructed from your encoded string"
  return encoded_text


def ask_questions():
    print("Type in a string you want to encode: \n")
    encoded_string = input()
    root = huffman_encode(encoded_string)
    huffman_tree_dict = get_huffman_code(root)
    while True:
      print("Would you like to encode a text or decode a binary string? (encode/decode/cancel)\n")
      answer = input()
      if answer == 'cancel':
        return
      elif answer == 'encode':
        print("Type in a text you want to encode: \n")
        text = input()
        print(encode_text_from_dict(text,huffman_tree_dict))
        continue
        # Helper method to check if all characters of the text is in the huffman tree
      elif answer == 'decode':
        print("Type in a binary string you want to decode: \n")
        binary_string = input()
        print(decodeText(root,binary_string))
        continue
      else: 
        print("That's an invalid input. Please try a different input.")
        continue
  

ask_questions()


