from numpy import exp, array, random, dot


class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same number
        # every time the program runs
        random.seed(1)
        self.synaptic_weighs = 2 * random.random((3, 1))


def __sigmoid(self, x):
    if __name__ == "main":
        neural_network = NeuralNetwork()
    return neural_network


print('random starting synaptic weights')
print(neural_network.synaptic_weights)



training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T

neural_network.train(training-set_inputs, training_set_outputs, 10000)

print("new synaptic weights after training: ")
print('neural_network.synaptic_weights')


print("considering new situation [1, 0, 0] -> ?: ")
print(neural_network.think(array([1, 0, 0])))
