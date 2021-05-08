fileName=input()
Dict={"py":"python","c":"C","cc":"C++","jsp":"Java","html":"HTML","pl":"Perl","php":"PHP"}
if '.' in fileName:
    i=fileName.index('.')
    extension=fileName[i+1:]
    print("The extension of the file is :")
    print(Dict[extension])
else:
    print("INVALID INPUT")
