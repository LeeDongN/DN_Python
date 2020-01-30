import random
import string

password = 'badGirL35'
n_generation = 300
population = 100
best_sample = 20
luckey_few = 20
n_child = 5
chance_of_mutation = 10

pop = generate_population(size = population, min_len = min_len, max_len = max_len)

for g in range(n_generation):
    pop_sorted, pred_len = compute_performance(population = pop, password = password)
    
    if int(pop_sorted[0][1]) == 100:
        print('SUCCESS! The password is %%s'%(pop_sorted[0][0]))
        break
    
    survivors = select_survivors(pop_sorted, pred_len, best_sample, lucky_few)
    
    children = create_children(parents = survivors, n_child)
    
    new_generation = mutate_population(population = children, chance_of_mutation)
    
    pop = new_generation
    
    print('=====%sth Generation ====='%(g+1))
    print(pop_sorted[0])