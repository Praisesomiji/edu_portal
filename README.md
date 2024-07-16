## MVP Features

    - **Student Dashboard**: 
        - Display Current GPA/CGPA.
        - Recent grades.
        - Attendance summary.
        - Upcoming events and deadlines.
        - Basic notifications.
    - **Academic Adviser Dashboard**:
        - List of advisees.
        - Basic performance analytics.
        - Communication tools.
        - Basic reporting.

## Technology Stack

- **Frontend**: Bootstrap (for responsive design), Chart.js (for graphs and charts)
- **Backend**: Django framework
- **Database**: SQLite

## Design

### Wireframes

**Student Dashboard Wireframe:**

```
+-----------------------------------------------------+
| Logo | Home | My Courses | My Performance | Profile |
+-----------------------------------------------------+
| User Profile Picture | Name | Logout                |
+-----------------------------------------------------+
| Summary Cards:                                       |
|  - Current GPA                                       |
|  - Attendance Rate                                   |
|  - Notifications                                     |
+-----------------------------------------------------+
| Graphs and Charts:                                   |
|  - Grade Trends                                      |
|  - Attendance                                        |
+-----------------------------------------------------+
| Notifications List                                   |
+-----------------------------------------------------+
```

**Academic Adviser Dashboard Wireframe:**

```
+------------------------------------------------------------+
| Logo | Home | Students | Advising Sessions | Reports | Profile |
+------------------------------------------------------------+
| User Profile Picture | Name | Account Settings | Logout       |
+------------------------------------------------------------+
| Quick Links:                                                |
|  - Dashboard                                                |
|  - Student Lists                                            |
|  - Reports                                                  |
|  - Messages                                                 |
+------------------------------------------------------------+
| Summary Cards:                                              |
|  - Total Students                                           |
|  - Students At Risk                                         |
|  - Upcoming Advising Sessions                               |
|  - Notifications                                            |
+------------------------------------------------------------+
| Graphs and Charts:                                          |
|  - Performance Overview                                     |
|  - Risk Analysis                                            |
|  - Advising Sessions                                        |
+------------------------------------------------------------+
| Notifications List                                          |
+------------------------------------------------------------+
```

### Database Design

We'll use SQLite for the database. Below is a simple schema to start with:

#### Tables

1. **Users**:
    - `id`: Integer (Primary Key)
    - `username`: Text (Unique)
    - `password`: Text
    - `first_name`: Text
    - `last_name`: Text
    - `email`: Text (Unique)
    - `role`: Text (Choices: "student", "adviser")

2. **StudentProfiles**:
    - `user_id`: Integer (Foreign Key to Users)
    - `gpa`: Float
    - `attendance_rate`: Float

3. **AdviserProfiles**:
    - `user_id`: Integer (Foreign Key to Users)
    - `department`: Text

4. **Courses**:
    - `id`: Integer (Primary Key)
    - `course_name`: Text
    - `instructor_name`: Text

5. **Enrollments**:
    - `id`: Integer (Primary Key)
    - `student_id`: Integer (Foreign Key to Users)
    - `course_id`: Integer (Foreign Key to Courses)
    - `current_grade`: Float
    - `attendance_rate`: Float

6. **Grades**:
    - `id`: Integer (Primary Key)
    - `student_id`: Integer (Foreign Key to Users)
    - `course_id`: Integer (Foreign Key to Courses)
    - `grade`: Float
    - `date_recorded`: DateTime

7. **Notifications**:
    - `id`: Integer (Primary Key)
    - `user_id`: Integer (Foreign Key to Users)
    - `message`: Text
    - `timestamp`: DateTime

8. **Messages**:
    - `id`: Integer (Primary Key)
    - `sender_id`: Integer (Foreign Key to Users)
    - `receiver_id`: Integer (Foreign Key to Users)
    - `content`: Text
    - `timestamp`: DateTime

#### Implementation

**Django project setup and implementation of the database schema**

1. **Set Up Django Project**:
    - Initialize a new Django project.
    - Create the necessary Django apps (users, courses, grades, notifications).

2. **Implement Database Schema**:
    - Define models corresponding to the database tables.
    - Apply migrations to create the database schema in SQLite.
