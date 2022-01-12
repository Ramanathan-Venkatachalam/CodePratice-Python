#SumofEvens

sum_of_evens = 0
for number in range(0, 101, 2):
  sum_of_evens = sum_of_evens + number
print(sum_of_evens)

sum_of_evens1 = 0
for number in range(0, 101):
    if number % 2 == 0:
        sum_of_evens1 = sum_of_evens1 + number
print(sum_of_evens1)