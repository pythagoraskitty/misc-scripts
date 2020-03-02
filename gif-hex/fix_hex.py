def FixHex(file_path):
  data = ""
  with open(file_path, "r") as input_file:
    data = input_file.read()

  data = data.lower()

  hex_list = []
  start = 0
  while start < len(data):
    end = start
    while end < len(data) and data[end] != ' ':
      end += 1
    hex_list.append(data[start:end])
    start = end + 1

  hex_list = ["0x" + item for item in hex_list]
  data = ", ".join(hex_list)

  pos = file_path.find(".txt")
  if pos == -1:
    pos = len(file_path)
  new_file_path = file_path[ : pos] + "_fix.txt"

  with open(new_file_path, "w+") as output_file:
    output_file.write(data)

FixHex("hex.txt")
