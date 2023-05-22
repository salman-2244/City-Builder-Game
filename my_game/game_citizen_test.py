import sys
sys.path.append('./my_game')  # importing sys library
import pytest
from Citizen import Citizen

class TestCitizen:
    def test_citizen_instance_creation(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")

        # Assert
        assert citizen.id == "1"
        assert citizen.workZone == "WorkZone"
        assert citizen.salary == 1000
        assert citizen.happy == 80
        assert citizen.home == "Home"

    def test_citizen_to_dict(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")

        # Act
        citizen_dict = citizen.toDict()

        # Assert
        assert citizen_dict == {
            "id": "1",
            "workZone": "WorkZone",
            "salary": 1000,
            "happy": 80,
            "home": "Home"
        }

    def test_calc_happy_with_positive_salary_and_tax(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = 20
        distance = 5

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 799.5

    def test_calc_happy_with_zero_salary(self):
        # Arrange
        citizen = Citizen("4", "WorkZone", 0, 80, "Home")
        salary = 0
        tax = 20
        distance = 5

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0

    def test_calc_happy_with_zero_distance(self):
        # Arrange
        citizen = Citizen("23", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = 20
        distance = 0

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0

    def test_calc_happy_with_negative_happiness(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = 20
        distance = 15

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 798.5

    def test_calc_happy_with_unemployed_citizen(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 0
        tax = 20
        distance = 10

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0

    def test_calc_happy_with_negative_tax(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = -20
        distance = 10

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 1199.0

    def test_calc_happy_with_zero_distance_and_salary(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 0, 80, "Home")
        salary = 0
        tax = 20
        distance = 0

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0
        
 ########################################
    def test_creation_of_citizen_with_default_values(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")

        # Assert
        assert citizen.id == "1"
        assert citizen.workZone == "WorkZone"
        assert citizen.salary == 1000
        assert citizen.happy == 80
        assert citizen.home == "Home"

    def test_conversion_of_citizen_to_dict(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")

        # Act
        citizen_dict = citizen.toDict()

        # Assert
        assert citizen_dict == {
            "id": "1",
            "workZone": "WorkZone",
            "salary": 1000,
            "happy": 80,
            "home": "Home"
        }

    def test_calculation_of_happiness_with_positive_salary_and_tax(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = 20
        distance = 5

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 799.5

    def test_calculation_of_happiness_with_zero_salary(self):
        # Arrange
        citizen = Citizen("4", "WorkZone", 0, 80, "Home")
        salary = 0
        tax = 20
        distance = 5

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0

    def test_calculation_of_happiness_with_zero_distance(self):
        # Arrange
        citizen = Citizen("23", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = 20
        distance = 0

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0

    def test_calculation_of_happiness_with_negative_happiness(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = 20
        distance = 15

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 798.5

    def test_calculation_of_happiness_with_unemployed_citizen(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 0
        tax = 20
        distance = 10

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0

    def test_calculation_of_happiness_with_negative_tax(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 1000, 80, "Home")
        salary = 1000
        tax = -20
        distance = 10

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 1199.0

    def test_calculation_of_happiness_with_zero_distance_and_salary(self):
        # Arrange
        citizen = Citizen("1", "WorkZone", 0, 80, "Home")
        salary = 0
        tax = 20
        distance = 0

        # Act
        happiness = citizen.calcHappy(salary, tax, distance)

        # Assert
        assert happiness == 0
