from State import State

class AFD: #AFD = (Q, Σ, δ, q0, F)
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
    def run(self):
        if self.initial_q_state is None or self.word is None: 
            return False

        while True:
            current_symbol = self.band[self.current]
            transition = self.initial_q_state.transition(current_symbol)
            
            print(f'Estado: {self.initial_q_state.state_name}, Cabeçote: {self.current}, Fita: {self.band}')

            if not transition:
                if self.initial_q_state.is_final:
                    return self.print_result()
                else:
                    print(f'{current_symbol} nao pertence ao alfabeto ou nao possui transicao!!')
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

    def print_result(self):
        if(self.initial_q_state.is_final):
            print(f'reconheceu: {self.word}')
        else:
            print(f'Não reconheceu: {self.word}')
        return self.initial_q_state.is_final

    #Ideia para Turing Machine abaixo:
    def set_band(self, band_size: int):
        #self.band = ['#'] + ['-'] * (2 * band_size)
        self.band = ['_'] * (2 * band_size)
                
        for i, character in enumerate(self.word):
            self.band[band_size + 1 + i] = character
            
        self.current = band_size + 1
        
        #print(f'{self.band}\nLEN: {len(self.band)}\nMAX: {2 * band_size}')
        #print(f'current -> {self.band[self.current]}')