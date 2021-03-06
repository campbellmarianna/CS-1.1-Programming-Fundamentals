class Logger(object):
    '''
    Utility class responsible for logging all interactions of note during the
    simulation.


    _____Attributes______

    file_name: the name of the file that the logger will be writing to.

    _____Methods_____

    __init__(self, file_name):

    write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
        basic_repro_num):
        - Writes the first line of a logfile, which will contain metadata on the
            parameters for the simulation.

    log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
        - Expects person1 and person2 as person objects.
        - Expects did_infect, person2_vacc, and person2_sick as Booleans, if passed.
        - Between the values passed with did_infect, person2_vacc, and person2_sick, this method
            should be able to determine exactly what happened in the interaction and create a String
            saying so.
        - The format of the log should be "{person1.ID} infects {person2.ID}", or, for other edge
            cases, "{person1.ID} didn't infect {person2.ID} because {'vaccinated' or 'already sick'}"
        - Appends the interaction to logfile.

    log_infection_survival(self, person, did_die_from_infection):
        - Expects person as Person object.
        - Expects bool for did_die_from_infection, with True denoting they died from
            their infection and False denoting they survived and became immune.
        - The format of the log should be "{person.ID} died from infection" or
            "{person.ID} survived infection."
        - Appends the results of the infection to the logfile.

    log_time_step(self, time_step_number):
        - Expects time_step_number as an Int.
        - This method should write a log telling us when one time step ends, and
            the next time step begins.  The format of this log should be:
                "Time step {time_step_number} ended, beginning {time_step_number + 1}..."
        - STRETCH CHALLENGE DETAILS:
            - If you choose to extend this method, the format of the summary statistics logged
                are up to you.  At minimum, it should contain:
                    - The number of people that were infected during this specific time step.
                    - The number of people that died on this specific time step.
                    - The total number of people infected in the population, including the newly
                        infected
                    - The total number of dead, including those that died during this time step.
    '''

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

        # https://www.pythonforbeginners.com/cheatsheet/python-file-handling
        # Also got help from Nolen Kovacik for this one:
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method.  The simulation class should use this method
        # immediately upon creation, to log the specific parameters of the simulation
        # as the first line of the file.  This line of metadata should be tab-delimited
        # (each item separated by a '\t' character).
        # NOTE: Since this is the first method called, it will create the text file
        # that we will store all logs in.  Be sure to use 'w' mode when you open the file.
        # For all other methods, we'll want to use the 'a' mode to append our new log to the end,
        # since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

        # writes to text file
        with open(self.file_name, "w") as file:
            file.write(f"{population_size}\t {vax_percentage}\t {virus_name}\t {mortality_rate}\t {infection_rate}")
            file.write("/n========================================================/n")
            file.write(f"     Population Size: {population_size}\n")
            file.write(f"    Vaccination Rate: {vax_percentage}\n")
            file.write(f"          Virus Name: {virus_name}\n" )
            file.write(f"      Mortality Rate: {mortality_rate}\n")
            file.write(f"      Infection Rate: {infection_rate}\n")
            file.write(f" # initial infection: {initial_infected}\n")
            file.write(f"   # of interactions: {interactions}\n")
        file.close()

        #Print same data to console:
        print(f"     Population Size: {population_size}")
        print("    Vaccination Rate: {vax_percentage}")
        print("          Virus Name: {virus_name}" )
        print("      Mortality Rate: {mortality_rate}")
        print("      Infection Rate: {infection_rate}")
        print(" # initial infection: {initial_infected}")
        print("   # of interactions: {interactions}")


    def log_interaction(self, person1, person2):
        # TODO: Finish this method.  The Simulation object should use this method to
        # log every interaction a sick individual has during each time step.  This method
        # should accomplish this by using the information from person1 (the infected person),
        # person2 (the person randomly chosen for the interaction), and the optional
        # keyword arguments passed into the method.  See documentation for more info
        # on the format of the logs that this method should write.
        # NOTE:  You'll need to think
        # about how the booleans passed (or not passed) represent
        # all the possible edge cases!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        """
        Documentation:
        - Expects person1 and person2 as person objects.
        - Expects did_infect, person2_vacc, and person2_sick as Booleans, if passed.
        - Between the values passed with did_infect, person2_vacc, and person2_sick, this method
            should be able to determine exactly what happened in the interaction and create a String
            saying so.
        - The format of the log should be "{person1.ID} infects {person2.ID}", or, for other edge
            cases, "{person1.ID} didn't infect {person2.ID} because {'vaccinated' or 'already sick'}"
        - Appends the interaction to logfile.
        """
        """
        Pseudocode:
        # check if person1 is infected:
            # Create log: {person1.ID} infects {person2.ID}
        # check if person1 is not infected:
            # Create log: {person1.ID} didn't infect {person2.ID}
        # if person 2 does not have a virus and is not vaccinated
            # then {person1.ID} didn't infect {person2.ID} because {'vaccinated'}
        # check if the random person does not have a virus and is not vaccinated
            # if the random person meets these requirements then we generate a
            random number between 0 and 1
            # check if that number is less than or equal to the basic
            reproduction rate
            # if the random number is less than the reproduction rate then we
            add the id of that person to the newly infected array
            # if the random number is greater than the reproduction rate then we
            then do nothing
        """
        with open(self.file_name, "w") as file:
            # if person1 has the virus then person1 infects person2
            if person1.infection != None:
                file.write(f"/n {person1._id} infects {person2._id} because already sick. /n")
            # if person2 has the virus then person1 infects person2
            if person2.infection != None:
                file.write(f"/n {person2._id} infects {person1._id} because already sick. /n")
            if person1.is_vaccinated == True:
                file.write(f"/n {person1._id} didn't infect {person2._id} because vaccinated. /n")
            if person2.is_vaccinated == True:
                file.write(f"/n {person2._id} didn't infect {person1._id} because vaccinated. /n")
        file.close()

    def log_infection_survival(self, person, population):
        # TODO: Finish this method.  The Simulation object should use this method to log
        # the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False.  Otherwise,
        # did_die_from_infection should be True.  See the documentation for more details
        # on the format of the log.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        """
        Pseudocode:
        if person.is_alive == True:
            did_die_from_infection = false
        else:
            did_die_from_infection = True
        """
        did_die_from_infection = None
        with open(self.file_name, "a") as file:
            for person in population:
                if person.is_alive == True:
                    did_die_from_infection == False
                    file.write(f"/n Person ID: {person._id} survived infection and is now immune")
            else:
                did_die_from_infection = True
                file.write(f"/n Person ID: {person._id} died from infection./n")
            file.close()

    def log_time_step(self, time_step_number):
        # TODO: Finish this method.  This method should log when a time step ends, and a
        # new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        def log_time_step(self, time_step_number):
            next_step = int(time_step_number + 1)
            with open(self.file_name, "a") as file:
                file.write("/n ===========================================/n")
                file.write(f"/n Time step {time_step_number} has ended, starting time step {next_step}/n")
                file.write("/n ===========================================/n")
                file.close()
