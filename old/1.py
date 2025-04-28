# f = open("myfile", "a")
# f.writelines(["sadra", "\n"])
# f.writelines(["parmis", "\n"])
# f.write("mehrad ")

f = open("myfile", "r")
for item in f.readlines():
    print(item[:-1])