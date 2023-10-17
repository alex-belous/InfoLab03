base_string = input("Введите строку: ")
required_fragment = input("Введите образец поиска: ")

if (len(base_string) == 0 or len(required_fragment) == 0):

    input("\nСтрока или образец поиска пусты\n")

elif (len(base_string) < len(required_fragment)):

    input("\nКол-во символов в строке меньше кол-ва символов в образце поиска\n")

else:

    matches_count = 0
    matches_indexes = []
    matches_unique_indexes_set = []

    matching_symbol = "\033[32mV\033[0m"

    print(f"\nСтрока, по которой будет происходить поиск:\n[{base_string}] [кол-во символов: {len(base_string)}]")
    print(f"Образец поиска:\n[{required_fragment}] [кол-во символов: {len(required_fragment)}]")
    print(f"Кол-во шагов поиска: {((len(base_string) - len(required_fragment)) + 1)}")

    for i in range(0, (len(base_string) - len(required_fragment)) + 1):
        if base_string[i:i + len(required_fragment)] == required_fragment:
            matches_count += 1
            print(f"\n   Образец поиска найден в строке (Совпадение номер {matches_count})")

            print("   Совпадение: [", end="")
            for f in range(0, i):
                print("-", end="")
            for g in range(i, i + len(required_fragment)):
                print(matching_symbol, end="")
                matches_unique_indexes_set.append(g)
            for h in range(i + len(required_fragment), len(base_string)):
                print("?", end="")
            if (len(required_fragment) != 1):
                print(
                    f"] с позиции {i + 1} по позицию {i + len(required_fragment)} [В виде вызова по индексам: [{i}:{i + len(required_fragment)}]]")
                matches_indexes.append([i, i + len(required_fragment)])
            else:
                print(f"] на позиции {i + 1} [В виде вызова по индексу: [{i}]]")
                matches_indexes.append([i])

            print(
                f"   Строка:     [{base_string}] [Проверено {((i + len(required_fragment)) * 100 // len(base_string))} % строки]")

    print(f"\nСтрока полностью проверена:")
    print("[", end="")
    for i in range(0, len(base_string)):
        matched = False
        for f in matches_unique_indexes_set:

            if i == f:
                print(matching_symbol, end="")
                matched = True
                break
        if not matched:
            print("-", end="")
    print("]")
    print(f"[{base_string}]")

    if (matches_count > 0):
        print(f"\nОбразец поиска встречается в строке. Кол-во совпадений: {matches_count}\n")
        for i in range(0, len(matches_indexes)):
            if len(required_fragment) > 1:
                print(f"   Совпадение {i + 1}: [{matches_indexes[i][0]}:{matches_indexes[i][1]}]")
            else:
                print(f"   Совпадение {i + 1}: [{matches_indexes[i][0]}]")
        input()
    else:
        input(f"\nОбразец поиска не встречается в строке\n")
