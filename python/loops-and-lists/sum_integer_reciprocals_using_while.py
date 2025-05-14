#summation = 0
#starting_index = 1
#index = starting_index
#maximum_index = 100
#
#while index < maximum_index:
#    summation += 1 / index
#
#print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')


summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index <= maximum_index:
    summation += 1 / index
    index += 1

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

#3 errors
#index should be <= max, not =... there isn't an index variable... because it isn't constrained, the loop never ends

#pt 2
#intermediate results hand solved(guesstimated): ~5.17

#LMM answer
#It looks like you're trying to compute the sum of the harmonic series from k = 1 to k = 100.
#The issue in your script is that the condition in the while loop while index < maximum_index: will stop the loop before reaching the value of 100.
#The reason is that index only goes from 1 to 99 and doesn't include 100.

def harmonic_sum(max_k):
    summation = 0
    index = 1
    while index <= max_k:
        summation += 1 / index
        index += 1
    return summation

max_k_3 = 3
sum_3 = harmonic_sum(max_k_3)
print(f"Sum for k[max] = {max_k_3}: {sum_3}")

max_k_100 = 100
sum_100 = harmonic_sum(max_k_100)
print(f"Sum for k[max] = {max_k_100}: {sum_100}")