def FixGif(file_path):
  data = ""
  with open(file_path, "r") as input_file:
    data = input_file.read()

  data = data.upper()

  gif_list = []
  start = 0
  while start < len(data):
    end = start
    while end < len(data) and data[end] != ' ':
      end += 1
    string = data[start:end]
    x = string.find('x')
    comma = string.find(',')
    gif_list.append(string[x + 1 : comma])
    start = end + 1

  data = " ".join(gif_list)

  pos = file_path.find(".txt")
  if pos == -1:
    pos = len(file_path)
  new_file_path = file_path[ : pos] + "_fix.gif"

  with open(new_file_path, "w+") as output_file:
    output_file.write(data)

FixGif("giftext.txt")
