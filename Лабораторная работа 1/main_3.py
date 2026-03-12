# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 * 1024 ** 2
pages = 100
lines = 50
elements_on_lines = 25
one_element = 4
book = (pages * lines * elements_on_lines) * 4
quantity_books = round(disk/book)
print("Количество книг, помещающихся на дискету:", quantity_books)
