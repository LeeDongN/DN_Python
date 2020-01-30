import random
import string

def create_child(individual1, individual2):
    child = ''
    #if len(individaul1) != len(individual2) follow min
    min_len_ind = min(len(individual1), len(individual2))
    for i in range(min_len_ind):
        if(int(100*random.random())<50):
            child += individual1[i]
        else:
            child += individual2[i]
    return child

#부모는 내가 임의로 짝지음
def create_children(parents, n_child):
    next_population = []
    for i in range(int(len(parents)/2)):
        for j in range(n_child):
            next_population.append(create_child(parents[i], parents[len(parents) - 1 - i]))
    return next_population
