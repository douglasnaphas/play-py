class ClassWInits:
  def __init__(self, a="aye"):
    self.ay = a

x = ClassWInits()
y = ClassWInits("bee")
print(x.ay)
print(y.ay)
