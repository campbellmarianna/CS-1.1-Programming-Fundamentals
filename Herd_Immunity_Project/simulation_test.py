# Pytest to test _simulation_should_continue() function
import pytest
from person import Person
import simulation
import sys

def test_simulation_should_continue():
    testing_population = []
    num_of_people = 6
    while len(testing_population) != num_of_people:
        person = Person(False, False)
        testing_population.append(person)
    # call function
    # assert False
    assert _simulation_should_continue(self) == False



# Test Code
# params = sys.argv[1:]
# pop_size = int(params[0])
# vacc_percentage = float(params[1])
# virus_name = str(params[2])
# mortality_rate = float(params[3])
# basic_repro_num = float(params[4])
# if len(params) == 6:
#     initial_infected = int(params[5])
# else:
#     initial_infected = 1
# simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
#                         basic_repro_num, initial_infected)
# test_simulation_should_continue()
