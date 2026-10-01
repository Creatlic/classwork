import random

random.seed(42)
print("random()             :", round(random.random(), 6))
print("uniform(1, 10)       :", round(random.uniform(1,10), 3))
print("radint(1,6)          :", random.randint(1,6))
print("randrange(0,100,5    :", random.randrange(0,100,5))

print("\n==Бросок кубиков 5 раз==")
for i in range(1,6):
    a, b = random.randint(1,6), random.randint(1,6)
    print(f"Бросок {i}: {a}+{b} = {a+b}")

print("\n==Статистика на 10 000 бросков одного кубика==")
random.seed(2026)
counts = {i: 0 for i in range(1,7)}
n = 10_000
for _ in range(n):
    counts[random.randint(1,6)] += 1
for face, cnt in sorted(counts.items()):
    bar = "#" * (cnt//50)
    print(f"{face}: {cnt:5d}    ({cnt/n*100:5.2f}%)     {bar}")
print("\n==Статистика на 100 000 бросков трех кубиков==")
sum_counts = {i: 0 for i in range(1,19)} #мин.сумма = 3, макс.сумма = 18
n = 100_000
for _ in range(n):
    dices = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    sum_counts[dices] += 1

most_common = max(sum_counts, key=sum_counts.get)
count = sum_counts[most_common]

print("\n==Распределение сумм==")
for face, cnt in sorted(sum_counts.items()):
    bar = "#" * (cnt // 250) 
    print(f"{face:2d}: {cnt:5d}    ({cnt/n*100:5.2f}%)     {bar}")
print(f"Чаще выпадает сумма: {most_common}")