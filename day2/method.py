class person:
  def __init__(self, name):
      self.name = name
  
  def greet(self):
    print("hello, my name is " + self.name)

p1 = person("Adil")
p2 = person("Emil")
p2.greet()