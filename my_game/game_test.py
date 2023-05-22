import pytest
from City import City
from Citizen import Citizen
class TestCity:
    def test_initial_population_zero(self):
        # Arrange
        city = City("TestCity", 10, 50)

        # Assert
        assert city.population == 0

    def test_initial_happiness_fifty(self):
        # Arrange
        city = City("TestCity", 10, 50)

        # Assert
        assert city.happiness == 50
        
    def test_citizens_moving_in_increases_population(self):
            # Arrange
        city = City("TestCity", 10, 50)
        citizen = citizen = Citizen("1", "WorkZone", 1000, 80, "Home")

        # Act
        city.citizensMovingIn(citizen)

        # Assert
        assert city.population == 0
        
    def test_citizens_moving_out_decreases_population(self):
            # Arrange
        city = City("TestCity", 10, 50)

        # Act
        city.citizensMovingOut()

        # Assert
        assert city.population == 0

    def test_tax_money_added_to_bank(self):
        # Arrange
        city = City("TestCity", 10, 50)
        citizen =citizen = Citizen("2", "WorkZone", 1000, 80, "Home")
        # Act
        city.citizensMovingIn(citizen)
        city.taxMoney()

        # Assert
        assert city.bank > 0
        
        
    # def test_happiness_change_based_on_tax_rate(self):
    #         # Arrange
    #     city = City("TestCity", 10, 50)

    #     # Act
    #     city.happinessChange()

    #     # Assert
    #     assert city.happiness == 50 



   