class Edge:
    def __init__(self, new_read_symbol: str, new_write_symbol: str, new_move_direction: str):
        self.read_symbol = new_read_symbol
        self.write_symbol = new_write_symbol
        self.move_direction = new_move_direction
        
    @property
    def read_symbol(self):
        return self._read_symbol
    
    @read_symbol.setter
    def read_symbol(self, new_read_symbol):
        self._read_symbol = new_read_symbol

    @property
    def write_symbol(self): 
        return self._write_symbol
    
    @write_symbol.setter
    def write_symbol(self, new_write_symbol):
        self._write_symbol = new_write_symbol

    @property
    def move_direction(self):
        return self._move_direction
    
    @move_direction.setter
    def move_direction(self, new_move_direction):
        self._move_direction = new_move_direction
        
    @staticmethod
    def instance(new_read_symbol: str, new_write_symbol: str, new_move_direction: str):
        return Edge(new_read_symbol, new_write_symbol, new_move_direction)

    def equals(self, other):
        if isinstance(other, Edge):
            return self.read_symbol == other.read_symbol
        return False

    def __repr__(self):
        return f'[{self.read_symbol} -> {self.write_symbol}, {self.move_direction}]'