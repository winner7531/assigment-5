try:
    file = open('sample.txt', 'r')

except FileNotFoundError:
    print('File not found. Please make one')
else:
    print("Reading file contents. \nLine1: ")
    first_lne = file.readline()
    print(first_lne)
    print("Line2: ")
    print(file.readline())
    print("Line3: ")
    print(file.readline())
    print("Line4: ")
    print(file.readline())
    print("Line5: ")
    print(file.readline())
finally:
    file.close()