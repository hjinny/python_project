
monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

#세금 계산 = takes profit returns tax_amount
def get_tax_amount(profit) :
  if profit > 100000 : 
    tax_credits = 0.25
  else : 
    tax_credits = 0.15

  tax_amount = profit * tax_credits
  return tax_amount


#연간 매출 계산 = takes monthly_revenue and returns revenue for a year
def get_yearly_revenue(monthly_revenue) :
 return monthly_revenue*12

#연간 비용 계산 = takes monthly_expenses returns expenses for a year
def get_yearly_expenses(monthly_expenses) :
 return monthly_expenses*12

#세액 공제 적용 = takes tax_amount and tax_credits returns amount to discount
def apply_tax_credits(tax_amount, tax_credits) :
  return tax_amount*tax_credits


#이익 = 연간 매출 - 연간 비용
profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)
tax_amount = get_tax_amount(profit)

#print("이익=", profit, ", 세금=",tax_amount,", 세율=", tax_credits)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")


