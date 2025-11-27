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

# Classification
if bmi < 18.5:
    body_type = "Underweight"
elif bmi < 25:
    body_type = "Healthy"
elif bmi < 30:
    body_type = "Overweight"
else:
    body_type = "Obese"

st.write(f"📌 **Body Type:** {body_type}")
st.write(f"🎯 **Goal Selected:** {goal}")


# Meal Plan Personalized by Body Type + Goal
meal_plans = {
    "Lose weight": {
        "Underweight": ["Oats + Milk", "Boiled Eggs + Fruit", "Paneer Salad", "Veg Soup", "Tofu Stir Fry", "Brown Rice + Dal", "Salad + Nuts"],
        "Healthy": ["Oats + Banana", "Chicken + Salad", "Brown Rice + Veg", "Milk + Nuts", "Paneer + Roti", "Fish + Salad", "Soup + Veggies"],
        "Overweight": ["Veg Soup + Apple", "Salad + Sprouts", "Low-carb Roti + Veg", "Smoothie + Seeds", "Tofu Wrap", "Fish + Greens", "Detox Day"],
        "Obese": ["Detox Smoothie", "Veg Soup", "Salad", "Boiled Veg", "Low-carb Roti", "Fruits only", "Soup only"]
    },
    "Maintain weight": {
        "Healthy": ["Oats + Eggs", "Chicken + Rice", "Dal + Roti", "Paneer + Rice", "Fish + Veg", "Egg Rice", "Balanced Meal"],
        "default": ["Oats", "Dal", "Veg", "Rice", "Chicken", "Roti", "Fruits"]
    },
    "Gain muscle": {
        "Underweight": ["Egg Omelette", "Chicken + Oats", "Peanut Butter Sandwich", "Paneer Rice", "Banana Shake", "Fish Meal", "High Protein Wrap"],
        "Healthy": ["Protein Shake", "Chicken + Rice", "Paneer + Roti", "Eggs + Rice", "Fish + Veg", "High Protein Dal", "Milk + Nuts"],
        "default": ["Protein Shake", "Paneer", "Eggs", "Fish", "Milk", "Banana", "Healthy Meals"]
    }
}

meal_plan = meal_plans.get(goal).get(body_type, meal_plans.get(goal).get("default"))


# Workout Plan Personalized
workout_plans = {
    "Lose weight": {
        "Sedentary (little/no exercise)": ["Light Walking", "Yoga", "Cycling", "Walk", "Stretching", "Light Cardio", "Rest"],
        "Moderately active (3-5 days/week)": ["HIIT", "Cardio", "Upper Body", "Core", "Lower Body", "Cycling", "Rest"]
    },
    "Gain muscle": {
        "Sedentary (little/no exercise)": ["Full Body", "Rest", "Full Body", "Rest", "Upper Body", "Lower Body", "Rest"],
        "Moderately active (3-5 days/week)": ["Push Day", "Pull Day", "Leg Day", "Rest", "Chest + Triceps", "Back + Biceps", "Abs"]
    },
    "Maintain weight": {
        "default": ["Mixed Cardio", "Upper Body", "Yoga", "Lower Body", "Stretching", "Full Body", "Rest"]
    }
}

workout_plan = workout_plans.get(goal).get(activity, workout_plans.get(goal).get("default"))


# Display Meal Plan
st.subheader("🍽 Your Personalized 7-Day Meal Plan")
for i, meal in enumerate(meal_plan):
    st.write(f"Day {i+1}: {meal}")

# Display Workout Plan
st.subheader("🏋️‍♀️ Your Personalized 7-Day Workout Plan")
for i, workout in enumerate(workout_plan):
    st.write(f"Day {i+1}: {workout}")


# Export Personalized CSV
if st.button("Download Personalized Plan"):
    df = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(7)],
        "Meal Plan": meal_plan,
        "Workout Plan": workout_plan
    })
    st.download_button("Click to Download", df.to_csv(index=False), file_name=f"{name}_fitlife_plan.csv")

st.caption("AI-Based Personalized Fitness & Diet Planner")
st.write("Last updated:", datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))
