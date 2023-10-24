# Welcome to the amortization interest tracker!
# Error as interest rate is not considered

p = float(input("Enter the loan amount: "))
apr = float(input("Enter the APR (Annual percentage rate): "))
n = int(input("Enter the compound period (1, 4, 12, 365): "))
t = int(input("Enter the repayment period (in years): "))
apr = round(apr / 100 / n, 5)

c = (p * apr) / (1 - 1 / (1 + apr) ** (n * t))
print('The monthly cash flow is ${c}'.format(c=round(c, 2)))

interest_month = int(input('Which period do you want to know the interest amount? (Input an integer): '))
interest = (p - c*(interest_month - 1))* apr
print('The interest in the {} period is ${}'.format(interest_month, round(interest, 2)))
# def amount(principal, pmt):
#     for i in range(1, n*t + 1):
#         principal -= pmt
#         amount(principal, pmt)
#     if p <= 0:
#         return
#     return
#
# print(amount(p, c))