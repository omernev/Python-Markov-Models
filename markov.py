import random

class Markov(object):

    def __init__(self, order):
        self.graph = {}
        self.text = None
        self.order = order
        self.group_size = self.order + 1
        return

    def train(self, filename):
        self.text = file(filename).read().split()
        self.text = self.text + self.text[ : self.order]

        for i in range(0, len(self.text) - self.group_size):
            
            key = tuple(self.text[i : i + self.order])
            value = self.text[i + self.order]

            if key in self.graph:
                self.graph[key].append(value)
            else:
                self.graph[key] = [value]
        return

    def generate(self,length):
        index = random.randint(0, len(self.text) - self.order)
        result = self.text[index : index + self.order]

        for i in range(length):
            state = tuple(result[len(result) - self.order : ])
            next_word = random.choice(self.graph[state])
            result.append(next_word)

        return " ".join(result[self.order : ])

    def avg_value(self):
        vals = [len(x) for x in self.graph.values()]
        return float(sum(vals)) / len(vals)
        

def do_it(filename, order, length):
    m = Markov(order)
    m.train(filename)
    print m.generate(length)
    return m
