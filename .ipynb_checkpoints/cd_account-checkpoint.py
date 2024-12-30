# cd_account.py

# 1. Import the Account class from the Accounts.py file
from Accounts import Account

def create_cd_account(balance, interest_rate):
  
    
    # 
    cd_account = Account(balance, interest_rate)
    
    # 
    interest_earned = cd_account.balance * cd_account.interest_rate
    
    # 
    updated_balance = cd_account.balance + interest_earned
    
    # 
    cd_account.set_balance(updated_balance)
    
    # 
    cd_account.set_interest(interest_earned)
    
    # 
    return updated_balance, interest_earned
