from controller.credit_analyzer import CreditAnalyzer

def test_score_1_should_not_grant_credit():
    customer = { "score": 1, "salary": 1000 }
    controller_credit_analyzer = CreditAnalyzer(customer)
    assert controller_credit_analyzer.grant_credit() is False

def test_score_299_should_not_grant_credit():
    customer = { "score": 299, "salary": 1000 }
    controller_credit_analyzer = CreditAnalyzer(customer)
    assert controller_credit_analyzer.grant_credit() is False

def test_score_300_should_grant_credit():
    customer = { "score": 300, "salary": 1000 }
    controller_credit_analyzer = CreditAnalyzer(customer)
    assert controller_credit_analyzer.grant_credit() is True
    assert controller_credit_analyzer.credit_granted() == 1000

def test_score_599_should_grant_credit():
    customer = { "score": 599, "salary": 1000 }
    controller_credit_analyzer = CreditAnalyzer(customer)
    assert controller_credit_analyzer.grant_credit() is True
    assert controller_credit_analyzer.credit_granted() == 1000

def test_score_600_should_grant_credit():
    customer = { "score": 600, "salary": 1000 }
    controller_credit_analyzer = CreditAnalyzer(customer)
    assert controller_credit_analyzer.grant_credit() is True
    assert controller_credit_analyzer.credit_granted() == 2500