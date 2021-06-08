name = input('insert a name: ')
print('Hi', name)

age = int(input('insert your age: '))
print('you are ',age,' years old')

if age < 18 :
    print(name, 'you are under age!')
else:
    print(name, 'welcome')

height = int(input('enter your height: '))
weight = int(input('enter your weight: '))

if height-weight < 100:
    print(name, 'you are overweight')
elif height - weight >120:
    print(name, 'you are too light')
else:
    print(name+' your height is :',height, ',weight is :',weight)