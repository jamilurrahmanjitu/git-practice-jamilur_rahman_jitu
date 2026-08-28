from datetime import date
from utils import add, subtract
from utils import add, subtract, multiply
from utils import add, subtract, multiply, divide

print("Name: Jamilur Rahman Jitu")
print(f"Today's date: {date.today()}")

print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")