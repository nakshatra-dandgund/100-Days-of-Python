# 🎓 Python Journey – Day 8

Welcome to **Day 8** of my Python learning journey!
I am following the **100 Days of Code – Python** series by **Code With Harry**.

This repository contains my **Day 8 practice project**, where I learned and applied **`match-case` statements** to evaluate student performance based on percentage.

---

## 🧠 Project Overview
**Project Name:** Student Result & Performance Analyzer
**File Name:** `main.py`
**Author:** Nakshatra Dandgund

This program simulates a basic **school result system**. It takes student details and subject marks, calculates total and percentage, and uses **`match-case` with guards** to determine performance levels.

---

## ✨ Key Features
- Takes user input for student name and marks
- Uses lists and loops for data handling
- Calculates total marks and percentage
- Formats output clearly like a report card
- Uses **`match-case` statements** instead of `if-elif-else`

---

## 📄 Code Highlights
```python
match percentage:
    case p if p >= 90:
        performance = "Excellent Performance"
    case p if p >= 75:
        performance = "Very Good Performance"
    case p if p >= 60:
        performance = "Good Performance"
    case p if p >= 40:
        performance = "Average Performance"
    case _:
        performance = "Fail"
