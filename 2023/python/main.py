def main():
    filename = 'text.txt'
    val = readFile(filename)
    print(val)

def readFile(fn):
    with open(fn, 'r') as file:
        content = file.read().split()
    return content

if __name__ == "__main__":
	main()