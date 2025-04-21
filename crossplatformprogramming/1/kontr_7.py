money = int(input("Push your cash. Value of your cash: "))
razmen = [500, 100, 10, 2]

if money % 2 == 0:
    for i in razmen:
        if money >= i:
            print(f"{int(money / i)}x{i}")
            while money > i:
                money -= i
else:
    print("No way")
