#Current status: Phase 1, Day 1 — not started yet. Your task is the 5 functions (my_sum, my_count, my_max, my_min, my_average). Test list: [4, 7, 2, 9, 1]. No built-ins allowed.

def my_sum(n):
    sum=0
    for i in n:
        sum +=i
    return sum

def my_count(n):
    count=0
    for i in n:
        count=count+1
    return count

def my_max(n):
    max=n[0]
    for i in n:
        if i > max:
            max=i
    return max

def my_min(n):
    min=n[0]
    for i in n:
        if i < min:
            min=i
    return min

def my_avg(n):
       return my_sum(n) / my_count(n)

Numbers=[4, 7, 2, 9, 1]
Numbers = [4, 7, 2, 9, 1]
print(my_sum(Numbers))
print(my_count(Numbers))
print(my_max(Numbers))
print(my_min(Numbers))
print(my_avg(Numbers))