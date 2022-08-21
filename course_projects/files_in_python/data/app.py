my_file = open("data.txt", "r")
file_content = my_file.read()
my_file.close()


print(file_content)

my_file_writing = open("data.txt", "w")
my_file_writing.write("Hey there! This was written by python!")
my_file.close()