def minion_game(string):
    score_1 = 0
    score_2 = 0
    for i in range(len(string)):
        if string[i].lower() in 'aeoui':
            score_1 += len(string) - i
        else:
            score_2 += len(string) - i
    
    if score_1 > score_2:
        print('Kevin', score_1)
    elif score_2 > score_1:
        print('Stuart', score_2)
    else:
        print('Draw')
        
if __name__ == '__main__':
    s = input()
    minion_game(s)