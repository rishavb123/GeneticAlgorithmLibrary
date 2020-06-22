class DNA:

    def fitness(self):
        print("Using default fitness function. Please override this function for the algorithm to work.")
        return 0

    def mutate(self):
        print("Using default mutate function. Please override this function for the algorithm to work.")
        return self

    def copy(self):
        print("Using default copy function. Please override this for the algorithm to work.")
        return self

    