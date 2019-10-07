


def fibs(num):
result = [0, 1]
for i in range(num-2):
result.append(result[-2] + result[-1])
return result


def peek_sum(x, y):
print 'Adding', x, 'and', y
return x + y



name = input ("podaj liczbe = ")
fibs (name)

reduce(peek_sum, [1, 2, 3, 4, 5])