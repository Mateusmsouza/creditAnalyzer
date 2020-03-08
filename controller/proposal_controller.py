class Proposal():

    def __init__(self, customer):
        self.customer = customer
        self.credit_granted = 0
    
    def __is_between(self, value, border_x, border_y):
        return value > border_x and value < border_y 
    
    def __set_credit_and_return_true(self, credit):
        self.credit_granted = credit
        return True

    def can_customer_receive_credit(self):
        score = self.customer["score"]
        salary = self.customer["salary"]

        if self.__is_between(score, -1, 300): 
            return False
            
        elif self.__is_between(score, 299, 600):
            return self.__set_credit_and_return_true(1000)

        elif score > 599:
            return self.__set_credit_and_return_true(salary/2)

    def get_granted_credit(self):
        return self.credit_granted
