def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 "+c1[-10:-5]+" "+c1[-5:] for c1 in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)