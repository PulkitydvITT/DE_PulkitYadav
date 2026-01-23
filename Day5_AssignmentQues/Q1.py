import pandas as pd

data = {
    'Student': ['Pulkit', 'Pawan', 'Pulkit', 'Kunal', 'Pawan', 'Kunal'],
    'Subject': ['Java', 'Cpp', 'Cpp', 'Cpp', 'Java', 'Java'],
    'Score': [85, 90, 95, 80, 90, 88]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

pivot_table = df.pivot_table(index='Student', columns='Subject', values='Score', aggfunc='mean')
print("\nPivot Table:\n", pivot_table)
