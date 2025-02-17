# Q1
import numpy as np
import matplotlib.pyplot as plt

M = float(input("Enter a value for M: "))

x = np.linspace(-10, 10, 100)
y1 = M * x**2
y2 = M * np.sin(x)

plt.plot(x, y1, color="blue", linestyle="-", label="y = M * x^2")
plt.plot(x, y2, color="red", linestyle="--", label="y = M * sin(x)")
plt.title("Mathematical Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Q2
import pandas as pd
import seaborn as sns

subjects = ["Math", "Physics", "Chemistry", "Biology", "Computer"]
scores = [85, 78, 92, 74, 88]

data = pd.DataFrame({"Subjects": subjects, "Scores": scores})

plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x="Subjects", y="Scores", data=data, palette="viridis")

for i in range(len(scores)):
    bar_plot.text(i, scores[i] + 1, str(scores[i]), ha="center")

plt.title("Scores in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# Q3
roll_number = 102317204
np.random.seed(roll_number)
data = np.random.randn(50)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(np.cumsum(data), color="green")
plt.title("Cumulative Sum")
plt.xlabel("Index")
plt.ylabel("Cumulative Sum")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.scatter(range(len(data)), data, color="purple")
plt.title("Random Noise")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)

plt.tight_layout()
plt.show()

# Q4
import seaborn as sns

data = pd.read_csv(
    "https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv"
)

plt.figure(figsize=(10, 6))
plt.plot(
    data["month_number"], data["total_profit"], color="blue", marker="o", linestyle="-"
)
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
for column in data.columns[1:-1]:
    plt.plot(data["month_number"], data[column], label=column)

plt.title("Product Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

data.plot(kind="bar", figsize=(15, 8))
plt.title("Company Sales Data")
plt.xlabel("Month")
plt.ylabel("Values")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
