# Django Attendance Tracker - Candidate Instructions

## 🎯 Your Mission

You are given a Django project for managing student attendance with some bugs. Your tasks:

1. **Debug & fix 2 bugs** that prevent the app from running
2. **Implement a new API endpoint** to mark student attendance

---

## 🚀 Setup Instructions

### Step 1: Open the Project
1. **Open VS Code**
2. **Install Rest Book extension** - [here](https://marketplace.visualstudio.com/items?itemName=tanhakabir.rest-book)


### Step 2: Try to Run the Project
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**Note:** The project won't start due to bugs. Your job is to fix them!

### Step 4: Once server is up, hit list_students endpoint and fix the bug

---

## 📋 Current Functionality

### Existing Endpoints:
- `GET /students/` - List all students
- `GET /students/<id>/` - Get student details

### Sample Data:
You'll need to create students first to test the functionality.

---

## 🐞 Bugs to Fix

You'll encounter 2 bugs that prevent the app from working. Your task is to debug each error and fix the underlying issues.

---


## 🧪 Testing Your Solution

1. **Fix all bugs** and get the server running
2. **Create some students first** using the provided `api.restbook` file:
   - The REST Book extension is pre-configured in this workspace
   - Open `api.restbook` and run the "Create a new student" request
   - You can modify the student data as needed

3. **Test the list students endpoint:**
   - Use the "List all students" request in `api.restbook`
   - This will help you identify and fix the second bug

4. **Test your new endpoint:**
   - Use the "Mark attendance" request in `api.restbook`
   - Or use curl:
   ```bash
   curl -X PUT http://localhost:8000/students/1/mark_attendance/ \
     -H "Content-Type: application/json" \
     -d '{"date": "2025-01-15"}'
   ```


---

## 🛠 New Functionality to Implement

- Create a new endpoint with following requirements

### Endpoint: Mark Student Attendance
**URL:** `PUT /students/<id>/mark_attendance/`

**Request Body:**
```json
{
  "date": "2025-01-15"
}
```

**Expected Behavior:**
- Mark the student as present for the given date
- Prevent duplicate attendance for the same date
- Return total attendance count for that student

**Success Response (200):**
```json
{
  "message": "Marked present",
  "total_attendance": 5
}
```

**Error Response (400):**
```json
{
  "error": "Already marked"
}
```

---

Good luck! 🍀 