inputsentence = ""
outputsentence = ""
input_path = "c99pros.txt"
output_path = "c99prod.txt"
def read(path):
    file = open(path,"r")
    inputsentence = file.read()
    file.close()
def write(path):
    file = open(path,"w")
    if path == input_path:
        file.write(outputsentence)
    else:
        file.write(inputsentence)
    file.close()
#read 1st file
read(input_path)
#read 2nd file
read(output_path)
#write 1st file
write(input_path)
#write 2nd file
write(output_path)
