# * Реализовать класс который принимает информацию о пользователе и возвращает эту информацию.


# class Human:
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def get_info(self):
#         print(self.name)
#         print(self.surname)
#         print(self.age)
#
# human_x = Human('asdas', 'jdjjd', 60)
#
#
# human_x.get_info()


#
#
# * Реализовать класс калькулятор.
# Конструктор принимает на вход три параметра:
# первое число, второе число и операцию которую нужно выполнить надо ними.
# Так же есть один метод который возвращает результат.
# Арифметические операции вынести в отдельные функции.
#

# class Calculator:
#
#     def __init__(self, num_1, num_2, operation):
#         self.num_1 = int(num_1)
#         self.num_2 = int(num_2)
#         self.operation = operation
#
#
#     def sum(self):
#         return int(self.num_1) + int(self.num_2)
#
#
#     def differ(self):
#         return int(self.num_1) - int(self.num_2)
#
#
#     def division(self):
#         return int(self.num_1) / int(self.num_2)
#
#
#     def multipli(self):
#         return int(self.num_1) * int(self.num_2)
#
#     def rezult(self):
#         if self.operation == '+':
#             return self.sum()
#         elif self.operation == '-':
#             return self.differ()
#         elif self.operation == '*':
#             return self.multipli()
#         elif self.operation == '/':
#             return self.division()
#         else:
#             return 'Данная операция не поддерживается'
#
#
# example_1 = Calculator(2222, 323232, '*')
#
#
# print(example_1.rezult())



# * Реализовать класс "журнал/справочник".
# В классе есть атрибут класса типа список, в него складываются все добавленные люди.
# Реализовать метод проверки на то что такой человек уже есть в списке и метод добавления.


#
# class Human:
#     list_person = []
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#
#     def convert_to_dict(self):
#         return {"name": self.name, "surname": self.surname, "age": self.age}
#
#
#     def check_and_add_to_list(self):
#         duplicated = 0
#         person_dict = self.convert_to_dict()
#         for i in self.list_person:
#             if i['name'] == person_dict.get('name') and i['surname'] == person_dict.get('surname') and i['age'] == person_dict.get('age'):
#                 duplicated += 1
#         if not duplicated:
#             Human.list_person.append(person_dict)
#
#
# human1 = Human("Ivan", "Ivan", 32)
# human2 = Human("Ivan", "Ivan", 32)
# human3 = Human("Petr", "Petr", 24)
# human4 = Human("Petr", "Petr", 24)
# human5 = Human("Petr", "Petr", 24)
#
# #
# #
#
# human1.check_and_add_to_list()
# human2.check_and_add_to_list()
# human3.check_and_add_to_list()
# human4.check_and_add_to_list()
# human5.check_and_add_to_list()
# # human21.check_and_add_to_list()
# # human3.check_and_add_to_list()
# # human4.check_and_add_to_list()
# # human5.check_and_add_to_list()
# print(Human.list_person)




# Второй вариант сделать через словарь и уникальный ключ.


# class Human:
#     list_person = []
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#
#
#
#     def convert_to_dict(self):
#         key = self.name, self.surname, self.age
#         return {"key": key, "name": self.name, "surname": self.surname, "age": self.age}
#
#
#
#
#     def check_and_add_to_list(self):
#         duplicated = 0
#         person_dict = self.convert_to_dict()
#         for i in self.list_person:
#             if i['key'] == person_dict.get('key'):
#                 duplicated += 1
#         if not duplicated:
#             Human.list_person.append(person_dict)
#
#
# human1 = Human("Ivan", "Ivan", 32)
# human2 = Human("Ivan", "Ivan", 32)
# human3 = Human("Petr", "Petr", 24)
# human4 = Human("Petr", "Petr", 24)
# human5 = Human("Petr", "Petr", 24)
#
#
#
# human1.check_and_add_to_list()
# human2.check_and_add_to_list()
# human3.check_and_add_to_list()
# human4.check_and_add_to_list()
# human5.check_and_add_to_list()
# # human21.check_and_add_to_list()
# # human3.check_and_add_to_list()
# # human4.check_and_add_to_list()
# # human5.check_and_add_to_list()
# print(Human.list_person)

# Создать класс "Матрица". Класс должен иметь следующие поля:
# Или двумерный массив вещественных чисел;
# Или количество строк и столбцов в матрице.


class Matrix:
    cort_line = []
    gen_cort = []
    def __init__(self, matrix_1, matrix_2, operation):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
        self.operation = operation



    def sum_matrix(self):


        if len(self.matrix_1) == len(self.matrix_2) and len(self.matrix_1[0]) == len(self.matrix_2[0]):
            for line in range(len(self.matrix_1)):
                print(len(self.matrix_1))

                for column in range(len(self.matrix_1[line])):
                    element_matrix = ((self.matrix_1[line])[column]) + ((self.matrix_2[line])[column])
                    Matrix.cort_line.append(element_matrix)
                    print(Matrix.cort_line)
                Matrix.gen_cort.append(Matrix.cort_line)
                Matrix.cort_line = []
            return Matrix.gen_cort


        else: return ('операция с матрицами не возможна')

    def mult_matrix(self):


        if len(self.matrix_1) == len(self.matrix_2) and len(self.matrix_1[0]) == len(self.matrix_2[0]):
            for line in range(len(self.matrix_1)):
                print(len(self.matrix_1))

                for column in range(len(self.matrix_1[line])):
                    element_matrix = ((self.matrix_1[line])[column]) * ((self.matrix_2[line])[column])
                    Matrix.cort_line.append(element_matrix)
                    print(Matrix.cort_line)
                Matrix.gen_cort.append(Matrix.cort_line)
                Matrix.cort_line = []
            return Matrix.gen_cort


        else: return ('операция с матрицами не возможна')

    def print_matrix(self):
        print(self.matrix_1)



    def mult_matrix_by_number(self):


            for line in range(len(self.matrix_1)):
                print(len(self.matrix_1))

                for column in range(len(self.matrix_1[line])):
                    element_matrix = ((self.matrix_1[line])[column]) * int(self.matrix_2)
                    Matrix.cort_line.append(element_matrix)
                    print(Matrix.cort_line)
                Matrix.gen_cort.append(Matrix.cort_line)
                Matrix.cort_line = []
            return Matrix.gen_cort



    def rezult(self):
            if self.operation == '+':
                return self.sum_matrix()
            elif self.operation == 'print':
                return self.print_matrix()
            elif self.operation == '*':
                return self.mult_matrix()
            elif self.operation == 'multiply by number':
                return self.mult_matrix_by_number()
            else:
                return 'Данная операция не поддерживается'






matrix_11 = [[1, 2, 3], [2, 3, 4], [2, 9, 5]]
matrix_21 = [[1, 2, 3], [2, 3, 4], [2, 9, 5]]

operation_1 = Matrix(matrix_11, matrix_21, 'print')


print(operation_1.rezult())
#
# Класс должен иметь следующие методы:
# 1) сложение с другой матрицей;
# 2) умножение на число;
# 3) вывод на печать;
# 4) умножение матриц.