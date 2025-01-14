from edge import Edge
from transition import Transition

class State:
    def __init__(self, state_name: str, value_is_final: bool = False): 
        self.state_name = state_name
        self.is_final = value_is_final
        self.transitions = []
 
    @property
    def state_name(self): return self._state_name
    
    @state_name.setter
    def state_name(self, state_name):
        self._state_name = state_name
        
    @property
    def is_final(self): return self._is_final
	
    @is_final.setter
    def is_final(self, value_is_final): self._is_final = value_is_final

    def add_transition(self, q_state, read_symbol, write_symbol, move_direction):
        return self.add_transitions(q_state, Edge.instance(read_symbol, write_symbol, move_direction))
    
    def add_transitions(self, q_state, *edges):
        for edge in edges:
            transition = Transition(q_state, edge)
            if transition not in self.transitions: 
                self.transitions.append(transition)
        return self
    
    def transition(self, current_symbol: str):
        for transition in self.transitions:
            edge = transition.edge
            if edge.read_symbol != None and edge.read_symbol == current_symbol:
                return transition
        return None
    
    def equals(self, q_state):
        if isinstance(q_state, State):
            return q_state.state_name == self.state_name
        return False
    
    def hashCode(self): 
        return hash(self.state_name)

