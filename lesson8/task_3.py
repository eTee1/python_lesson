import random

task3 = [random.randint(0, 99) for _ in range(15)]
print(task3)
# print('чёт', sum(i for i in task3 if i % 2 == 0))
# print('нечет', sum(i for i in task3 if not i % 2 == 0))

print('YES' if (sum(i for i in task3 if i % 2 == 0) < sum(i for i in task3 if not i % 2 == 0)) else 'NO')
