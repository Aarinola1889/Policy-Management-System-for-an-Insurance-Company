#Insurance Policy Management System

Overview
This Project involve using object-oriented programming (OOP) principles in Python to design policy management system for an insurance company to manage policyholders, insurance products, and payments. This system consist three main classes:
1. Policyholder Management: This handles registration, suspension, and reactivation of policyholders.
2. Payment Management: This processes payments, issues payment reminders, and applies penalties if necessary
3. Product Management: This implement methods for creation, updating, and removal or suspension of insurance products.

Requirement
Ensure you have Python installed on your 

Files
- policyholder.py: Contains the Policyholder class to implement policyholder information and actions.
- Insurance_product.py: Contains the Product class to implement the insurance products.
- Insurance_payment.py: Contains the Payment class to implement payment processing.
- README.md: instructions on how to access and utilize the code

Method
 Policyholder.py: __init__(self, name): Initializes a policyholder with a name and an empty list of policies.
- add_policy(self, product, start_date, end_date): Add a new insurance policy for the policyholder.
- suspend(self): For suspending the policyholder account.
- reactivate(self): To Reactivates the policyholder account.

Insurance_Product.py: __init__(self, name, coverage_amount, premium): It will Initialize a new insurance product with a name, coverage amount, and premium.
suspend(self): It suspends the product from being available for sale.
update_coverage(self, new_coverage_amount): Updates the coverage amount of the product.


Insurance_Payment: __init__(self, amount, date): Initializes a payment with an amount and a date.
complete_payment(self): To Mark the payment status as "Completed".