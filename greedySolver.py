from scenario import Scenario

class GreedySolver:
  def __init__(self, input_data):
    self.scenario = Scenario(input_data)

  def solve(self):
    self.value = 0
    weight = 0
    self.taken = [0]*len(self.scenario.items)

    for item in self.scenario.items:
        if weight + item.weight <= self.scenario.capacity:
            self.taken[item.index] = 1
            self.value += item.value
            weight += item.weight

  def output_solution(self):
     # prepare the solution in the specified output format
    output_data = str(self.value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, self.taken))
    return output_data