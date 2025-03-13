def greetings(name="noble stranger"):
  if isinstance(name, str):
    print(f"Hello, {name}.")
  else:
    print("Error: Is thhat even a name?")
greetings("Alexandra")
greetings("!!!")
greetings()
greetings(1)
greetings(4)