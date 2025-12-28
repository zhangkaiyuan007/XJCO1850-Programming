'''
You may write this code separately or add it to the code from grade-analyser
Read student_grades.csv into an appropriate data structure and use matplotlib to create a histogram of the score frequencies.
Have a go at changing the colour and chart title, and marking the average score with a line.
'''
import csv
import matplotlib.pyplot as plt

def main():
    filename = 'student_data.csv'
    grades = []

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(int(row['Grade']))

    plt.hist(grades, bins=10, color='skyblue', edgecolor='black')
    
    average_score = sum(grades) / len(grades)
    plt.axvline(average_score, color='red', linestyle='dashed', linewidth=2)
    
    plt.title('Frequency of Student Grades')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    
    plt.show()

if __name__ == "__main__":
    main()
