from collections import deque

def names_list():
    names = deque(['John', 'Oscar', 'Faith'])
    names.append('Eric')
    names.append('David')
    names.popleft()
    names = set(names)
    names.pop()
    return names

# Call the function and print its result
print(names_list())
