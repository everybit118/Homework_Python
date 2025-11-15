print ("Example 1")
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
else:
    # сортируем по алфавит
    boys.sort(key=str.lower)
    girls.sort(key=str.lower)

    print("Идеальные пары:")
    for i in range(len(boys)):
        print(boys[i], "и", girls[i])

print ()
print ("Example 2")
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
else:
    boys.sort(key=str.lower)
    girls.sort(key=str.lower)

    print("Идеальные пары:")
    for i in range(len(boys)):
        print(boys[i], "и", girls[i])
