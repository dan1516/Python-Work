while (monthly_investment := float(input("Enter monthly investment amount: "))) <= 0:
    print("Monthly investment must be a positive number.")
    monthly_investment = float(input("Enter monthly investment amount: "))
while (yearly_interest_rate := float(input("Enter the annual interest rate: "))) <= 0:
    print("Interest rate must be a positive number.")
    yearly_interest_rate = float(input("Enter the annual interest rate: "))
while (investment_years := int(input("Enter number of years: "))) <= 0:
    print("Investment years must be a positive number of years.")
    investment_years = int(input("Enter number of years: ")) 
for month in range(1, investment_years * 12 + 1):
    Final_amount = monthly_investment * ((1 + (yearly_interest_rate / 100) / 12) ** (month * investment_years))
    print(f'Month {month}: ${Final_amount:.2f}')
print(f'After {investment_years} years, your investment will be worth: ${Final_amount:.2f} at a yearly rate of {yearly_interest_rate}%.')