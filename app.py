import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='FitLife - Streamlit', layout='centered')

st.title('🏋️‍♂️ FitLife — Multi-Agent Fitness & Diet Planner')
st.markdown('A Streamlit UI for the FitLife project.')

# Sidebar Inputs
st.sidebar.header("Enter Your Details")
name = st.sidebar.text_input("Name", value="User")
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=22)
gender = st.sidebar.selectbox("Gender", ["male", "female", "other"])
weight = st.sidebar.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0)
height = st.sidebar.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
activity = st.sidebar.selectbox("Activity Level", [
    "Sedentary (little/no exercise)",
    "Lightly active (1-3 days/week)",
    "Moderately active (3-5 days/week)",
    "Very active (6-7 days/week)",
    "Extra active (physical job / training)"
])
goal = st.sidebar.selectbox("Goal", ["Maintain weight", "Lose weight", "Gain muscle"])
diet = st.sidebar.selectbox("Diet Preference", ["Balanced", "Vegetarian", "High-protein", "Keto"])

# BMI Calculator
def calculate_bmi(weight, height_cm):
    return weight / ((height_cm / 100) ** 2)

bmi = calculate_bmi(weight, height)
st.metric("BMI", f"{bmi:.1f}")

# Display goal-based message
st.write(f"🎯 Goal: **{goal}**")
st.write(f"👤 Hello **{name}**, your daily calorie intake will be adjusted based on your goal.\n")


# Personalized MEAL PLAN
meal_plans = {
    "Lose weight": [
        "Oats + Fruit",
        "Salad + Soup",
        "Veg Sandwich",
        "Brown Rice + Veggies",
        "Lean Chicken + Salad",
        "Paneer + Roti",
        "Detox Day: Fruit/Nuts"
    ],
    "Gain muscle": [
        "Eggs + Oats",
        "Chicken + Rice",
        "Paneer + Chapati",
        "Protein Shake + Banana",
        "Beef/Fish + Sweet Potato",
        "Daal + Roti + Ghee",
        "High-Protein Salad + Nuts"
    ],
    "Maintain weight": [
        "Balanced Indian Thali",
        "Vegetable Upma",
        "Egg Sandwich",
        "Paneer Curry + Rice",
        "Mixed Veg + Quinoa",
        "Grilled Chicken + Salad",
        "Moderate Carb Day"
    ]
}

meal_plan = meal_plans.get(goal, meal_plans["Maintain weight"])

st.subheader("🍽 Personalized 7-Day Meal Plan")
for i, meal in enumerate(meal_plan):
    st.write(f"Day {i+1}: {meal}")


# Personalized WORKOUT PLAN
workout_plans = {
    "Lose weight": {
        "Sedentary (little/no exercise)": ["Light Walk", "Yoga", "Cycling", "Yoga", "Stretching", "Light Cardio", "Rest"],
        "Lightly active (1-3 days/week)": ["Jogging", "Cycling", "Core Workout", "Yoga", "HIIT-Light", "Cardio Mix", "Rest"],
        "Moderately active (3-5 days/week)": ["HIIT", "Cardio + Strength", "Upper Body", "Yoga", "Core + Cardio", "Cycling", "Rest"],
        "Very active (6-7 days/week)": ["HIIT Intensive", "Running", "Strength Mix", "Core + Cardio", "Leg Day", "Swimming", "Rest"],
        "Extra active (physical job / training)": ["Advanced HIIT", "Strength Circuit", "Endurance Run", "Plyometrics", "Core", "Active Recovery", "Rest"]
    },
    "Gain muscle": {
        "Sedentary (little/no exercise)": ["Full Body", "Rest", "Full Body", "Rest", "Upper Body", "Lower Body", "Rest"],
        "Lightly active (1-3 days/week)": ["Push", "Rest", "Pull", "Legs", "Rest", "Arms + Abs", "Rest"],
        "Moderately active (3-5 days/week)": ["Push Day", "Pull Day", "Leg Day", "Rest", "Chest + Triceps", "Back + Biceps", "Abs"],
        "Very active (6-7 days/week)": ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core", "Active Rest"],
        "Extra active (physical job / training)": ["Powerlifting", "Olympic Lifts", "Legs", "Push", "Pull", "Core", "Rest"]
    },
    "Maintain weight": {
        "Sedentary (little/no exercise)": ["Light Cardio", "Stretching", "Yoga", "Walk", "Core", "Light Strength", "Rest"],
        "Lightly active (1-3 days/week)": ["Cardio Mix", "Upper Body", "Core", "Yoga", "Lower Body", "Full Body", "Rest"],
        "Moderately active (3-5 days/week)": ["Cardio + Strength", "Upper Body", "Yoga", "Lower Body", "Core + Strength", "Full Body", "Rest"],
        "Very active (6-7 days/week)": ["Strength", "Cardio", "Yoga", "Leg Day", "Upper Body", "HIIT", "Rest"],
        "Extra active (physical job / training)": ["Strength Intensive", "Endurance Cardio", "Core", "Mobility", "Leg Day", "Full Body", "Rest"]
    }
}

workout_plan = workout_plans.get(goal, {}).get(activity)

if workout_plan is None:
    workout_plan = ["Mixed Activity", "Walk", "Yoga", "Strength", "Core", "Cardio", "Rest"]

st.subheader("🏋️‍♀️ Personalized 7-Day Workout Plan")
for i, workout in enumerate(workout_plan):
    st.write(f"Day {i+1}: {workout}")


# Export CSV for download
if st.button("Download Workout + Meal Plan"):
    df = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(7)],
        "Meal": meal_plan,
        "Workout": workout_plan
    })
    st.download_button("Click to Download", df.to_csv(index=False), file_name="fitlife_plan.csv")


st.caption("This is a simple frontend demo. You can integrate AI features later.")
st.write("Last updated:", datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))
