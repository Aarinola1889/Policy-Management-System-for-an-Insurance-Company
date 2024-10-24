# class creation for insurance_product

class InsuranceProduct:
    def __init__(self, product_name, coverage_amount, premium):
        self.product_name = product_name
        self.coverage_amount = coverage_amount
        self.premium = premium
        self.active = True
        
def create_product(self):
        #Creates a new insurance product
        print(f"Insurance product {self.product_name} created.")

def update_product(self, new_coverage_amount, new_premium):
        #Updates the insurance product details
        self.coverage_amount = new_coverage_amount
        self.premium = new_premium
        print(f"Insurance product {self.product_name} updated.")

def remove_product(self):
        #Removes or suspends the insurance product
        self.active = False
        print(f"Insurance product {self.product_name} has been suspended.")

def display_product(self):
        #Displays the details of the insurance product.
        status = "Active" if self.active else "Suspended"
        print(f"Product: {self.product_name} ({status})")
        print(f"Coverage Amount: ${self.coverage_amount}")
        print(f"Premium: ${self.premium}")
