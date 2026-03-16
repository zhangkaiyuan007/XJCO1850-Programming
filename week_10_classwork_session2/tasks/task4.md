# Task 4

## Task 4.1. 
Given the following relations in table format, identify the candidate keys, primary key and justify why a particular attribute or a combination of attributes is chosen. Give your answer by editing this file.

* TaskAssignment

  |TaskID	| TaskName|	EmployeeID |	EmployeeName |	ProjectID	| StartDate	| EndDate|
  |---	| ---|	--- |	--- |	---	| ---	| ---|
  |1	| Design Phase	|E001	| Alice Johnson	|P1001	|2025-01-01	|2025-01-10|
  |2	| Development	  |E002	| Bob Smith	|P1001	|2025-01-11	|2025-02-01|
  |3	| Testing Phase	|E001 |	Alice Johnson	|P1001	|2025-02-02	|2025-02-10|

  1. Candidate keys: TaskID; (EmployeeID, ProjectID, TaskName, StartDate)
  2. Primary key is: TaskID
  3. Reason: TaskID uniquely identifies each task assignment, while the composite key only works if those fields are always unique together.

* StudentEnrollment

  |StudentID	|CourseID	|EnrollmentDate	|Grade	|Semester	|Credits|
  |---	|---	|---	|---	|---	|---|
  |S001	|C101	|2025-01-10	|A	|Spring	|3|
  |S002	|C102	|2025-01-12	|B	|Spring	|4|
  |S001	|C102	|2025-01-12	|A-	|Spring	|4|
  |S003	|C101	|2025-01-11	|B+	|Spring	|3|
  |S002	|C103	|2025-01-13	|A	|Spring	|3|

  1. Candidate keys: (StudentID, CourseID, Semester); (StudentID, CourseID, EnrollmentDate)
  2. Primary key is: (StudentID, CourseID, Semester)
  3. Reason: A student can take a course again in a different semester, so the composite key is needed to uniquely identify an enrollment.

* CarRental

  |RentalID	|CustomerID	|CarID	|StartDate	|EndDate	|RentalCost	|Location |
  |---	|---	|---	|---	|---	|---	|--- |
  |R001	|C1001	|V001	|2025-01-05	|2025-01-10	|£200	| Leeds |
  |R002	|C1002	|V002	|2025-01-07	|2025-01-12	|£250	|York |
  |R003	|C1001	|V003	|2025-01-15	|2025-01-20	|£300	|London|
  |R004	|C1003	|V001	|2025-01-20	|2025-01-25	|£220	|Sheffield|
  |R005	|C1004	|V002	|2025-01-18	|2025-01-23	|£240	|Manchester|

  1. Candidate keys: RentalID; (CustomerID, CarID, StartDate)
  2. Primary key is: RentalID
  3. Reason: RentalID is a single unique identifier for each rental record.
 

## Task 4.2
  
Given the following relation schemas, identify the foreign keys (e.g., in the Staff relation, branchNo is a foreign key referencing branchNo in the Branch relation). The underlined attribute is the primary key. Give your answer by editing this file.

* E-commerce system

  - Product(<ins>ProductID</ins>, ProductName, Price, CategoryID)
  - Categories(<ins>CategoryID</ins>, CategoryName, Description)
  - Foreign keys: Product.CategoryID -> Categories.CategoryID

* Student-Course Enrollment

  - Students(<ins>StudentID</ins>, FirstName, LastName, Email)
  - Courses(<ins>CourseID</ins>, CourseName, Credits)
  - Enrollments(<ins>EnrollmentID</ins>, StudentID, CourseID, EnrollmentDate)
  - Foreign keys: Enrollments.StudentID -> Students.StudentID; Enrollments.CourseID -> Courses.CourseID

* Employee-Department

  - Departments: (<ins>DepartmentID</ins>, DepartmentName, ManagerID)
  - Employees: (<ins>EmployeeID</ins>, FirstName, LastName, DepartmentID, ManagerID)
  - Foreign keys: Employees.DepartmentID -> Departments.DepartmentID; Employees.ManagerID -> Employees.EmployeeID; Departments.ManagerID -> Employees.EmployeeID
    
* Hospital Management System

  - Doctors(<ins>DoctorID</ins>, Name, Specialty, DepartmentID)
  - Departments(<ins>DepartmentID</ins>, DepartmentName)
  - Patients(<ins>PatientID</ins>, Name, Age, DoctorID)
  - Appointments(<ins>AppointmentID</ins>, PatientID, DoctorID, AppointmentDate)
  - Foreign keys: Doctors.DepartmentID -> Departments.DepartmentID; Patients.DoctorID -> Doctors.DoctorID; Appointments.PatientID -> Patients.PatientID; Appointments.DoctorID -> Doctors.DoctorID
  
* Social Media Platform

  - Users: (<ins>UserID</ins>, UserName, Email, DateJoined)
  - Posts: (<ins>PostID</ins>, UserID, Content, PostDate)
  - Comments: (<ins>CommentID</ins>, PostID, UserID, CommentContent, CommentDate)
  - Likes: (<ins>LikeID</ins>, PostID, UserID, LikeDate)
  - Foreign keys: Posts.UserID -> Users.UserID; Comments.PostID -> Posts.PostID; Comments.UserID -> Users.UserID; Likes.PostID -> Posts.PostID; Likes.UserID -> Users.UserID










  
