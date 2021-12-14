from utils import general_functions as gf
import random

LEARNING_RATE = .8


class NeuronCol:

    def __init__(self, number):
        self.bias = Neuron()
        self.neurons = [Neuron() for i in range(number)]

    def connect(self, col):
        for neuron in self.neurons:
            for neurons in col:
                neuron.connections.append(Axon(neuron, neurons))

    def insert_bias(self, col):
        self.bias.held = int(1)
        for neurons in col:
            self.bias.weights[neurons] = 1
            self.bias.connections.append(neurons)

    def output_error(self, movie):
        for neuron in self.neurons:
            neuron.error = (movie.my_rating - neuron.held) * neuron.held * (1 - neuron.held)


class Neuron:

    def __init__(self):
        self.held = None
        self.connections = []
        self.error = None

        # an ordered list of values
        self.push_forward = []
        self.pull_back = []

    def push(self):
        """
        Sends the the currently 'held' value forward across all its connections.
        """
        for con in self.connections:
            con.forward_propagate(self.held)

    def pull(self):
        """
        Sends the the currently 'held' value backwards across all its connections.
        """
        for con in self.connections:
            con.backward_propagate(self.error)

    def compute_held(self):
        """
        Held calculates the value 'held' by this particular neuron from the inputs collected
        from other Neurons firing into it. Not relevant for input neurons as their held values are the inputs.
        """
        self.held = gf.sigmoid(sum(self.push_forward))

    def compute_error(self):
        """
        Error represents how wrong this particular neuron was in contributing to the final output. Not relevent to
        terminal neurons as the error is the difference between the correct result and the calculated result.
        """
        total = sum(self.pull_back)
        total *= self.held * (1 - self.held)
        self.error = total

    def adjust_weights(self):
        """
        Adjusts the weights to reflect the calculated error.
        """
        for con in self.connections:
            con.adjust_weights()

    def clean(self):
        """
        Scrubs forward and back holding structs.
        """
        self.push_forward.clear()
        self.pull_back.clear()
        self.held = None
        self.error = None

    def compute_error_variance(self, value):
        """
        Represents the square of the error. The value is only used by terminal neurons as they
        cannot get their error through back propagation.
        """
        self.error = (value - self.held)**2


class Axon:

    def __init__(self, comes_from, goes_to, weight=None):
        """
        An axon is a squiggley tail that transfers signals from one neuron to another.
        The role of an axon is to know where the signal comes from, the weight to apply to that signal, and where
        to send it.
        """
        # constantly changing
        self.weight = weight
        if weight is None:
            self.weight = random.randint(-20, 20) / 100

        # immutable
        self.__comes_from = comes_from
        self.__goes_to = goes_to

    @property
    def comes_from(self):
        return self.__comes_from

    @property
    def goes_to(self):
        return self.__goes_to

    @comes_from.setter
    def comes_from(self, value):
        raise AttributeError("Cannot alter a connection during runtime.")

    @goes_to.setter
    def goes_to(self, value):
        raise AttributeError("Cannot alter a connection during runtime.")

    def forward_propagate(self, value):
        self.goes_to.push_forward.append(value * self.weight)

    def backward_propagate(self, value):
        self.comes_from.pull_back.append(value * self.weight)

    def adjust_weight(self):
        self.weight += self.comes_from.held * self.goes_to.error * LEARNING_RATE



