from models import CardioExercise, StrengthExercise, Workout

# Інструмент (Tool) для AI-агента
def calculate_workout(exercises: list) -> dict:
    workout = Workout()
    
    for exe_data in exercises:
        exe_type = exe_data.get("type", "").lower()
        name = exe_data.get("name")
        duration = exe_data.get("duration_min")
        
        if exe_type == "cardio":
            intensity = exe_data.get("intensity", 1.0)
            exercise = CardioExercise(name, duration, intensity)
        elif exe_type == "strength":
            weight = exe_data.get("weight_kg", 0.0)
            exercise = StrengthExercise(name, duration, weight)
        else:
            continue  # Ігноруємо невідомі типи вправ
            
        workout.add(exercise)
        
    return workout.summary()


# AI-агент (Персональний фітнес-тренер)
class FitnessCoachAgent:
    def __init__(self):
        self.role = "Персональний фітнес-тренер"
        self.language = "Українська"

    def answer_user(self, user_prompt: str, exercises_data: list) -> str:
        # Агент викликає інструмент calculate_workout
        workout_summary = calculate_workout(exercises_data)
        total_cals = workout_summary["total_calories"]
        
        # Формування відповіді агента українською мовою
        response = f"💪 **Привіт! Я твій персональний фітнес-тренер.**\n"
        response += f"Аналізую твій запит: *\"{user_prompt}\"*\n\n"
        response += f"📋 **Звіт по тренуванню:**\n"
        
        for exe in workout_summary["exercises"]:
            response += f" - {exe['name']}: {exe['calories']} ккал\n"
            
        response += f"🔥 **Загалом спалено калорій:** {total_cals} ккал\n\n"
        response += f"🧠 **Мої рекомендації щодо навантаження:**\n"
        
        # Логіка аналізу навантаження
        if total_cals < 250:
            response += "✨ Це була чудова легка розминка або відновлювальне тренування. Для жироспалення або росту витривалості наступного разу варто збільшити тривалість або інтенсивність!"
        elif 250 <= total_cals <= 500:
            response += "👍 Гарне збалансоване тренування середньої інтенсивності. Ти у чудовій формі, підтримуй такий темп 3-4 рази на тиждень."
        else:
            response += "🚀 Потужно! Високоінтенсивне або важке силове тренування. Обов'язково зроби якісну заминку (стретчинг) та пий достатньо води. Не забудь відпочити мінімум 24 години перед наступним таким навантаженням."
            
        return response