import random
import string

def fitness(password, test_word):
    score = 0
    
    if len(password) != len(test_word):
        return score
    
    #if fit length, give score 0.5
    else:
        len_score = 0.5
        score += len_score
        
        for i in range(len(password)):
            if password[i] == test_word[i]:
                score += 1
     
    #백점 만점에 몇점?
    return score/(len(password) + len_score)*100
