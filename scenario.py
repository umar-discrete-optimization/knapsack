from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

class Scenario:
  def __init__(self, input_data):
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    self.capacity = int(firstLine[1])

    self.items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        self.items.append(Item(i-1, int(parts[0]), int(parts[1])))