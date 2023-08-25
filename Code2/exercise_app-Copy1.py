import tkinter as tk
from tkinter import messagebox


def recommend_exercise(weight, bmi, bmr, gender, age):
    recommended_exercises = []
    
    if weight > 0.8 and age <= 40:
        recommended_exercises.append("High-intensity interval training (HIIT)")
    elif weight > 0.6:
        recommended_exercises.append("Cardio exercises (e.g., running, cycling)")
    else:
        recommended_exercises.append("Moderate-intensity exercises (e.g., brisk walking)")
    
    if bmi > 30:
        recommended_exercises.append("Low-impact exercises (e.g., swimming, yoga)")
    else:
        recommended_exercises.append("Strength training exercises")
    
    if bmr < 1500 and gender == "Female" and age > 40:
        recommended_exercises.append("Pilates or light resistance training")
    
    return recommended_exercises

def get_user_input():
    weight_lb = float(input("Enter weight in pounds: "))
    bmi = float(input("Enter BMI: "))
    bmr = float(input("Enter BMR: "))
    gender = input("Enter gender (Male/Female): ")
    age = int(input("Enter age: "))
    
    return weight_lb, bmi, bmr, gender, age

def main():
    weight_lb, bmi, bmr, gender, age = get_user_input()
    weight_kg = weight_lb * 0.453592  # Convert pounds to kilograms
    recommended_exercises = recommend_exercise(weight_kg, bmi, bmr, gender, age)

    print("Recommended Exercises:")
    for exercise in recommended_exercises:
        print(exercise)

    # Exercise calorie information (calories per hour per kg)
    exercise_calories = {
        "Moderate Cycling": 1.647825,
        "Light Calisthenics": 0.721008,
        "Vigorous Weight Lifting": 1.234853,
        "Light Weight Lifting": 0.617427,
        "Stair Machine": 1.852957,
        "Moderate Rowing": 1.441339,
        "General Aerobics": 1.338435,
        "Jazzercise": 1.234853,
        "Hatha Yoga Stretching": 0.823236,
        "General Running": 1.647825,
        "Moderate Jumping Rope": 2.059443,
        "Tai Chi": 0.823236,
        "Backpacking Hiking": 1.441339,
        "Moderate Walking": 0.679711,
        "Leisurely Swimming": 1.234853
    }

    print("\nCalories burned per hour for each exercise:")
    for exercise, calories_per_kg in exercise_calories.items():
        calories_burned = calories_per_kg * weight_kg
        print(f"{exercise}: {calories_burned:.2f} calories")

if __name__ == "__main__":
    main()
