fileName=input()
if '.' in fileName:
    i=fileName.index('.')
    extension=fileName[i+1:]
    if extension=="py":
        print("The extension of the file is :")
        print("python")
    elif extension=="c":
        print("The extension of the file is :")
        print("C language")
    elif extension=="java":
        print("The extension of the file is :")
        print("java")
    elif extension=="cc":
        print("The extension of the file is :")
        print("C++ language")
    else:
        print("some other language")
else:
    print("INVALID INPUT")
