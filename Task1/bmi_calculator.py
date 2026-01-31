def calculate_bmi():
    # BMI Calculator

    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))

        #Check for non-positive input
        if height <= 0 or weight <= 0:
            print("Error: Weight and height must be positive numbers.")
            return

        #Check for unrealistic height input
        if height > 3:
            print("Warning: Did you enter height in centimeters? Please enter height in meters (e.g., 1.75).")
            return

        #BMI Calculation
        print("-" * 50)
        bmi = weight / (height ** 2)

        print(f"Your BMI is:{bmi:.2f}")

        #Categorization of BMI
        if bmi < 18.5:
            print("Category:You're Underweight")
        elif 18.5 <= bmi <= 24.9:
            print("Category:You're Normal weight")
        elif 25.0 <= bmi <=29.9: 
            print("Category:You're Overweight")
        else:
            print("Category:You're Obese")

    #Handle invalid input: Such as non-numeric values
    except ValueError:
        print("Invalid input. Please enter numbers only (e.g., 70 or 1.75).")

    #Handle division by zero error
    except ZeroDivisionError:
        print("Height or Weight cannot be zero. Please enter a valid height.")

if __name__ == "__main__":
    calculate_bmi()

