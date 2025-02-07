import pandas as pd

n = int(input("Enter the number of entries: "))

w = float(input("Enter weight: "))

income = []
members = []
avg_age = []
expenses = []

for i in range(n):
    print(f"Enter data for entry {i+1}:")
    income_value = float(input("Income: "))
    members_value = int(input("Number of Family Members: "))
    avg_age_value = float(input("Average Age: "))
    
    income.append(income_value)
    members.append(members_value)
    avg_age.append(avg_age_value)

    expense = w * (income_value + members_value + avg_age_value)
    expenses.append(expense)

# Create a DataFrame to store the data
df = pd.DataFrame({
    'Income': income,
    'Family Members': members,
    'Average Age': avg_age,
    'Expenses': expenses
})

# Display the DataFrame
print("\nYour DataFrame with Expenses:")
print(df)

# mean
def mean(data):
    return sum(data) / len(data)

# correlation
def correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    
    a = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    cov = a/(len(x)-1)

    var_x = sum((x[i] - mean_x) ** 2 for i in range(len(x)))
    sigma_x = (var_x / len(x)) ** 0.5
    
    var_y = sum((y[i] - mean_y) ** 2 for i in range(len(y)))
    sigma_y = (var_y / len(y)) ** 0.5
    
    correl = cov / (sigma_x * sigma_y)
    
    return correl

# Calculate the mean for each feature
mean_income = mean(income)
mean_members = mean(members)
mean_avg_age =mean(avg_age)

# Calculate the correlation between features
correlation_income_members = correlation(income, members)
correlation_income_avg_age = correlation(income, avg_age)
correlation_members_avg_age = correlation(members, avg_age)

# Print the mean and correlation values
print(f"\nMean of Income: {mean_income}")
print(f"Mean of Family Members: {mean_members}")
print(f"Mean of Average Age: {mean_avg_age}")

print("\nCorrelation between the features:")
print(f"Correlation between Income and Family Members: {correlation_income_members}")
print(f"Correlation between Income and Average Age: {correlation_income_avg_age}")
print(f"Correlation between Family Members and Average Age: {correlation_members_avg_age}")

def predict(x,y,z):
    expenses = w*(x+y+z)
    return expenses

income = float(input("Income: "))
members = int(input("Number of Family Members: "))
avg_age = float(input("Average Age: "))
predicted_expenses = predict(income,members,avg_age)
print("Expense(",income,",",members,",",avg_age,") = ",predicted_expenses)