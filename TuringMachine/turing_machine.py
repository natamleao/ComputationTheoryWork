from state import State

class TuringMachine: #AFD = (Q, Σ, δ, q0, F)
    def __init__(self, new_initial_q_state: State, new_word: str, band_size: int):
        self.initial_q_state = new_initial_q_state
        self.word = new_word
 
        #Ideia para Turing Machine abaixo:        
        self.set_band(band_size)
    
    @property
    def initial_q_state(self): return self._initial_q_state
        
    @initial_q_state.setter
    def initial_q_state(self, new_initial_q_state):
        self._initial_q_state = new_initial_q_state
        
    @property
    def word(self): return self._word
    
    @word.setter
    def word(self, new_word):
        self._word = new_word
        
    @property
    def band(self): return self._band
    
    @band.setter
    def band(self, new_band: list = []):
        self._band = new_band
    
    #Ideia para Turing Machine abaixo:        
    def run_step(self):
        if self.initial_q_state is None or self.word is None: 
            return False

        current_symbol = self.band[self.current]
        transition = self.initial_q_state.transition(current_symbol)
        
        copy = self.band.copy()
        copy[self.current] = f'->{copy[self.current]}'
        print(f'Estado: {self.initial_q_state.state_name}, Cabeçote: {self.current}, Fita: {copy}')
        
        if not transition:
            return False
        
        self.band[self.current] = transition.edge.write_symbol
        self.initial_q_state = transition.q_state

        if transition.edge.move_direction == '>':
            self.current += 1
            if self.current >= len(self.band):
                self.band.append(None)
        elif transition.edge.move_direction == '<':
            self.current -= 1
            if self.current < 0:
                self.band.insert(0, None)
                self.current = 0
        
        return True

    def print_result(self):
        if self.initial_q_state.is_final:
            print(f'reconheceu: {self.word}')
            return True
        else:
            print(f'Não reconheceu: {self.word}')
            return False

    #Ideia para Turing Machine abaixo:
    def set_band(self, band_size: int):
        self.band = ['_'] * (2 * band_size)
                
        for i, character in enumerate(self.word):
            self.band[band_size + 1 + i] = character
            
        self.current = band_size + 1
        
        print(f'{self.band}\nLEN: {len(self.band)}\nMAX: {2 * band_size}')