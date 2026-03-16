'''
This is a difficult activity which will involve some relatively challenging filtering/sorting of data
You will want to have the docs or a guide on using matplotlib/pandas available, it is not expected that you do this completely independently.
chatGPT is very good when debugging Pandas, as it decodes error messages into more readable explanations- so if you are struggling to understand what 
you have done wrong I recommend pasting error messages into it!

All the basic program code has been included, you should be able to simply write the code to filter the data into an appropriate dataframe and then
plot and show the graphs.
'''

import pandas as pd
import matplotlib.pyplot as plt

def average_bar_chart(data):
    '''
    Complete this code to produce a bar chart of the total of each 'hours per day' column
    '''
    hour_cols = [c for c in data.columns if c.endswith("_Hours_Per_Day")]
    totals = data[hour_cols].sum()
    plt.figure(figsize=(10, 6))
    plt.bar(totals.index, totals.values)
    plt.title("Total Hours Per Day by Activity")
    plt.xlabel("Activity")
    plt.ylabel("Total Hours")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def hours_histogram(data, column_name):
    '''
    Complete this code so that it can display a histogram of any given 'hours per day' column
    '''
    if column_name not in data.columns:
        print(f"Column '{column_name}' not found.")
        return
    plt.figure(figsize=(8, 5))
    plt.hist(data[column_name], bins=10, edgecolor="black")
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def hours_pie_chart(data, student_id):
    '''
    Complete this code so that it produces a pie chart of any given student's hours per day - this should be selected by student ID (the first column)
    '''
    if student_id < 1 or student_id > len(data):
        print("Invalid student ID.")
        return
    hour_cols = [c for c in data.columns if c.endswith("_Hours_Per_Day")]
    row = data.iloc[student_id - 1]
    labels = [c.replace("_Hours_Per_Day", "").replace("_", " ") for c in hour_cols]
    values = row[hour_cols].values
    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title(f"Student {student_id} Hours Breakdown")
    plt.tight_layout()
    plt.show()

def total_hours_per_stress_level(data, stress_level):
    '''
    Complete this code to create a stacked bar chart showing a breakdown of the total hours worked by students, grouped by their reported stress level.
    '''
    hour_cols = [c for c in data.columns if c.endswith("_Hours_Per_Day")]
    subset = data[data["Stress_Level"] == stress_level]
    if subset.empty:
        print(f"No data for stress level '{stress_level}'.")
        return
    totals = subset[hour_cols].sum()
    plt.figure(figsize=(8, 5))
    bottom = 0
    for col in hour_cols:
        plt.bar(stress_level, totals[col], bottom=bottom, label=col.replace("_Hours_Per_Day", "").replace("_", " "))
        bottom += totals[col]
    plt.title(f"Total Hours by Activity for {stress_level} Stress Level")
    plt.xlabel("Stress Level")
    plt.ylabel("Total Hours")
    plt.legend()
    plt.tight_layout()
    plt.show()

def display_menu():
    print("Student Lifestyle Data Analysis")
    print("1 - view average hours per day")
    print("2 - view specific activity")
    print("3 - view per-student breakdown")
    print("4 - view per stress level breakdown")
    print("Q - quit")
    choice = 0
    while choice not in ["1","2","3","4","Q"]:
        choice = input("Select option: ").upper()
    return choice


## main program:

data = pd.read_csv("lifestyle_data.csv")

# Note - when you run this in Interactive mode, the 'input' will be through a pop up instead of the terminal.
while True:
    choice = display_menu()
    match choice:
        case "Q":
            break
        case "1":
            average_bar_chart(data)
        case "2":
            col = input("Enter Hours Per column to analyse: ")
            hours_histogram(data, col)
        case "3":
            stid = int(input("Enter student ID: "))
            hours_pie_chart(data, stid)
        case "4":
            stress_level = input("Enter stress level: ").title()
            total_hours_per_stress_level(data, stress_level)
