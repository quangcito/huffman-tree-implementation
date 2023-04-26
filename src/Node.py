class Node:
  """Implements a typical tree node. It also includes specialized properties for huffman tree node."""


  def __init__(self, character, occurences, left = None, right = None):
    self.character = character
    self.occurences = occurences
    self.left = left
    self.right = right
    self.code = ''

  def __repr__(self):
    return repr({self.character:self.occurences})

  def __lt__(self, nxt):
    return self.occurences < nxt.occurences

