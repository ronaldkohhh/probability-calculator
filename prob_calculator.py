import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    print(kwargs)
    for k, v in kwargs.items():
      ##print(k,v)
      for x in range(v):
        self.contents.append(k)
    print(self.contents)

  def draw(self, num):
    if num > len(self.contents):
      return self.contents
    removed = []

    result = random.sample(self.contents, num)
    for x in result:
      removed.append(x)
      self.contents.remove(x)
    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  print("#######################")
  count = 0  ##this is M
  ##change 5 to num_experiments
  for x in range(num_experiments):
    newHat = copy.deepcopy(hat)
    result = newHat.draw(num_balls_drawn)
    allMatch = True
    ##print(result)

    ##converts result from list to dict
    resultDict = {}
    for x in result:
      if x not in resultDict:
        resultDict[x] = 1
      else:
        resultDict[x] += 1
    ##print(resultDict)
    ##print("expected: ", expected_balls,"\nactual: ",resultDict)

    allMatch = True
    for key in expected_balls.keys():
      if result.count(key) < expected_balls[key]:
        allMatch = False
        break
    if allMatch:
      count += 1

  print("count: ", count)
  print("probabilty: ", count / num_experiments)
  probability = count / num_experiments
  return probability
