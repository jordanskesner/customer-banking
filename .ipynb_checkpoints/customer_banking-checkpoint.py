# customer_banking.py

# import
from cd_account import create_cd_account
from savings_account import create_savings_account

def main():
    # savings account
    # Prompt the user to set the savings balance, interest rate, and months
    savings_balance = float(input("Enter Savings Account balance: "))
    savings_interest_rate = float(input("Enter Savings Account interest rate (e.g., 0.05 for 5%): "))
    savings_months = int(input("Enter the number of months for the Savings Account: "))
    
    # call create savings function
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate)
    
    # 
    print(f"\n--- Savings Account Summary ---")
    print(f"Months: {savings_months}")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Balance: ${updated_savings_balance:.2f}\n")
    
    ## CD account
    # 
    cd_balance = float(input("Enter CD Account balance: "))
    cd_interest_rate = float(input("Enter CD Account interest rate (e.g., 0.05 for 5%): "))
    cd_months = int(input("Enter the number of months for the CD Account: "))
    
    # Call the create_cd_account function, passing the user inputs
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate)
    
    # Print 
    print(f"\n--- CD Account Summary ---")
    print(f"Months: {cd_months}")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Balance: ${updated_cd_balance:.2f}")

# 
if __name__ == "__main__":
    main()
