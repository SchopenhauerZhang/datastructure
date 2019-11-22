import subprocess
import sys

def init():
	try:
		subprocess.call("python --version", shell = True)
	except Exception:
		exit("sorry ,your python env is not available")

def get():
    total_line = 3
    i = 0
    input_data = []
    # 读取所有输入（共有3行）放入list
    while i < 3:
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        input_data.append(values)
        i += 1
    
    search_data = input_data.pop().pop()
    origin_data = input_data.pop()
    length = input_data.pop().pop()
    print(search_data, ":", origin_data, ":", length)
    if search_data not in origin_data:
        print(-1)
        exit()
    index = 0
    while length > 0:
        length -= 1
        pop_data = origin_data.pop()
        if pop_data == search_data:
            index = length
    
    print(index)
    exit()

def get_character_distance():
    # read input date
    line = sys.stdin.readline().strip()
    # get length of input data(characters and spcace and something else)
    input_line_length = len(line)
    characters = line.split(" ")
    character_length = 0
    
    for i in characters:
        character_length += len(i)
        if "\\n" in i:
            character_length = character_length - 2
            
    # get the result
    print(input_line_length - character_length)
    exit()
