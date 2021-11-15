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
