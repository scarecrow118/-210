from agent import FitnessCoachAgent

def main():
    # Ініціалізуємо нашого AI-агента
    coach = FitnessCoachAgent()

    # --- ЗАПИТАННЯ 1 (Кардіо) ---
    prompt_1 = "Привіт, тренере! Сьогодні зранку побігав у високому темпі, а потім спокійно покрутив педалі. Що скажеш?"
    exercises_1 = [
        {"type": "cardio", "name": "Біг", "duration_min": 30, "intensity": 1.8},
        {"type": "cardio", "name": "Велосипед", "duration_min": 20, "intensity": 1.1}
    ]

    # --- ЗАПИТАННЯ 2 (Силове) ---
    prompt_2 = "Я сьогодні працював у залі з важкою вагою, робив базу. Оціни енерговитрати."
    exercises_2 = [
        {"type": "strength", "name": "Присідання зі штангою", "duration_min": 45, "weight_kg": 80.0},
        {"type": "strength", "name": "Жим лежачи", "duration_min": 30, "weight_kg": 60.0}
    ]

    # --- ЗАПИТАННЯ 3 (Комбіноване/Легке) ---
    prompt_3 = "Доброго дня! Був важкий день, тому зробила легку розминку з гантельками та трохи кардіо-рухів."
    exercises_3 = [
        {"type": "strength", "name": "Вправи з гантелями", "duration_min": 15, "weight_kg": 5.0},
        {"type": "cardio", "name": "Легка аеробіка", "duration_min": 10, "intensity": 1.0}
    ]

    # Виводимо результати демонстрації
    print("=== ДЕМОНСТРАЦІЯ РОБОТИ АГЕНТА ===\n")
    
    print(coach.answer_user(prompt_1, exercises_1))
    print("\n" + "="*60 + "\n")
    
    print(coach.answer_user(prompt_2, exercises_2))
    print("\n" + "="*60 + "\n")
    
    print(coach.answer_user(prompt_3, exercises_3))

if __name__ == "__main__":
    main()