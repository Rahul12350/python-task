try:
    # Open the file in read mode
    with open('e:\python data science\module3assigment\python-task\modulle5\samplefile.txt', 'r') as file:
        # Read and print each line
        for line in file:
            print(line.strip())
            #line=file.readline()
            
except FileNotFoundError: 
    print("Error: The file 'sample.txt' does not exist.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")