#Sample code to change a character at a given index and print the modified string
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character;
    string = ''.join(l);
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
