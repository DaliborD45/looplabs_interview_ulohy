left_brackets = ["[", "{", "("]
right_brackets = ["]", "}", ")"]


def are_balanced(str):
    arr = []
    for i in str:
        if i in left_brackets:
            arr.append(i)
        elif i in right_brackets:
            pos = right_brackets.index(i)
            if (len(arr) > 0) and (left_brackets[pos] == arr[len(arr) - 1]):
                arr.pop()
            else:
                return False
    if len(arr) == 0:
        return True


print(are_balanced("{[()]}"))
print(are_balanced("{[(])}"))  # !
print(are_balanced("{{[[(())]]}}"))
print(are_balanced("{[()((]))])}"))  # !
print(are_balanced("{[][]}()(([[[]]{}]))"))