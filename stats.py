import csv
import os

STATS_FILE = "game_stats.csv"

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"wins": 0, "losses": 0, "ties": 0, "games_played": 0}

    with open(STATS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            return {
                "wins": int(row["wins"]),
                "losses": int(row["losses"]),
                "ties": int(row["ties"]),
                "games_played": int(row["games_played"])
            }
    return {"wins": 0, "losses": 0, "ties": 0, "games_played": 0}

def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["wins", "losses", "ties", "games_played"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(stats)

def show_report(stats):
    if stats['games_played'] == 0:
        print("\nยังไม่มีการเล่นเกมเลยครับ\n")
        return

    print("\n=== 🎮 Rock Paper Scissors Game Report 🎮 ===")
    print(f"Total games played: {stats['games_played']}")
    
    # คำนวณเปอร์เซ็นต์
    win_rate = stats['wins'] / stats['games_played'] * 100
    loss_rate = stats['losses'] / stats['games_played'] * 100
    tie_rate = stats['ties'] / stats['games_played'] * 100

    def bar(percent):
        total_blocks = 20
        filled_blocks = int(percent / 100 * total_blocks)
        return "█" * filled_blocks + "░" * (total_blocks - filled_blocks)

    print(f"\n✅ Wins:   {stats['wins']} ({win_rate:.2f}%) {bar(win_rate)}")
    print(f"❌ Losses: {stats['losses']} ({loss_rate:.2f}%) {bar(loss_rate)}")
    print(f"🤝 Ties:   {stats['ties']} ({tie_rate:.2f}%) {bar(tie_rate)}\n")
