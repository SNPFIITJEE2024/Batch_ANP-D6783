#Problem Statement: Accept: • Employee Name • Basic Salary Calculate: Component Percentage HRA 20% DA 10% PF Deduction 12% Display: • Gross Salary • Net Salary Additionally: Net Salary > 50000 → Senior Grade Net Salary > 30000 → Mid Grade Else → Junior Grade
# --- Step 1: Accept Inputs from the User ---
emp_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

# --- Step 2: Calculate Salary Components ---
# Allowances are additions to the basic salary
hra = basic_salary * 0.20  # House Rent Allowance (20%)
da = basic_salary * 0.10   # Dearness Allowance (10%)

# Deductions are taken away from the salary
pf_deduction = basic_salary * 0.12  # Provident Fund Deduction (12%)

# --- Step 3: Compute Gross and Net Salary ---
# Gross Salary is the total earnings before any deductions
gross_salary = basic_salary + hra + da

# Net Salary is the actual take-home money after deductions
net_salary = gross_salary - pf_deduction

# --- Step 4: Determine Employee Grade Based on Net Salary ---
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# --- Step 5: Display the Payslip ---
print("\n" + "="*15 + " EMPLOYEE PAYSLIP " + "="*15)
print(f"Employee Name : {emp_name}")
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print("-" * 48)
print(f"HRA (20%)     : +₹{hra:.2f}")
print(f"DA (10%)      : +₹{da:.2f}")
print(f"PF (12%)      : -₹{pf_deduction:.2f}")
print("-" * 48)
print(f"Gross Salary  : ₹{gross_salary:.2f}")
print(f"Net Salary    : ₹{net_salary:.2f}")
print(f"Employee Grade: {grade}")
print("=" * 48)