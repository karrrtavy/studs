def supply_menu():
    menu = [
        {'name': 'Борщ', 'price': 35}, 
        {'name': 'Котлета', 'price': 40}, 
        {'name': 'Каша', 'price': 20}, 
        {'name': 'Чай', 'price': 3}
        ]
    return menu

def sort_menu(menu):
    smenu = sorted(menu, key=lambda x: x['price'])
    return smenu

def main():
    menu = supply_menu()
    print('Menu: ')
    for i in menu:
        print(f'{i['name']}: {i['price']}')

    smenu = sort_menu(menu)
    print('Sorted menu: ')
    for i in smenu:
        print(f'{i['name']}: {i['price']}')

if __name__ == '__main__':
    main()