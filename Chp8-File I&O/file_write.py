st = "this is program written with python"

f = open("../Chp8-File I&O/myfile.txt", "w")  # The open() function is used to open a file in Python. The first argument is the name of the file, and the second argument is the mode in which we want to open the file. In this case, we are opening the file in write mode ("w"), which allows us to write to the file. If the file already exists, it will be overwritten. If the file does not exist, it will be created.

f.write(st) # The write() method is used to write a string to the file. It takes a string as an argument and writes it to the file. If you want to write multiple lines to the file, you can use the writelines() method, which takes a list of strings as an argument and writes them to the file.

f.close() # It is important to close the file after we are done with it to free up system resources and avoid potential issues with file locks or data corruption.