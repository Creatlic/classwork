import sched, time

s = sched.scheduler(time.time, time.sleep)

def say(text):
    print(f"[{time.strftime('%H:%M:%S')}] {text}")

start = time.time()
print("Старт. Отсчёт времени от t0 = 0\n")

s.enter(2, 1, say, ("Прошло 2 секунды(0)",))
s.enter(2, 0, say, ("Прошло 2 секунды(1)",))
s.enter(1, 1, say, ("Прошла 1 секунда",))
s.enterabs(start + 3, 1, say, ("Абсолютное время",))
s.enter(0.5, 1, say, ("Прошло 0.5 секунды",))

print("Очередь до run:", len(s.queue), "задач")

print("\nСодержимое s.queue до запуска:")
for item in s.queue:
    print(item)
print()

print("run блокирует поток, пока все задачи не выполнятся:\n")
s.run()
print("\nГотово. Пустая очередь?", s.empty())