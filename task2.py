try:
    file = open('output.txt', 'r+')
except FileNotFoundError:
    print("No such file or directory")
else:
    context = input('enter the text to enter in file: ')
    file.write(context)
    print('data written to file\n')

    a_context = input('Enter additional data to append in file: ')
    file = open('output.txt', 'a')
    file.write(a_context)
    print('data appended to file\n')

    file = open('output.txt', 'r')
    print("final content of output.txt: ")
    print(file.readline())
    print('\n')
    print(file.readline())

