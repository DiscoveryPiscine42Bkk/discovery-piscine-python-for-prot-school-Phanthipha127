import sys
if len(sys.argv) == 3:
  keyword = sys.argv[1]
  search_string = sys.argv[2]
  count = search_string.count(keyword)
  if count > 0:
    print(count)
  else:
    print("none")
else:
    print("none")