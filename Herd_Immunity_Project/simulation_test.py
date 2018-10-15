# Pytest to test _simulation_should_continue() function
import pytest
from person import Person
from simulation import Simulation
import simulation
import sys
from virus import Virus

def test_simulation_simulation_should_continue():
    # Get virus
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
    # Run Simulation
    simulation = Simulation(10, 0.10, "Ebola", 0.70,
    0.25, 2)
    simulation.run()
    # Create Population
    # testing_population = []
    # num_of_people = 6
    # for i in range(0, num_of_people):
    #     person = Person(i, False, False)
    #     self.population.append(person)
    # while people still alive or people still infected
    # while len(testing_population) != num_of_people:
    #     person = Person(False, False)
    #     testing_population.append(person)
    # call function
    # assert False
    # Point out error I get when running test: NameError for
    # _simulation_should_continue
    # _simulation_should_continue()

test_simulation_simulation_should_continue()

"""
Pseudocode:
What do we want to test? We want to test to see if the time counter is greater
than zero so we create a population that passes the edge cases and causes
_simulation_should_continue to return True. So, that means when the person is
alive and not vaccinated the simulation will continue so we want to create a
population like that.
# set an should_continue = True
"""
# def test_simulation_run():

# test for interaction function
# once population is created check to see

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
