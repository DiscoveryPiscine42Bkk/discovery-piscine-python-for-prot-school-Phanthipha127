def average(score_dict):
  total = sum(score_dict.values())
  count = len(score_dict)
  return total / count
class_3D = {
  "earlene": 27,
  "jean": 7,
  "coline": 11,
  "luc": 8
}

class_3C = {
  "quentin": 19,
  "julie": 10,
  "sarah": 21,
  "stephanie": 6
}

print(f"Average for class 3D: {average(class_3D)}.")
print(f"Average for class 3C: {average(class_3C)}.")