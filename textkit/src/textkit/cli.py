from .stats import char_stats, word_count

def main():
    t = "Привет, мир! Это мой первый пакет."
    print("Слов:", word_count(t), "| Статистика:", char_stats(t))

if __name__ == "__main__":
    main()