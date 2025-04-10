
# step 1 taking the user input
user_input = input("Enter some data to write to the file: ")
# step 2 writing the input to the file
with open('e:\python data science\module3assigment\python-task\modulle5\output.txt', 'w') as file:
    file.write(user_input + '\n')
# step 3 appending additional data to the file
# with open('e:\python data science\module3assigment\python-task\modulle5\output.txt', 'a') as file:
add_data = input("Enter additional data to append to the file: ")
with open('e:\python data science\module3assigment\python-task\modulle5\output.txt', 'a') as file:
    file.write(add_data + '\n')
                        

  # step 4 reading and displaying the final content of the file


try:
    
    with open('e:\python data science\module3assigment\python-task\modulle5\output.txt', 'r') as file:
        print("Final content of the file:")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'output.txt' does not exist.")
