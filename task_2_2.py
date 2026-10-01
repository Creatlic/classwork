import random

deck = [f"{v}{s}" for s in "♠♥♦♣" for v in "6789TJQKA"]
random.seed(7)
print("Всего кард в коллоде:", len(deck))

hand = random.sample(deck, 5)
print("Рука игрока:", hand)

print("Карта дня:", random.choice(deck))

weights = {"обычная": 70, "редкая": 25, "легендарная": 5}
loot = random.choices(list(weights), weights=list(weights.values(   )), k=5)
print("Лут:", loot)

random.shuffle(deck)
print("После размешивания:", deck[:6], "...")

print("\n==Раздача 3 игрокам по 5 карт==")
players = ["Алиса", "Борис", "Вера"]
pool = deck.copy()

for p in players:
  player_cards = random.sample(pool, 5)
  for card in player_cards:
    pool.remove(card)
  print(f"{p:6s}: {player_cards}")