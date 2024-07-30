def main():
    filename = 'text.txt'
    line = readFile(filename)
    char = [char for char in line.strip() if char.isdigit()]
    print(char)
    

def readFile(fn):
    with open(fn, 'r') as file:
        lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
	main()