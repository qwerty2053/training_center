### Training Center API

An API for managing a training center using Django Rest Framework (DRF). It allows managing courses, students, and scores, as well as establishing relationships between them. The API provides CRUD (Create, Read, Update, Delete) functionality for each entity, along with search and filtering capabilities.

---

### Requirements

- Python 3.7 or higher  
- Django 3.2 or higher  
- Django Rest Framework 3.12 or higher  

---

### Installation

1. Clone the project repository:

   ```bash
   git clone https://github.com/qwerty2053/training_center.git
   ```

2. Navigate to the project directory:

   ```bash
   cd training_center
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the database:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

---

### Endpoints

#### **Courses**

- `GET /api/courses/` - Retrieve a list of courses  
- `POST /api/courses/` - Create a new course  
- `GET /api/courses/{id}/` - Retrieve details of a course by ID  
- `PUT /api/courses/{id}/` - Update a course by ID  
- `DELETE /api/courses/{id}/` - Delete a course by ID  

#### **Students**

- `GET /api/students/` - Retrieve a list of students  
- `POST /api/students/` - Create a new student  
- `GET /api/students/{id}/` - Retrieve details of a student by ID  
- `PUT /api/students/{id}/` - Update a student by ID  
- `DELETE /api/students/{id}/` - Delete a student by ID  

#### **Scores**

- `GET /api/scores/` - Retrieve a list of scores  
- `POST /api/scores/` - Create a new score  
- `GET /api/scores/{id}/` - Retrieve details of a score by ID  
- `PUT /api/scores/{id}/` - Update a score by ID  
- `DELETE /api/scores/{id}/` - Delete a score by ID  

---

### Entity Relationships

- `POST /api/courses/{course_id}/enroll/{student_id}/` - Enroll a student in a course  

---

### Search and Filtering

- `GET /api/courses/?search=<query>` - Search for courses by name  
- `GET /api/students/?search=<query>` - Search for students by first and last name  

---

### Data Models

#### **Course**

- `id` (integer): Course ID  
- `name` (string): Course name  
- `description` (string): Course description  
- `duration` (duration): Course duration  

#### **Student**

- `id` (integer): Student ID  
- `first_name` (string): Student's first name  
- `last_name` (string): Student's last name  
- `email` (string): Student's email  
- `courses` (many-to-many): Courses associated with the student  

#### **Score**

- `id` (integer): Score ID  
- `value` (integer): Score value (from 1 to 10)  
- `date` (date): Date of the score  
- `course` (integer): Course ID associated with the score  
- `student` (integer): Student ID associated with the score  