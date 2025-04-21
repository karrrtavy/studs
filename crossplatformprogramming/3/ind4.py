# Инициализация словаря цветов
color_dict = {
    'red': 'красный',
    'blue': 'синий',
    'green': 'зеленый',
    'yellow': 'желтый',
    'orange': 'оранжевый',
    'indigo': 'темно-синий',
    'violet': 'фиолетовый',
    'black': 'черный',
    'white': 'белый',
    'gray': 'серый'
}
print("Весь словарь:")
for key, value in color_dict.items():
    print(f"{key}: {value}")
last_key = list(color_dict.keys())[-1]
print(f"Перевод последнего слова '{last_key}': {color_dict[last_key]}")
del color_dict['red']
print(f"Слово 'red' удалено из словаря.")
print("Словарь после удаления:")
for key, value in color_dict.items():
    print(f"{key}: {value}")
