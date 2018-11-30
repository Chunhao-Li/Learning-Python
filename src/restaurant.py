class Restaurant():
  """"""
  def __init__(self, name, cuisine_type):
    """"""
    self.restaurant_name = name
    self.cuisine_type = cuisine_type
    self.number_serverd = 0

  def describe_restaurant(self):
    """"""
    print("The restaurant's name is " + self.restaurant_name)
    print("The cuisine type is " + self.cuisine_type)

  def open_restaurant(self):
    """"""
    print("The restaurant " + self.restaurant_name + " is open!")

  def set_number_served(self, number):
    """"""
    self.number_serverd = number 

  def increment_number_served(self, increment):
    """"""
    self.number_serverd += increment 