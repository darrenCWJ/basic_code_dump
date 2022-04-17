from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

a = [1,2,3]
b = [1,3]

print(list(product(a,b))) # [(1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 3)]

print(list(product(a,b, repeat = 2))) #[(1, 1, 1, 1), (1, 1, 1, 3), (1, 1, 2, 1), (1, 1, 2, 3), (1, 1, 3, 1), (1, 1, 3, 3), (1, 3, 1, 1), (1, 3, 1, 3), (1, 3, 2, 1), (1, 3, 2, 3), (1, 3, 3, 1), (1, 3, 3, 3), (2, 1, 1, 1), (2, 1, 1, 3), (2, 1, 2, 1), (2, 1, 2, 3), (2, 1, 3, 1), (2, 1, 3, 3), (2, 3, 1, 1), (2, 3, 1, 3), (2, 3, 2, 1), (2, 3, 2, 3), (2, 3, 3, 1), (2, 3, 3, 3), (3, 1, 1, 1), (3, 1, 1, 3), (3, 1, 2, 1), (3, 1, 2, 3), (3, 1, 3, 1), (3, 1, 3, 3), (3, 3, 1, 1), (3, 3, 1, 3), (3, 3, 2, 1), (3, 3, 2, 3), (3, 3, 3, 1), (3, 3, 3, 3)]

perm = permutations(a)

print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


perm = permutations(a,2)
 
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

comb = combinations(a, 2)

print(list(comb)) #[(1, 2), (1, 3), (2, 3)]

comb_w_r = combinations_with_replacement(a, 2)

print(list(comb_w_r)) #[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


acc = accumulate(a)
print(list(acc)) #[1, 3, 6] , 1, 1+2, 1+2+3

acc2 = accumulate(a, func = operator.mul)
print(list(acc2))  #[1, 2, 6]

a = [1,2,3,4]

def smaller_thn_3(x):
    return x<3

group_obj = groupby(a,key = smaller_thn_3)

for k,v in group_obj:
    print(k, list(v))

# True [1, 2]
# False [3, 4]


# group_obj = groupby(b, key= lambda x: x["value_to_group"])  # for dictionaries grouping

for i in count(10):
    print(i) # starts from 10 to inf
    if i == 15:
        break
    
a = [1,2,3]
summa = 0
for i in cycle(a):
    print(i)
    summa += i
    if summa > 45:
        break

summa = 0
for i in repeat(1):
    print(i)
    summa += i
    if summa > 45:
        break



