import sys
if len(sys.arge) ==2:
  parameter = sys.argv[1]
  user_input = input("Enter a word:" )
  if user_input == parameter:
    print("Good job!")
  else:
    print("Nope, sorry...")
else:
  print("none")