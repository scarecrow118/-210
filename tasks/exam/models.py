from abc import ABC, abstractmethod

class Exercise(ABC):
    """Абстрактний клас для вправ."""
    def __init__(self, name: str, duration_min: int):
        self.name = name
        self.duration_min = duration_min

    @abstractmethod
    def calories_burned(self) -> float:
        pass


class CardioExercise(Exercise):
    """Клас для кардіо-вправ (Успадкування)."""
    def __init__(self, name: str, duration_min: int, intensity: float):
        super().__init__(name, duration_min)
        # Обмежуємо коефіцієнт інтенсивності в межах 1.0–2.0
        self.intensity = max(1.0, min(2.0, intensity))

    def calories_burned(self) -> float:
        return self.duration_min * 8 * self.intensity


class StrengthExercise(Exercise):
    """Клас для силових вправ (Успадкування)."""
    def __init__(self, name: str, duration_min: int, weight_kg: float):
        super().__init__(name, duration_min)
        self.weight_kg = weight_kg

    def calories_burned(self) -> float:
        return self.duration_min * 5 + self.weight_kg * 0.5


class Workout:
    """Клас для обліку тренування (Інкапсуляція та Поліморфізм)."""
    def __init__(self):
        self.__exercises = []  # Приватний атрибут (інкапсуляція)

    def add(self, exercise: Exercise):
        if isinstance(exercise, Exercise):
            self.__exercises.append(exercise)
        else:
            raise TypeError("Об'єкт має бути нащадком класу Exercise")

    def total_calories(self) -> float:
        # Поліморфний виклик методу calories_burned()
        return sum(exe.calories_burned() for exe in self.__exercises)

    def summary(self) -> dict:
        return {
            "exercises": [
                {"name": exe.name, "calories": round(exe.calories_burned(), 2)} 
                for exe in self.__exercises
            ],
            "total_calories": round(self.total_calories(), 2)
        }