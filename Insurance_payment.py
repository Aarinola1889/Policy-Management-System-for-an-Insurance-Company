# class creation for insurance_payment.py

class Insurance_Payment:
    def __init__(self, payment_date, amount):
        self.payment_date = payment_date
        self.amount = amount
        
def process_payment(self):
        #Processes the payment
        self.status = "Completed"
        print(f"Payment of ${self.amount} on {self.payment_date} processed.")

def payment_reminder(self):
        #Sends a reminder for payment
        if self.status == "Pending":
            print(f"Reminder: Payment of ${self.amount} is due on {self.payment_date}.")

def apply_penalty(self, penalty_amount):
        #Applies a penalty to the payment
        self.amount += penalty_amount
        print(f"A penalty of ${penalty_amount} has been applied. New amount due: ${self.amount}.")

def display_payment(self):
        #Displays payment details.
        print(f"Payment Date: {self.payment_date}, Amount: ${self.amount}, Status: {self.status}")

