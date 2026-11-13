# 🧮 Python Scientific Calculator

A sleek, fully functional **Scientific Calculator** built using Python and the Tkinter GUI library. This desktop application goes beyond basic arithmetic, offering advanced mathematical functions wrapped in a modern, dark-themed user interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## ✨ Features

### 🔢 Basic Operations
*   **Addition, Subtraction, Multiplication, Division**
*   **Decimal Support** for precise calculations
*   **Clear (C) button** to reset the calculator instantly

### 📐 Advanced Mathematical Functions
*   **Square Root (√):** Accurately calculates the root of any positive number.
*   **Square (x²):** Instantly squares the current value.
*   **Logarithm (log):** Base-10 logarithm calculations (with error handling for negative numbers).
*   **Trigonometry:** Dedicated buttons for **Sine (sin)**, **Cosine (cos)**, and **Tangent (tan)**. 
    *   *Note: Calculations are automatically converted to degrees.*
*   **Pi (π):** Insert the value of Pi directly into your expression.

### 🛡️ Robust Error Handling
The calculator doesn't just crash when you give it bad input. It features custom error handling:
*   Prevents division by zero.
*   Catches invalid mathematical expressions (e.g., `5 ++ 3`).
*   Blocks negative number square roots.
*   Displays user-friendly error popups via `messagebox`.

---

## 🎨 UI/UX Design

*   **Modern Dark Theme:** Easy on the eyes with a deep charcoal background (`#1e1e1e`) and high-contrast white text.
*   **Color-Coded Buttons:** 
    *   🟠 **Orange:** Equals (`=`) for quick visual recognition.
    *   🔴 **Red:** Clear (`C`) for emergency resets.
    *   ⬛ **Dark Grey:** Standard numbers and operators.
    *   🔲 **Light Grey:** Advanced scientific functions.
*   **Fixed Aspect Ratio:** The window is non-resizable to ensure the grid layout remains perfectly intact on all screens.

---

## 🛠️ Tech Stack

*   **Language:** Python 3
*   **GUI Library:** Tkinter (Standard Python Interface to Tk GUI toolkit)
*   **Math Module:** Python's built-in `math` library for advanced calculations.

---

## 🚀 How to Run Locally

Follow these simple steps to run the calculator on your machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dimpal-Sharma231/Python-Scientific-Calculator.git
