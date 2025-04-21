box_size = input("Enter box's size with space-between using sentimetres: ")
box = [int(i) for i in box_size.split(' ') if i.isdigit()]
first_area = box[0] * box[1]
second_area = box[1] * box[2]
third_area = box[2] * box[0]
print(f"First, second and third areas: {first_area, second_area, third_area} sentimetres")

door_size = input("Enter the door's size in sentimetres: ")
door = [int(i) for i in door_size.split(' ') if i.isdigit()]
door_area = door[0] * door[1]
print(f"Door area: {door_area} sentimetres")

def prints():
    print("Yes, the box can enter tho door")

if first_area and second_area and third_area >= door_area:
    print("No, the box can't enter tho door")
elif first_area or second_area and third_area >= door_area:
    prints()
elif second_area or first_area and third_area >= door_area:
    prints()
elif third_area or first_area and second_area >= door_area:
    prints()
else:
    prints()