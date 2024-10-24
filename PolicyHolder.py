# class creation for policyholder

from PolicyHolder import Policy
class Policyholder:
    def __init__(self, policyholder_name, policyholder_id, contact_info):
        self.policyholder_name = policyholder_name
        self.policyholder_id = policyholder_id
        self.contact_info = contact_info
        self.policies = []
        self.active = True
        
def register_policyholder(self):
    #Registering a new policyholder
        print(f"Policyholder {self.policyholder_name} has been registered successfully.")

def suspend_policyholder(self):
        #Suspends the policyholder
        self.active = False
        print(f"Policyholder {self.policyholder_name} has been suspended.")

def add_policy(self, policy):
        #Adds a policy to the policyholder's list of policies.
        self.policies.append(policy)

def view_policies(self):
        #Displays all the policies the policyholder has.
        if not self.policies:
            print(f"{self.policyholder_name} has no active policies.")
        else:
            print(f"{self.policyholder_name}'s policies:")
            for policy in self.policies:
                policy.display_policy()

def view_contact_info(self):
        print(f"Contact Info for {self.policyholder_name}: {self.contact_info}")

