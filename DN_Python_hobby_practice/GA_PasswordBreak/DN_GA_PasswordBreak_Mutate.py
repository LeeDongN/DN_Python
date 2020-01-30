import random
import string

def mutate_word(word):
    idx = int(random.random()*len(word))
    if (idx == 0):
        #바꿈
        word = random.choice(string.punctuation + string.ascii_letters
                             + string.digits + string.whitespace)+word[1:]
    else:
        word = word[:idx] + random.choice(string.punctuation + string.ascii_letters
                             + string.digits + string.whitespace) + word[idx+1:]
    return word

#chance_of_mutation(퍼센트)만큼만 돌연변이를 만든다
def mutate_population(population, chance_of_mutation):
    for i in range(len(population)):
        if random.random()*100 < chance_of_mutation:
            population[i] = mutate_word(population[i])
    return population
