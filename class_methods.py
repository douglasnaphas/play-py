
# do classmethods have lower precedence than instance methods of the same name?
# (when the instance method is in a base class)

class BaseClass:
  @classmethod
  def some_method(cls):
    print("base some_method called")

class DerivedClass(BaseClass):
#  def __init__(self):
#    pass
#  def some_method(cls):
#    print("derived some_method called")
  pass

x = DerivedClass()
x.some_method()
print(type(x))
x.some_member = "some member"
print(x.some_member)
BaseClass.some_method()
DerivedClass.some_method()
