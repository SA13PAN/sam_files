import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name": ["John","Suresh","Ramesh","Jessica","Jennifer","Annu","pooja","Ritesh","Farha","Mukesh"],
    "Maths": [55,75,25,78,58,45,55,54,55,96],
    "Physics": [45,96,54,96,96,87,64,76,63,46],
    "Chemistry": [56,78,89,86,78,52,61,87,89,77],
    "English": [87,64,76,63,46,89,58,56,75,83],
    "Biology": [21,90,95,54,96,55,75,25,78,58],
    "Economics": [52,61,87,89,77,89,58,56,75,83],
    "History": [89,58,56,75,83,87,64,76,63,46],
    "Civics": [65,2,74,45,53,52,61,87,89,77]
}

df = pd.DataFrame(data)
df.to_csv("STUDENTSMARKS.csv", index=False)

df = pd.read_csv("STUDENTSMARKS.csv")
print(df)

subjects = ["Maths", "Physics", "Chemistry", "English", "Biology"]

average_marks = np.mean(df[subjects], axis=0)
max_marks = np.max(df[subjects], axis=0)
min_marks = np.min(df[subjects], axis=0)

print("\nAverage Marks:")
print(average_marks)

print("\nMaximum Marks:")
print(max_marks)

print("\nMinimum Marks:")
print(min_marks)

plt.figure()
plt.bar(subjects, average_marks)
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

df["Total Marks"] = df[subjects].sum(axis=1)

plt.figure()
plt.bar(df["Name"], df["Total Marks"])
plt.title("Students Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.show()