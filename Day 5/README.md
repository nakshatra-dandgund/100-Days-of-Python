# 🧾 Python Journey - Day 5

Welcome to **Day 5** of my Python learning journey!
I am following the **100 Days of Code – Python** series by **Code With Harry**.
This repository contains my practice code for **Day 10 concepts**, uploaded as Day 5 on GitHub.

---

## 🧠 Project Overview
**Project Name:** Simple Billing System
**File Name:** `main.py`
**Author:** Nakshatra Dandgund

This program generates a basic bill by taking user input such as name, product, price, and quantity, then calculating the total cost.

---

## 📄 Code Explanation
The program:
- Takes user input using `input()`
- Converts values using `int()` and `float()`
- Performs arithmetic calculations
- Displays formatted bill output

```python
#author: Nakshatra Dandgund
#taking user input

name = input("Enter your name")
product = input("Enter the product name")
price = float(input("Enter the price of the product"))
pieces = int(input("Enter the number of pieces you have bought"))

total_cost = price * pieces

print("-------------- The Bill -----------------------")
print("name :", name)
print("product name", product)
print("The price of the product", price)
print("the number of", product, "pieces bought", pieces)
print("The total cost =", total_cost)
