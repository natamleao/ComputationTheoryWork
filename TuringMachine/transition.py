class Transition:
    def __init__(self, q_state, edge):
        self.q_state = q_state
        self.edge = edge
      
    @property
    def edge(self): return self._edge
    
    @edge.setter
    def edge(self, edge):
        self._edge = edge
    
    @property
    def q_state(self): return self._q_state
    
    @q_state.setter
    def q_state(self, q_state):
        self._q_state = q_state

    def equals(self, _inst_transition):
        if isinstance(_inst_transition, Transition):
            return _inst_transition.edge.equals(self.edge) and _inst_transition.q_state.equals(self.q_state)
        return False

    def hashCode(self):
        hc = self.q_state.hashCode() if self.q_state != None else 0
        hc = 47 * hc + (self.edge.hashCode() if self.edge != None else 0)
        return hc

    def __repr__(self):
        return f'{self.edge} --> {self.q_state.state_name}' 