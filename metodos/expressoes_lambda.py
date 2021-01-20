# def square(num):
#     result = num ** 2
#     return result
# print(square(16))

#agora como lambda


square = lambda num: num ** 2
print(square(2))

par = lambda x: x % 2 == 0
print(par(3))

inverter_string = lambda s: s[::-1]
print(inverter_string('pedro'))

