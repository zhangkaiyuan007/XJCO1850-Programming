class Transaction:
    def __init__(self, tid, amt, date, description):
        self.transaction_id = tid
        self.amount = amt
        self.date = date
        self.description = description

# define the __str__ and __repr__ in the following format:
# (1) __str__: Transaction T123 on 2023-11-05 for £500.00 for Rent
# (2) __repr__: Transaction(tid='T123', amt=500.00, date='2023-11-05', description='Rent')
