'''
Create a program which reads in the provided file ‘student_grades.csv’.
The program should:
-	Print out the average score
-	Add an extra column ‘Passed’ which contains ‘True’ if the score is greater than 70.
-	Print out the data with this new column, sorted by student_id ascending.
'''
import csv

def main():
    filename = 'student_data.csv'
    student_records = []
    total_score = 0
    count = 0

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            s_id = row['Student_ID']
            grade = int(row['Grade'])
            passed = grade > 70
            
            student_records.append({
                'Student_ID': s_id,
                'Grade': grade,
                'Passed': passed
            })
            total_score += grade
            count += 1

    if count > 0:
        average = total_score / count
        print(f"Average score: {average:.2f}")

    sorted_records = sorted(student_records, key=lambda x: x['Student_ID'])

    print("Student_ID,Grade,Passed")
    for record in sorted_records:
        print(f"{record['Student_ID']},{record['Grade']},{record['Passed']}")

if __name__ == "__main__":
    main()