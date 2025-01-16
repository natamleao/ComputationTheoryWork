from src.turing_machine import TuringMachine
from src.state import State

def test_increment_binary_deve_passar():
    """
    Descrição: adiciona 1 a um número binário.
    
    band 1011 -> 1100
    band 110 -> 111
    band 1111 -> 10000
    band 10001 -> 10010
    band 0 -> 1
    band 1110 -> 1111
    band 101010 -> 101011

    init right
    accept done

    right, 1, right, 1, >
    right, 0, right, 0, >
    right, _, carry, _, <

    carry, 1, carry, 0, <
    carry, 0, done, 1, <
    carry, _, done, 1, <
    """
    
    state_right = State('right')
    state_carry = State('carry')
    state_done = State('done',value_is_final=True)
    
    state_right.add_transition(state_right,'1','1','>')
    state_right.add_transition(state_right,'0','0','>')
    state_right.add_transition(state_carry,'_','_','<')
    
    state_carry.add_transition(state_carry,'1','0','<')
    state_carry.add_transition(state_done,'0','1','<')
    state_carry.add_transition(state_done,'_','1','<')

    words = ['1011','110','1111','10001','0','1110','101010']
    words_sucess = ['1100','111','10000','10010','1','1111','101011']
    for index, word in enumerate(words):
        turing_machine = TuringMachine(state_right, word,12)
        while turing_machine.run_step(): 
            pass
        result = list(filter(lambda x: x != '_',turing_machine.band))
        word_sucess = ''
        for symbol in result:
            word_sucess += symbol
            
        assert turing_machine.print_result() is True
        assert word_sucess == words_sucess[index]
        
