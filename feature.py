eng2uz = {
    "one": 'bir',
    'two': 'ikki',
    'three': 'uch',
    'four': 'tort'
}
one = input("Translate: ")
if one == "one":
    print("result: ", eng2uz['one'])
else:
    print('invalid')

# below is to check if certain key is inside of dictionary
print('one' in eng2uz)

# below is the check if certain value is insde of dictionary

valve = eng2uz.values()
print('uch' in valve)

final_marks = {
    'CSF': 75,
    'FUNPRO': 80,
    'IMOB': 57,
    'ISDS': 63
}

option = input("Choose Modules: ").upper()

if option == 'CSF':
    print(final_marks['CSF'])
elif option == 'FUNPRO':
    print(final_marks['FUNPRO'])
elif option == 'IMOB':
    print(final_marks['IMOB'])
elif option == 'ISDS':
    print(final_marks['ISDS'])

average = input(f"Calculate average of all modules?\nY(yes) or N(no): ").upper()

if average == 'Y':
    total = sum(final_marks.values()) / len(final_marks)
    print(total)
elif average == 'N':
    pass
else:
    print("Invalid Value")


h = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(h.get('f', 0))

csf = {
    'cw1_weight': 0.4,
    'cw1_mark': 79,
    'exam_weight': 0.6,
    'exam_mark': 65
}
a = csf.get('cw1_mark') * csf['cw1_weight']
b = csf['exam_mark'] * csf['exam_weight']
c = a + b
d = c / len(csf)
print(f"Final mark: {d}")


#this is how to create a tuple with a single element
#with brackets it is going to be a string not a tuple
#for a tuple it is not must to have brackets
t1 = 2, 3, 4, 7
print(type(t1))
#type tuple.

t2 = 'work'
print(tuple(t2))

print((1, 123, 4) < (1, 2, 4))

print((14555, 10, 'Samarkand')<(15775, 19, 'Tashkent'))

a, b, c = 1, 2, 3
print(a + b + c)

email = 'james@gamil.com'

username, gmail = email.split('@')
print(username, gmail)

try:
    one = int(input("1: "))
    two = int(input("2: "))

    def cal(one, two):
        calcul = one//two
        return calcul


    print("division: ", cal(one, two))
except ValueError:
    print("Invalid input")


result = divmod(10, 3)
print(result)


def write(*work):
    print(work)


write(1, 2, 56, 'work')

dad = 'good'
mom = [1, 2, 3, 4]
me = zip(dad, mom)
# print(list(me))
for wire in me:
    print(wire)

print('\n')

for index, word in enumerate('abs', 0):
    print(index, word)
print('\n')

my_tuple = ('a', 'b', 'c', 'd', 'e')
for i in enumerate(my_tuple):
 print(i)

print('\n')

for work, yea in enumerate("job"):
    print(work, yea)

print(dict(zip('WOK', range(3))))

print(dict())

d = {'d': 1, 'b': 2, 'c': 3}

t = d.items()
print(t)

wok = [('c', 1), ('g', 2), ('f', 3)]
print(dict(wok))

jj = 1, 2, 4, 5, 6, 7
kk = 'absdefg'

print(list(zip(kk, jj)))

meme = {'name': 'Mike', 'work': 'Logistics', 'status': 'single'}

for kaggle, value in meme.items():
    print(kaggle, value)

def add(a = 0, b= 0, c= 0):
    sum = a + b + c
    print(f'Sum: {sum}')
add()



