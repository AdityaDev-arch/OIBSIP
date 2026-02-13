# OIBSIP - Oasis Infobyte Student Internship Program

This repository contains the tasks completed during my **Python Programming Internship** at **Oasis Infobyte**.

---

## 🚀 Task 1: Command-Line BMI Calculator

### Project Description

A Python-based tool designed to calculate a user's **Body Mass Index (BMI)** and classify it into health categories such as Underweight, Normal Weight, Overweight, and Obese. This project focuses on clean code, accurate mathematical implementation, and robust error handling.

### ✨ Key Features

- **User Input Validation:** Ensures that weight and height inputs are positive numbers and handles non-numeric inputs gracefully using `try-except` blocks.
- **Realistic Range Checks:** Includes logic to warn users if a height seems unrealistic (e.g., entered in centimeters instead of meters).
- **Automated Categorization:** Classifies the BMI result based on standard WHO health ranges.
- **Professional CLI Output:** Uses visual dividers and formatted strings for a clean user experience.

### 🛠️ Technical Concepts Used

- **Python Basics:** Functions, Conditional Statements (`if-elif-else`).
- **Error Handling:** `ValueError` and `ZeroDivisionError` handling.
- **Input/Output:** `f-strings` for precise decimal formatting.
- **Environment:** Virtual environment (venv) for dependency isolation.

### 🏃 How to Run

1. Clone the repository:
   git clone [https://github.com/AdityaDev-arch/OIBSIP.git](https://github.com/AdityaDev-arch/OIBSIP.git)

2. Navigate to the task folder:
   cd Task1

3. Run the script:
   python bmi_calculator.py

---

## 🔐 Task 2: Random Password Generator

### Project Description

A versatile command-line tool that generates secure and random passwords. This project allows users to customize their password's strength by choosing specific lengths and selecting which character types (letters, numbers, or symbols) to include.

### ✨ Key Features

- **Customizable Complexity:** Users can toggle letters, numbers, and symbols on or off based on their security needs.
- **Input Validation Loop:** Includes a robust `while` loop to handle user preferences, ensuring only 'y' or 'n' responses are accepted.
- **Error Handling:** Prevents crashes by validating numerical input for length and ensuring at least one character set is selected before generation.
- **Clean User Interface:** Provides clear feedback and formatted output for a better user experience.

### 🛠️ Technical Concepts Used

- **Standard Libraries:** Utilized `random` for unpredictable character selection and `string` for secure character set management.
- **Modular Logic:** Implemented helper functions to keep the code "DRY" (Don't Repeat Yourself).
- **Control Flow:** Used generator expressions and the `.join()` method to build strings efficiently.

### 🏃 How to Run

1. Navigate to the task folder:
   cd Task2

2. Run the script:
   python password_generator.py

---

## ☁️ Task 3: Basic Weather App

### Project Description

A real-time weather application that fetches data from the **OpenWeatherMap API**. Users can enter any city name to retrieve current weather statistics, including temperature, humidity, and general weather conditions.

### ✨ Key Features

- **Live API Integration:** Connects to external servers to provide real-time, accurate global weather data.
- **Smart Error Handling:** Specifically manages connection issues and cases where a city name might be misspelled or not found.
- **Data Parsing:** Demonstrates the ability to process JSON responses from web services into a user-friendly format.
- **Unit Conversion:** Displays temperature in Celsius for easy reading.

### 🛠️ Technical Concepts Used

- **External Libraries:** Used the `requests` library for HTTP communication.
- **JSON Manipulation:** Navigated complex dictionary structures to extract specific data points.
- **User-Centric Design:** Focused on friendly, conversational feedback for a "human" feel.

### 🏃 How to Run

1. Navigate to the task folder:
   cd Task3

2. Run the script:
   python weather_app.py
