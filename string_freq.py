import operator
input_string= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return sorted(d.items(),key=operator.itemgetter(1),reverse=True)

print(*most_frequent(input_string))

