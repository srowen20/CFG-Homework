# TASK 1: GIT AND GITHUB

"""
Question 1
Complete definitions for key Git & GitHub terminology

GIT WORKFLOW FUNDAMENTALS

·        Working Directory
Repositories built using the git init command are working directories until they are committed. They are what
you can see, and where you can add, delete, edit and move files while you are working on a project. Files that
were not in the last snapshot and are not in the staging area are usually what you have in your working
directory. You can clean the working directory by staging then committing all files in it.

·        Staging Area
When files are staged they start getting tracked. It gives you control over what you commit next, and once
you’ve decided the files in there are right you can commit them. Files not added to the staging area before a
commit can be added to a future commit. It’s a step to combining multiple files in one commit so they become
part of the same stage of a project.

·        Local Repo (head)
Head refers to the most recent commit and tells us what we’ve just checked out. It can be the same commit as the
master. Local repo could be a directory in our local system, and cannot be seen by collaborators in our remote
repository until we push.

·        Remote repo (master)
The master is automatically set to the first commit. If we stay on this commit, each branch usually joins to
this. A remote repository in another location to where we’re currently working, that other collaborators can
access.


WORKING DIRECTORY STATES:

·        Staged
The file has been added to the staging area i.e. it’s now being tracked, but hasn’t been committed. Files can
still be modified, deleted or replaced. You can add untracked or modified files to the staging area.

·        Modified
Changes have been made to the file in the staging area in the working directory that haven’t been committed yet.
This can be undone to the original staged file. By undoing this you clean the working tree.

·        Committed
 	Changes to the file are saved as a snapshot in the repository for good. You can revert to each commit at any
 	point in time.


GIT COMMANDS:

·        Git add
This is how you make untracked files into tracked files. It adds files from the working directory to the staging
area, then they’re ready to commit.

·        Git commit
Takes a snapshot of your files in the staging area at any time. These snapshots are called commits. You can always
go back to this point, as it essentially saves your place. Once committed, you can make changes and commit again,
so you have multiple commits. It logs who made changes and when. You usually commit when a logical piece of work
has been done, so you save a stage of your project. Git commit commits whatever is within the staging area.

·        Git push
Used to publish changes made in the local repository, usually on your computer, to the remote repository. As soon
as you push, your changes are shared with the rest of the team.

·        Git fetch
Git doesn’t automatically check what is stored remotely. Git fetch origin can be used to see what is in the remote
repository.

·        Git merge
Combines changes made on a branch that separated from the master, with the master. This result is recorded in it’s
own commit which includes the names of the commits which merged to form it. You can then delete the branched
commit. Catches you up to where the remote repository is.

·        Git pull
Checks what is in your remote branch and downloads it to the local branch, then merges the changes with your local
repository. Combines fetch and merge into one command. However, it can be messy so is better to use fetch and merge
separately so you can more easily see what you’re merging.
"""


# TASK 2: EXCEPTION HANDLING

"""
Question 1: Simple ATM Program
Using exception handling code blocks such as try/ except / else / finally (NB: the 
more the better, but try to use at least two key words e.g. try/except) write a 
program that simulates and ATM machine to withdraw money.
Tasks:
1.       Prompt user for a pin code
2.       If the pin code is correct then proceed to the next step, otherwise ask a 
user to type in a password again. You can give a user a maximum of 3 attempts and 
then exit a program.
3.       Set account balance to 100.
4.       Now we need to simulate cash withdrawal
5.       Accept the withdrawal amount
6.       Subtract the amount from the account balance and display the remaining 
balance (NOTE! The balance cannot be negative!)
7.       However, when a user asks to ‘withdraw’ more money than they have on their 
account, then you need to raise an error an exit the program. 

"""
# Aware that import sys is helpful to exit the code but this doesn't exist in the PyCharm packages available on my laptop
import sys
from sys import exit

# Set the actual pin and count to 0
real_pin = 1234
count = 0


def withdraw_money(account_balance):

    # User says how much they want to withdraw
    amount = int(input('How much would you like to withdraw? (£) '))

    # Raise an exception if they try to enter a negative amount
    if amount < 0:
        raise Exception
    try:
        #Calculate the new balance based on the requested withdrawal amount
        new_balance = account_balance - amount

        # If the new balance is negative give them the opportunity to stop the transaction. End the code if they try,
        # or allow them to try entering a new amount if they say no until they enter a valid amount.
        while new_balance < 0:
            print('NOTE! You are trying to withdraw more money than you have! Your new balance would be {}'.format(new_balance))
            decision = input('Would you like to continue? (y/n) ')
            if decision.lower() == 'y':
                print('It is not possible to have a negative account balance.')
                raise Exception
            elif decision.lower() == 'n':
                amount = int(input('How much would you like to withdraw? (£) '))
            else:
                print('This is not a valid input. Ending transaction.')
                raise ValueError

    # End the code if there's an exception
    except:
        exit()
    else:
        # Print the new balance
        print('Your new balance is: £' + str(new_balance))
    finally:
        # Complete the transaction
        print('Your transaction is now complete. Thank you for using this ATM.')


