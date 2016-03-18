import fileinput
filename=r"c.txt"
def process(str):
	return str
for line in fileinput.input(filename):
	print(process(line))