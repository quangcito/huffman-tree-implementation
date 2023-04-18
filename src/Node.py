class Node:
  """Implements a typical Binary Search Tree that does no balancing. It also includes
  several general binary tree algorithms, just so you can see them."""


  def __init__(self, character, occurences, left = None, right = None):
    self.character = character
    self.occurences = occurences
    self.left = left
    self.right = right
    self.code = None
    
  def __repr__(self):
    return repr({self.character:self.occurences})

