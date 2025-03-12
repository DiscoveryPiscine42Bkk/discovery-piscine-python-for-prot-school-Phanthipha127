def array_of_names(persons):
  result = []
  for first, last in persons.items():
    full_name = f"{first.capitalize()} {last.capitalize()}"
    result.append(full_name)
  return result
if __name__ == "__main__":
  names = {
    "john": "Valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
  }
  print("array_of_names(persons)")