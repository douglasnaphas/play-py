def use_kwargs(*args, **kwargs):
  print("*************")
  print(args)
  if len(args) > 0:
    print(args[0])
  print(kwargs)
  if "c" in kwargs:
    print(kwargs["c"])
use_kwargs("A")
use_kwargs("B", c="d")
