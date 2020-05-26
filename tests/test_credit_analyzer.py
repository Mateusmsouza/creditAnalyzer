from controller.credit_analyzer import CreditAnalyzer

def test_score_1_should_not_grant_credit():
    customer = { "score": 1, "salary": 1000 }
    controller_credit_analyzer = CreditAnalyzer(customer)
    assert controller_credit_analyzer.grant_credit() is False
