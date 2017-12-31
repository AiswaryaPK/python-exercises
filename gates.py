import sys

class Gate(object):
    """ class representing a gate. It can be any gate. """

    def __init__(self, *args):
        """ initialise the class """
        self.input = args
        self.output = None

    def logic(self):
        """ the intelligence to be performed """
        raise NotImplementedError

    def output(self):
        """ the output of the gate """
        self.logic()
        return self.output


class AndGate(Gate):
    """ class representing AND gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]


class OrGate(Gate):
    """ class representing OR gate """

    def logic(self):
        self.output = self.input[0] or self.input[1]


class NotGate(Gate):
    """ class representing NOT gate """

    def logic(self):
        self.output = not self.input[0]
        
class NorGate(OrGate,NotGate):
    """ class representing NOT gate """

    def logic(self):
       OrResult = OrGate(self.input[0],self.input[1])
       OrResult.logic()
       NotG =NotGate(OrResult.output)
       NotG.logic()
       print ("NorGate = " + str(NotG.output))
        
class NandGate(AndGate,NotGate):
    """ class representing NOT gate """

    def logic(self):
       AndResult = AndGate(self.input[0],self.input[1])
       AndResult.logic()
       NG =NotGate(c.output)
       NG.logic()
       print ("NandGate = "+ str(NG.output))
       
NandG=NandGate(int(sys.argv[1]),int(sys.argv[1]))
NandG.logic()
NorG=NorGate(int(sys.argv[1]),int(sys.argv[1]))
NorG.logic()