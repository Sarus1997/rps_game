import random
from stats import load_stats, save_stats, show_report

def play_game():
    choices = {'1': 'หิน', '2': 'กระดาษ', '3': 'กรรไกร'}
    stats = load_stats()

    while True:
        rounds_input = input("ป้อนจำนวนรอบที่คุณต้องการเล่น: ")
        if rounds_input.isdigit():
            rounds = int(rounds_input)
            break
        else:
            print("❌ กรุณากรอกหมายเลขที่ถูกต้อง")

    user_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} of {rounds} ---")
        print("เลือก: 1 = หิน, 2 = กระดาษ, 3 = กรรไกร")
        user_input = input("ตัวเลือกของคุณ: ")

        if user_input not in choices:
            print("❌ ตัวเลือกไม่ถูกต้อง กรุณากรอก 1, 2 หรือ 3")
            continue

        user_choice = choices[user_input]
        computer_choice = random.choice(list(choices.values()))

        print(f"ตัวเลือกของคุณ: {user_choice}")
        print(f"คอมพิวเตอร์เลือก: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 เสมอกัน!")
            stats['ties'] += 1
        elif (user_choice == 'หิน' and computer_choice == 'กรรไกร') or \
             (user_choice == 'กระดาษ' and computer_choice == 'หิน') or \
             (user_choice == 'กรรไกร' and computer_choice == 'กระดาษ'):
            print("✅ รอบนี้คุณชนะ!")
            user_score += 1
            stats['wins'] += 1
        else:
            print("💻 รอบนี้คอมพิวเตอร์ชนะ!")
            computer_score += 1
            stats['losses'] += 1

        print(f"คะแนน -> คุณ: {user_score} | คอมพิวเตอร์: {computer_score}")

    stats['games_played'] += 1
    save_stats(stats)

    print("\n=== Final Result ===")
    if user_score > computer_score:
        print("🎉 ยินดีด้วย! คุณชนะเกมแล้ว!")
    elif user_score < computer_score:
        print("😢 คอมพิวเตอร์ชนะแล้ว! คราวหน้าขอให้โชคดีนะ!")
    else:
        print("🤝 เกมเสมอกัน!")

    show_report(stats)
