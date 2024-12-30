"""Import the Account class from the Account.py file."""

from Accounts import Account

def create_savings_account(balance, interest_rate):

    
    # 
    savings_account = Account(balance, interest_rate)
    
    # 
    interest_earned = savings_account.balance * savings_account.interest_rate
    
    # 
    updated_balance = savings_account.balance + interest_earned
    
    # 
    savings_account.set_balance(updated_balance)
    
    # 
    savings_account.set_interest(interest_earned)
    
    # 
    return updated_balance, interest_earned
