numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_left = numbers[:4]
numbers_right = numbers[5::]
quantity = len(numbers)
new_element = (sum(numbers_left) + sum(numbers_right)) / quantity
numbers[4] = new_element

print("Измененный список:", numbers )
