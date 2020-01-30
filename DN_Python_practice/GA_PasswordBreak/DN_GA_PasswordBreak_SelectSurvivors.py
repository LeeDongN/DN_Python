import random
import string

#생성된 값의 점수를 list에 저장, password의 길이 저장
def compute_performance(population, password):
    performance_list = []
    for individual in population:
        score = fitness(password, individual)
        
        #we can predict length of password
        if score > 0:
            pred_len = len(individual)
        performance_list.append([individual, score])
        
    #To sort list on score & reverse
    population_sorted = sorted(performance_list, key = lambda x:x[1], reverse = True)
    return population_sorted, pred_len

def select_survivors(population_sorted, pred_len, best_sample, lucky_few):
    next_generation = []
    
    for i in range(best_sample):
        if population_sorted[i][1]>0:
            next_generation.append(population_sorted[i][0])
            
    lucky_survivors = random.sample(population_sorted, k = lucky_few)
    for l in lucky_survivors:
        next_generation.append(l[0])
    
    #generate new population if next_generation is too small
    if len(next_generation)<best_sample + lucky_few:
        next_generation.append(generate_word(length = pred_len))
        
    random.shuffle(next_generation)
    return next_generation
