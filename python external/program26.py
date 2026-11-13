#26. program using Pandas to read student
# records from a CSV file and display the contents in tabular forma
import pandas as pd

# Create student records
data = {
    'Roll No': [1, 2, 3, 4],
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha'],
    'Marks': [85, 90, 78, 95]
}

# Create CSV file
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

# Read CSV file
df = pd.read_csv("students.csv")

# Display student records
print(df)