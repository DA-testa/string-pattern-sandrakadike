# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    choice = input().rstrip()
    if choice == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif choice == "F":
        with open(f"tests/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = len(pattern)
    t = len(text)
    result = []

    for i in range(t - p + 1):
        if pattern == text[i:i+p]:
            result.append(i)

    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

