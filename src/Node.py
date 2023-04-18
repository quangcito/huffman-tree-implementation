class BST:
  """Implements a typical Binary Search Tree that does no balancing. It also includes
  several general binary tree algorithms, just so you can see them."""


  def __init__(self, character, occurences, left = None, right = None):
    self.character = character
    self.occurence = occurences
    self.left = left
    self.right = right
    self.code = None
