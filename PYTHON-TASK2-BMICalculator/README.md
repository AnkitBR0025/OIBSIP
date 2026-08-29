# BMI Checker (Python)

A simple Python script to calculate BMI (Body Mass Index) using weight (kg) and height (feet), and show the category you fall into.

## How it works

1. Enter your weight in kg.
2. Enter your height in feet.
3. Height is converted to meters.
4. BMI is calculated as:
   ```
   BMI = weight / (height_in_meters ** 2)
   ```
5. Based on the BMI value, a category is shown.

## Categories

 BMI Range      Category    

 < 18.5         Underweight 
 18.5 – 24.9    Normal      
 25 – 29.9      Overweight  
 30 and above   Obese       

## Run it

```bash
python bmi_checker.py
```

## Example


---CHECK YOUR BMI(Body Mass Index)---
Enter your weight in kg: 65
Enter your height in feet: 5.6

Your weight is 65.0 kg and height is 1.71 m.

Result:-
Your BMI is: 22.19
Category: Normal


## Tech used

Python
