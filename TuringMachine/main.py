# .\.venv\Scripts\python.exe -m pip install readchar
#import threading
#import readchar
from collections import defaultdict
from state import State
from turing_machine import TuringMachine 
     
def read_input(arquivo):
    
    with open(arquivo, 'r') as file:
        lines = file.readlines()
    
    states = {}
    transitions = defaultdict(list)
    band = ''
    initial_state = None
    accept_state = None
    band_size = 10

    for line in lines:
        line = line.strip()
        
        if line.startswith('#') or not line:
            continue  
        
        if line.startswith('band'):
            band = line.split()[1]
        elif line.startswith('init'):
            initial_state = line.split()[1]
        elif line.startswith('accept'):
            accept_state = line.split()[1]
        else:
            parts = line.split(',')
            origin_state = parts[0].strip()
            symbol_read = parts[1].strip()
            destination_state = parts[2].strip()
            symbol_described = parts[3].strip()
            direction = parts[4].strip()

            transitions[origin_state].append((symbol_read, destination_state, symbol_described, direction))

    for state_name in set(transitions.keys()).union({accept_state}):
        states[state_name] = State(state_name)
                
    if accept_state:
        states[accept_state].is_final = True
        
    for origin_state, lista_transitions in transitions.items():
        for symbol_read, destination_state, symbol_described, direction in lista_transitions:
            states[origin_state].add_transition(
                states[destination_state],
                symbol_read,
                symbol_described,
                direction
            )

    turing_machine = TuringMachine(states[initial_state], band, band_size)
    turing_machine.run()

if __name__ == '__main__':
    read_input('../fonte.mt')