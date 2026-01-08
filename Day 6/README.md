# 🔤 Python Journey - Day 6

Welcome to **Day 6** of my Python learning journey!
I am following the **100 Days of Code – Python** series by **Code With Harry**.
This repository contains my **Day 11 practice work**, uploaded as Day 6 on GitHub.

---

## 🧠 Project Overview
**Project Name:** String Slicing and Character Iteration
**File Name:** `main.py`
**Author:** Nakshatra Dandgund

This program demonstrates how to:
- Access characters in a string using indexing
- Extract characters using negative indexing
- Iterate through a string using a `for` loop

---

## 📄 Code Explanation
The program:
1. Takes a name as input
2. Extracts the last and second-last characters
3. Prints each character of the string on a new line

```python
#Author: Nakshatra Dandgund
#Practicing slicing in python

name = input("Enter your name")

last = name[-1]
second_last = name[-2]

print("The last and second last letter of your name are", last, second_last)

print("The characters in your name are")
for character in name:
    print(character)
