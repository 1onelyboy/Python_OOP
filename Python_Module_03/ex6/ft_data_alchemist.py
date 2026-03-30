import random


def main() -> None:
    players = [
        'Alice', 'bob', 'Charlie',
        'dylan', 'Emma', 'Gregory',
        'john', 'kevin', 'Liam'
    ]

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")

    all_capitalized_names = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized_names}")

    capitalized_names_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_names_only}")

    scores = {name: random.randint(50, 1000) for name in all_capitalized_names}
    print(f"\nScore dict: {scores}")

    total = [scores[name] for name in scores]
    average_score = sum(total) / len(scores) if scores else 0
    print(f"Score average is {round(average_score, 2)}")

    high_scores = {
        name: scores[name] for name in scores
        if scores[name] > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
