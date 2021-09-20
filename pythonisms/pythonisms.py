class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class BaseLinkedList:
  def __init__(self, collection=None):
    self.head = None
    self._length = 0
    if collection:
      for item in reversed(collection):
        self.insert(item)

class LinkedList(BaseLinkedList):
  
  def traverse(self, action):
    current = self.head
    while current:
      action(current.value)
      current = current.next

  def __iter__(self):
    def generator():
      current = self.head
      while current:
        yield current.value
        current = current.next
    return generator()
  
  def __str__(self):
    out = ""
    for value in self:
      out += f"[{value}] -> "
    return out + "None"

  def __len__(self):
    return self._length
  
  def insert(self, value):
    self.head = Node(value, self.head)
    self._length += 1
  
  def __getitem__(self, index):
    # loop through the linked list, keeep a counter, whent eh counter  = index return the item

    if index < 0:
      raise IndexError

    for i, item in enumerate(self):
      if i == index:
        return item
    
    raise IndexError
    


class Math:
  def __init__(self):
    self.total = 0
    self.product = 1
    self.squares = []

  def adder(self, value):
    self.total += value

  def multiplier(self, value):
    self.product *= value
  
  def squarer(self, value):
    self.squares.append(value ** 2)



def capital_letter(text):
    return text.upper()
 
def small_letter(text):
    return text.lower()
 
def hi(func):
    greeting = func("""Hi, How is every thing?""")
    print (greeting)
 
hi(capital_letter)
hi(small_letter)