# class IteratorRange1:
#     def __init__(self, stop, start=0, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __next__(self):
#         if self.start < self.stop:
#             self.start += self.step
#             return self.start
#         else:
#             raise StopIteration
#
#
# s_iter1 = IteratorRange1(10, 5, 3)
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))

# class GeneratorRange1:
#     def __init__(self, stop, start=0, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step

def simple_generator(stop, start=0, step=1):
    while start < stop:
        start += step
        yield start



s_gener1 = simple_generator(10, 5, 3)

print(next(s_gener1))
print(next(s_gener1))
print(next(s_gener1))
print(next(s_gener1))
print(next(s_gener1))
print(next(s_gener1))


