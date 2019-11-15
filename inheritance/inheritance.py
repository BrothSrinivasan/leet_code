# Author: Barath Srinivasan

# Design the class structure for a banking system using object-oriented principles
# Your design must have at least 5 classes
# Each class must have at least 2 variables and 2 functions (doesn't need to be implemented, just declared)
# You must also use 1 enum

# Possible Clarifying Questions
"""
1) Are there different types of Accounts a person can hold?
2) Besides balance, what information should an account hold?
3) Should we implement any security features?
"""

# Possible Answers
"""
1) Yes. There is a basic checking and saving account. Then there is a premium version 
2) Each account needs an id, which needs to be unique, and needs to attached to a person. Person needs to present basic information to create his/her account
3) Try to protect sensitive information about the holder
"""

import hashlib
import enum


# enum defines the different currencies of the world
class Curr(Enum):
    USD = 0
    EUR = 1
    CNY = 2
    RUP = 3

# Corporate defines the corportate structure of the Bank
class Corporate:
    __CEO = "Barath Srinivasan" # notes the CEO of the bank
    __LocationofHQ = "College Park, MD" # notes the location of corporate HQ

    def oustCEO(new: str): # CEO is changed if method is call 
        pass;

    # allows to merge with another company
    def mergeCompanies(company: str):
        pass;

    # ...more functions possible... #

# BankSys is a central place for bank activties to take place. 
class BankSys:
    __currentInterestRate = 0.5 # current loan interest company of the bank
    __lastUpgrade = "9/27/19" # notes when last upgrade of the system took place

    # can allow for multiple branches with seperate accounts
    def __init__():
        accToName = {}

    # allows holder to create a specific account. accType can be "basic" or "premium"
    def createAcct(name: Holder, accId: int, acctType: str) -> Account:
        pass;

    # defines accounts for a transfer to take place and the amount to be transfered
    def transfer(recv: Account, send: Account, amount: int):
        pass;

    # ...more functions possible... #
    
# Holder defines an account holder. Holds information about them
class Holder:
    __accessRestriction = "low-access" # displays that they have low access unlike a CEO or manager
    __salt = "protecting our customers" # a salt to add to sensitive information
    
    # creates the account holder
    def __init_(self, fname: str, lname: str, dob: str, ssn: str):
        self.fname = fname
        self.lname = lname
        self.dob = hashlib.sha526(((dob + salt).encode()).hexdigest()) # hashing dob to protect holder
        self.ssn = hashlib.sha256(((ssn + salt).encode()).hexdigest()) # hashing ssn to protect ssn

    # changes name if holder chooses to wish
    def changeName(fname: str, lname: str):
        pass;

    # account holder can set up notifications by passing in phone number and email address in string format
    def setUpNotifications(phone: str, email: str):
        pass;

    # ...more functions possible... #

# Account is a base account holders can create
class Account:
    __accountCost = 10 # cost of running this type of account
    __minimumBalance = 15 # minimum money needed in account

    # creates this accout
    def __init__(self, name: Holder, accId: int):
        self.name = name
        self.accId = accId
        self.checking = 0
        self.saving = 0

    # allows to deposit or withdraw from either checking or saving
    def changeBalance(acctType: str, amount: int):
        pass;

    # allows holder to view balance of either checking or saving
    def viewBalance(acctType: str) -> str:
        pass;

    # ...more functions possible... #

# PremiumAcct extends Account in that in addition to the shared methods, those with premiumaccts have different cost, yet more functionality
class PremiumAcct(Account):
    __accountCost = 15 # overrides parent cost
    __minimumBalance = 5 # overrides parent minimumbalance

    # allows holder to convert currency
    def convertCurr(amount: int, curr: Curr) -> int:
        pass;

    # allows holder to apply for a loan. Takes in principal and time, and computes with it own interest rate.
    def applyLoan(princ: int, time: int) -> bool:
        pass;

    # ...more functions possible... #
