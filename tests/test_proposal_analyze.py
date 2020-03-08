import pytest
from controller.proposal_controller import Proposal

def test_controller_proposal_with_one_analyze_should_reprove_proposal():
    
    # arrange
    customer = {
        "name": "Mateus Souza",
        "address": "Planeta Terra",
        "phone": "+5512999999999",
        "salary": 0,
        "score": 1
    }
    
    proposal_controller = Proposal(customer)
    
    # act
    analyze_result = proposal_controller.can_customer_receive_credit()
    
    # assert
    assert analyze_result is False, "Proposal analyze not working with customer score 1"

def test_controller_proposal_analyze_should_reprove_proposal():
    
    # arrange
    customer = {
        "name": "Mateus Souza",
        "address": "Planeta Terra",
        "phone": "+5512999999999",
        "salary": 0,
        "score": 299
    }
    
    proposal_controller = Proposal(customer)
    
    # act
    analyze_result = proposal_controller.can_customer_receive_credit()
    
    # assert
    assert analyze_result is False, "Proposal analyze not working with customer score 299"

def test_controller_proposal_with_three_hundred_analyze_should_approve_proposal():
    
    # arrange
    customer = {
        "name": "Mateus Souza",
        "address": "Planeta Terra",
        "phone": "+5512999999999",
        "salary": 0,
        "score": 300
    }
    
    proposal_controller = Proposal(customer)
    
    # act
    analyze_result = proposal_controller.can_customer_receive_credit()
    
    # assert
    assert analyze_result is True, "Proposal analyze not approving with customer score 300"
    assert proposal_controller.get_granted_credit() == 1000

def test_controller_proposal_with_five_hundred_ninety_nine_analyze_should_approve_proposal():
    
    # arrange
    customer = { "name": "Mateus Souza", "address": "Planeta Terra", "phone": "+5512999999999", "salary": 0, "score": 599 }
    
    proposal_controller = Proposal(customer)
    
    # act
    analyze_result = proposal_controller.can_customer_receive_credit()
    
    # assert
    assert analyze_result is True, "Proposal analyze not approving with customer score 599"
    assert proposal_controller.get_granted_credit() == 1000

def test_controller_proposal_with_six_hundred_analyze_should_approve_proposal():
    
    # arrange
    customer = { "name": "Mateus Souza", "address": "Planeta Terra", "phone": "+5512999999999", "salary": 5000, "score": 600 }
    
    proposal_controller = Proposal(customer)
    
    # act
    analyze_result = proposal_controller.can_customer_receive_credit()
    
    # assert
    assert analyze_result is True, "Proposal analyze not approving with customer score 600"
    assert proposal_controller.get_granted_credit() == customer["salary"]/2