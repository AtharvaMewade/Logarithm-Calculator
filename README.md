LOGARITHM CALCULATOR

This is a lightweight Command Line Interface (CLI) Python program I built during my 10th-grade year to merge my algebra studies with introductory computer science logic.

💡 PURPOSE
I designed this tool for students working on logarithmic problems who know the initial equations but are uncertain of their final calculations. It serves as an automated utility to instantly cross-check and verify answers.

🛠️ HOW IT WORKS

The program offers three straightforward execution paths depending on the unknown value:
1. **Find Base (Option 1):** Approximates an unknown base using **Bisection Search** (binary search) logic. By splitting the search bounds in half dynamically, it calculates values with efficient **$O(\log n)$ time complexity**.
2. **Find Target (Option 2):** Calculates the final exponential result by continuously multiplying the base across the step count.
3. **Find Steps (Option 3):** Determines the numerical exponent required by continuously dividing the target by its base.
4. More details, ready comments side by side to understand mechanism

📜 LICENSE
This project is distributed under the open-source MIT License.

💡 Project Background & Inspiration
This project was directly inspired by **MIT OpenCourseWare's 6.0001 (Fall 2016) Problem Set 0**. While the official assignment instructs students to simply use a built-in library to print a logarithm value, I wanted to challenge myself by building the underlying mathematical engine from scratch. 

Instead of relying on standard imports, I implemented a custom **Bisection Search** loop to natively calculate logarithm components with an optimized **$O(\log n)$ time complexity**.
