'''Служит для связывания бизнес-логики.'''
#!/usr/bin/env python

import abc
import random

# Result class that stores all results for futher calculations
class Blackboard(object):
    def __init__(self):
        self.ks = []
        self.common_state = {
            'results': 0,
            'ks_list': [],
            'progress': 0   # percentage, if 100 -> task is finished
        }

    def add_ks(self, ks):
        self.ks.append(ks)

# Our Controller class that runs all KnowledgeSource methods
# It can be used to configure KS before caluclations with entry data
class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def run_loop(self):
        while self.blackboard.common_state['progress'] < 100:
            for ks in self.blackboard.ks:
                if ks.is_ready:
                    ks.calculate_result()
        return self.blackboard.common_state['ks_list']

# Abstract class/interface to ensure that all KnowledgeSource classes have the same methods to be invoked
class AbstractKS(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, blackboard):
        self.blackboard = blackboard

    @abc.abstractmethod
    def is_ready(self):
        raise NotImplementedError('Must provide implementation in subclass.')

    @abc.abstractmethod
    def calculate_result(self):
        raise NotImplementedError('Must provide implementation in subclass.')

# KnowledgeSource type N, it could be f.e.
# - database source and business logic
# - some data science calucations that needs to be added to even more complext data calculations
# - speech recognition
# - and so on so forth...
class KS_Type0(AbstractKS):
    def is_ready(self):
        return random.randint(0,1)

    def calculate_result(self):
        self.blackboard.common_state['results'] += random.randint(1, 10)
        self.blackboard.common_state['ks_list'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(1, 2)

class KS_Type1(AbstractKS):
    def is_ready(self):
        return True # let's say this one is obligatory

    def calculate_result(self):
        self.blackboard.common_state['results'] += random.randint(5, 10)
        self.blackboard.common_state['ks_list'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(2, 4)

## Execute
if __name__ == '__main__':
    blackboard = Blackboard()

    blackboard.add_ks(KS_Type0(blackboard))
    blackboard.add_ks(KS_Type1(blackboard))

    c = Controller(blackboard)
    contributions = c.run_loop()

    from pprint import pprint
    pprint(blackboard.common_state)
