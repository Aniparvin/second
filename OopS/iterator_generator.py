# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# n = int(input("Enter how many terms: "))

# for num in fibonacci(n):
#     print(num, end=" ")
# print("\n")

# #2
# class EvenNums:
#     def __init__(self, start):
#         # Ensure start is even
#         self.num = start if start % 2 == 0 else start + 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.num > 100:   # stop condition
#             raise StopIteration
#         current = self.num
#         self.num += 2
#         return current


# even_numbers = EvenNums(0)

# for n in even_numbers:
#     print(n)
# print("\n")


#3
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
items = [10, 20, 30, 40]

for x in ReverseIterator(items):
    print(x, end = " , ")



