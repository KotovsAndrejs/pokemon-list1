
import csv

pokemons = []

with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])


print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by name")
    print("5. Search by length of name")
    print("6. Print 10 words")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        num = int(input("Enter the sequence number "))
        print(pokemons[num-1])
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        pass
    elif choice == '4':
        name = input("Enter the name ")
        
        results = [x for x in pokemons if name in x]
        print(results)
        pass
    elif choice == '5':
        results = []
        length_word = int(input("Enter the length "))
        for x in pokemons:
            if length_word == len(x):
                results.append(x)
        print(results)
        pass
    elif choice == '6':
        a = 0
        b = 10
        for x  in range(a, b):
            print(pokemons[x])
        while True:
            ans = input("n, q or exit ")
            if ans =='n':
                a = a + 10
                b = b + 10
                for x  in range(a, b):
                    print(pokemons[x])
            if ans =='q':
                a = a - 10
                b = b - 10
                for x  in range(a, b):
                    print(pokemons[x])
            if ans == 'exit':
                break
            pass
    elif choice == '7':
        print("Exiting")
        break

    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
