import pandas as pd
from datetime import datetime

def process_employee_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    
    print("Original DataFrame:")
    print(df)
    
    dept_salary_total = df.groupby('Department')['Salary'].sum().reset_index()
    print("\n1. Total Salary per Department:")
    print(dept_salary_total)
    
    df['Date of Joining'] = pd.to_datetime(df['Date of Joining'])
    
    current_date = datetime.now()
    df['Tenure (Years)'] = (current_date - df['Date of Joining']).dt.days / 365.25
    
    tenured_employees = df[df['Tenure (Years)'] > 2]
    print("\n2. Employees with more than 2 years of tenure:")
    print(tenured_employees[['Name', 'Department', 'Date of Joining', 'Tenure (Years)']])
    
    top_paid_employees = df.nlargest(3, 'Salary')
    print("\n3. Top 3 highest-paid employees:")
    print(top_paid_employees[['Name', 'Department', 'Salary']])
    
    df['Annual Salary'] = df['Salary'] * 6
    print("\n4. DataFrame with Annual Salary column:")
    print(df[['Name', 'Salary', 'Annual Salary']])
    
    dept_avg_salary = df.groupby('Department')['Salary'].mean().reset_index()
    print("\n5. Average Salary per Department:")
    print(dept_avg_salary)
    
    return df

if __name__ == "__main__":
    file_path = r"C:\Users\Mitalee Shirsat\OneDrive\Desktop\Nobias\sample_data.csv"
    result_df = process_employee_data(file_path)
    print("\nFinal processed DataFrame:")
    print(result_df)