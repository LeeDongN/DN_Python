import random
import string

#비밀번호 설정과 최대 길이, 최소 길이 설정(컴퓨터가 맞춰야 함.)
password = 'badgirl35'
min_len = 3
max_len = 12
n_generation = 300
population = 100
best_sample = 20
luckey_few = 20
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

