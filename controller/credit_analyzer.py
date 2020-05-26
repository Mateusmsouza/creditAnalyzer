class CreditAnalyzer:

    def __init__(self, customer):
        self.customer = customer
        self.credit = 0

    def grant_credit(self):
        score = self.customer["score"]

        if score > 0 and score < 300:
            return False
        elif score > 299 and score < 600:
            self.credit = 1000
            return True
            
    def credit_granted(self):
        return self.credit