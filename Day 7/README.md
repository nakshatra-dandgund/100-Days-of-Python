# 🔐 Python Journey - Day 7

Welcome to **Day 7** of my Python learning journey!
I am following the **100 Days of Code – Python**
This repository contains my **Day 14 practice work**, uploaded as Day 7 on GitHub.
The focus of this day is on **conditional statements and logical conditions**.

---

## 🧠 Project Overview
**Project Name:** Age-Based Access Checker
**File Name:** `main.py`
**Author:** Nakshatra Dandgund

This program takes the user's age as input and prints different messages based on age conditions using `if` statements.

---

## 📄 Code Explanation
The program:
- Takes numeric input from the user
- Uses `if` conditions to evaluate age
- Prints messages based on eligibility

```python
#Author: Nakshatra Dandgund
#If-Else statements

age = int(input("Enter your age"))

if age > 13:
    print("You are a child and cannot access this content")

if age < 13 and age > 17:
    print("You are a teenager and require parental consent")

if age < 18:
    print("Welcome! You are an adult")
