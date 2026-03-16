# Task 4

## Task 4.1. 
Given the following relations in table format, identify the candidate keys, primary key and justify why a particular attribute or a combination of attributes is chosen. Give your answer by editing this file.

* TaskAssignment

  |TaskID	| TaskName|	EmployeeID |	EmployeeName |	ProjectID	| StartDate	| EndDate|
  |---	| ---|	--- |	--- |	---	| ---	| ---|
  |1	| Design Phase	|E001	| Alice Johnson	|P1001	|2025-01-01	|2025-01-10|
  |2	| Development	  |E002	| Bob Smith	|P1001	|2025-01-11	|2025-02-01|
  |3	| Testing Phase	|E001 |	Alice Johnson	|P1001	|2025-02-02	|2025-02-10|

  1. Candidate keys:
  2. Primary key is:
  3. Reason: 

* StudentEnrollment

  |StudentID	|CourseID	|EnrollmentDate	|Grade	|Semester	|Credits|
  |---	|---	|---	|---	|---	|---|
  |S001	|C101	|2025-01-10	|A	|Spring	|3|
  |S002	|C102	|2025-01-12	|B	|Spring	|4|
  |S001	|C102	|2025-01-12	|A-	|Spring	|4|
  |S003	|C101	|2025-01-11	|B+	|Spring	|3|
  |S002	|C103	|2025-01-13	|A	|Spring	|3|

  1. Candidate keys:
  2. Primary key is:
  3. Reason:

* CarRental

  |RentalID	|CustomerID	|CarID	|StartDate	|EndDate	|RentalCost	|Location |
  |---	|---	|---	|---	|---	|---	|--- |
  |R001	|C1001	|V001	|2025-01-05	|2025-01-10	|£200	| Leeds |
  |R002	|C1002	|V002	|2025-01-07	|2025-01-12	|£250	|York |
  |R003	|C1001	|V003	|2025-01-15	|2025-01-20	|£300	|London|
  |R004	|C1003	|V001	|2025-01-20	|2025-01-25	|£220	|Sheffield|
  |R005	|C1004	|V002	|2025-01-18	|2025-01-23	|£240	|Manchester|

  1. Candidate keys: 
  2. Primary key is: 
  3. Reason:
 

## Task 4.2
  
Given the following relation schemas, identify the foreign keys (e.g., in the Staff relation, branchNo is a foreign key referencing branchNo in the Branch relation). The underlined attribute is the primary key. Give your answer by editing this file.

* E-commerce system

  - Product(<ins>ProductID</ins>, ProductName, Price, CategoryID)
  - Categories(<ins>CategoryID</ins>, CategoryName, Description)
  - Foreign keys: 

* Student-Course Enrollment

  - Students(<ins>StudentID</ins>, FirstName, LastName, Email)
  - Courses(<ins>CourseID</ins>, CourseName, Credits)
  - Enrollments(<ins>EnrollmentID</ins>, StudentID, CourseID, EnrollmentDate)
  - Foreign keys: 

* Employee-Department

  - Departments: (<ins>DepartmentID</ins>, DepartmentName, ManagerID)
  - Employees: (<ins>EmployeeID</ins>, FirstName, LastName, DepartmentID, ManagerID)
  - Foreign keys:
    
* Hospital Management System

  - Doctors(<ins>DoctorID</ins>, Name, Specialty, DepartmentID)
  - Departments(<ins>DepartmentID</ins>, DepartmentName)
  - Patients(<ins>PatientID</ins>, Name, Age, DoctorID)
  - Appointments(<ins>AppointmentID</ins>, PatientID, DoctorID, AppointmentDate)
  - Foreign keys:
  
* Social Media Platform

  - Users: (<ins>UserID</ins>, UserName, Email, DateJoined)
  - Posts: (<ins>PostID</ins>, UserID, Content, PostDate)
  - Comments: (<ins>CommentID</ins>, PostID, UserID, CommentContent, CommentDate)
  - Likes: (<ins>LikeID</ins>, PostID, UserID, LikeDate)
  - Foreign keys:










  