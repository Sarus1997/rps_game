from stats import load_stats, show_report
from game import play_game

def main_menu():
    while True:
        print("\n=== Rock Paper Scissors Game ===")
        print("1. เล่นเกม")
        print("2. ดูสถิติการเล่น")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกตัวเลือก: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            stats = load_stats()
            show_report(stats)
        elif choice == "3":
            print("ออกจากโปรแกรม...")
            break
        else:
            print("❌ ตัวเลือกไม่ถูกต้อง กรุณาเลือก 1, 2 หรือ 3")

if __name__ == "__main__":
    main_menu()