def enter_pin(attempt, actual_pin):
    # Set the balance to 100
    balance = 100
    try:
        # Try entering the pin numbers until you reach three attempts then stop the code from running
        while attempt < 3:
            pin_code = int(input('Please enter your pin: '))

            if pin_code == actual_pin:
                print('Pin Correct')
                break # once the pin is correct
            else:
                wrong = 'Incorrect Pin. Try again.'
                print(wrong)
                attempt += 1

        if attempt >= 3:
            raise Exception
        withdraw_money(balance)

    except:
        print('You inserted your pin incorrectly too many times. Exiting withdrawal request. Number of attempts = {}'.format(attempt))

# enter_pin(0, 1234)

# FUNCTIONS FOR TESTING - EXCLUDING USER INPUT


def withdraw_money_no_user_input(account_balance, amount, decision, amount2):

    try:
        if amount < 0:
            raise Exception
        new_balance = account_balance - amount
        while new_balance < 0:
            print('NOTE! You are trying to withdraw more money than you have! Your new balance would be {}'.format(new_balance))
            if decision.lower() == 'y':
                response = 'It is not possible to have a negative account balance.'
                print(response)
                raise Exception
            elif decision.lower() == 'n':
                amount = amount2
                new_balance = account_balance - amount
            else:
                print('This is not a valid input. Ending transaction.')
                return ValueError
    except:
        output = ' exception'
        return 'It is not possible to have a negative account balance.'
    else:
        print('Your new balance is: £' + str(new_balance))
        output = ''
    finally:
        final = ('Your transaction is now complete. Thank you for using this ATM.' + output)
        print(final)
        return final


def enter_pin_no_user_input(attempt, actual_pin, pin_code, withdrawal_amount, user_decision):
    balance = 100
    try:

        for pin in pin_code:

            if pin == actual_pin:
                print('Pin Correct')
                response = withdraw_money_no_user_input(balance, withdrawal_amount, user_decision, 0)
                return response
            else:
                response = 'Incorrect Pin. Try again.'
                print(response)
                attempt += 1

        if attempt >= 3:
            raise Exception

    except:
        response = 'You inserted your pin incorrectly too many times. Exiting withdrawal request. Number of attempts = {}'.format(attempt)
        print(response)
    else:
        return response
    finally:
        return response


import unittest

# TASK 3: Testing

"""
Question 1
Use the Simple ATM program to write unit tests for your functions.
You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of 
code to make it easier to write tests.
Try to write at least 5 unit tests in total covering various cases. 
"""

from Week_4_homework_SO import enter_pin_no_user_input, withdraw_money_no_user_input


class TestATMFunction(unittest.TestCase):

    # Testing the same incorrect pin
    def test_wrong_pin_three_times(self):
        pins = [1432, 1432, 1432]
        expected = 'You inserted your pin incorrectly too many times. Exiting withdrawal request. Number of attempts = 3'
        result = enter_pin_no_user_input(attempt=0, actual_pin=1321, pin_code=pins, withdrawal_amount=0, user_decision='n')
        self.assertEqual(expected, result)

    def test_not_y_or_n(self):
        expected = 'Your transaction is now complete. Thank you for using this ATM. exception'
        result = withdraw_money_no_user_input(account_balance=100, amount=120, decision='y', amount2=0)
        self.assertEqual(expected, result)

    def test_trying_to_withdraw_too_much_and_continuing(self):
        expected = 'Your transaction is now complete. Thank you for using this ATM. exception'
        result = withdraw_money_no_user_input(account_balance=100, amount=120, decision='y', amount2=0)
        self.assertEqual(expected, result)

    def test_wrong_withdrawal_right(self):
        expected = 'Your transaction is now complete. Thank you for using this ATM.'
        result = withdraw_money_no_user_input(account_balance=100, amount=120, decision='n', amount2=50)
        self.assertEqual(expected, result)

    def test_everything_input_correctly(self):
        expected = 'Your transaction is now complete. Thank you for using this ATM.'
        result = enter_pin_no_user_input(attempt=0, actual_pin=1234, pin_code=[1234], withdrawal_amount=50, user_decision='n')
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
