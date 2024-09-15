def minion_game(string):
    kevin_score=0
    stuart_score = 0
    lenght= len(string)
    for i in range (lenght):
        
        if string[i] in "AEIOU":
           kevin_score+=(lenght-i)
        else: 
           stuart_score+=(lenght-i)
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")
                
    

if __name__ == '__main__':
    s = input()
    minion_game(s)