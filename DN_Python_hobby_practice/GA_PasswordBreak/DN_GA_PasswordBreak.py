import random
import string

#비밀번호 설정과 최대 길이, 최소 길이 설정(컴퓨터가 맞춰야 함.)
password = 'badg!irl#35'
min_len = 3
max_len = 12
n_generation = 500
population = 100
best_sample = 20
lucky_few = 20
n_child = 5
chance_of_mutation = 10

#length에 맞춰 랜덤하게 숫자와 문자 생성
def generate_word(length):
    result =''
    x = ''.join(random.sample(string.punctuation + string.whitespace + string.ascii_letters + string.digits, k = length))
    return x

#generate population
def generate_population(size, min_len, max_len):
    population = []
    for i in range(size):
        #generate words with balanced length
        length = i%(max_len - min_len +1) + min_len
        population.append(generate_word(length))
    return population

def mutate_word(word):
    idx = int(random.random()*len(word))
    if (idx == 0):
        word = random.choice(string.punctuation + string.whitespace + string.ascii_letters + string.digits)+word[1:]
    else:
        word = word[:idx] + random.choice(string.punctuation + string.whitespace + string.ascii_letters + string.digits)+word[idx+1:]
    return word

#chance_of_mutation(퍼센트)만큼만 돌연변이를 만든다
def mutate_population(population, chance_of_mutation):
    for i in range(len(population)):
        if random.random()*100 < chance_of_mutation:
            population[i] = mutate_word(population[i])
    return population

def create_child(individual1, individual2):
    child =''
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

def select_survivors(population_sorted, best_sample, lucky_few, password_len):
    next_generation = []
    
    for i in range(best_sample):
        if population_sorted[i][1]>0:
            next_generation.append(population_sorted[i][0])
            
    lucky_survivors = random.sample(population_sorted, k = lucky_few)
    for l in lucky_survivors:
        next_generation.append(l[0])
    
    #generate new population if next_generation is too small
    if len(next_generation)<best_sample + lucky_few:
        next_generation.append(generate_word(length = password_len))
        
    random.shuffle(next_generation)
    return next_generation

def fitness(password, test_word):
    score = 0
    
    if len(password) != len(test_word):
        return score
    
    #if fit length, give score 0.5
    len_score = 0.5
    score += len_score
        
    for i in range(len(password)):
        if password[i] == test_word[i]:
            score += 1
     
    #백점 만점에 몇점?
    return score/(len(password) + len_score)*100


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
        print('SUCCESS! The password is %s'%(pop_sorted[0][0]))
        break
    
    survivors = select_survivors(pop_sorted, best_sample, lucky_few, pred_len)
    
    children = create_children(parents = survivors, n_child = n_child)
    
    new_generation = mutate_population(population = children, chance_of_mutation = chance_of_mutation)
    
    pop = new_generation
    
    print('=====%sth Generation ====='%(g+1))
    print(pop_sorted[0])