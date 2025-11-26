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
st.write(f"👤 Hello **{name}**, your daily calorie intake will be adjusted based on your goal.")

# Sample Meal Plan
st.subheader("🍽 Sample 7-Day Meal Plan")
meal_plan = [
    "Chicken + Rice + Salad",
    "Eggs + Oats + Banana",
    "Grilled Paneer + Roti + Veggies",
    "Brown Rice + Dal + Salad",
    "Tofu + Quinoa + Veggies",
    "Fish + Sweet Potato",
    "Vegetable Salad + Nuts"
]
for i, meal in enumerate(meal_plan):
    st.write(f"Day {i+1}: {meal}")

# Sample Workout Plan
st.subheader("🏋️‍♀️ 7-Day Workout Plan")
workouts = [
    "Full Body Strength",
    "Cardio Training",
    "Upper Body",
    "Yoga / Recovery",
    "Leg Day",
    "HIIT",
    "Rest Day"
]
for i, w in enumerate(workouts):
    st.write(f"Day {i+1}: {w}")

# Export CSV
if st.button("Download Workout + Meal Plan"):
    df = pd.DataFrame({"Day": [f"Day {i+1}" for i in range(7)], "Meal": meal_plan, "Workout": workouts})
    st.download_button("Click to Download", df.to_csv(index=False), file_name="fitlife_plan.csv")

st.caption("This is a simple frontend demo. You can integrate AI features later.")
st.write("Last updated:", datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))
