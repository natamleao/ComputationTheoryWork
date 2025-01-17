import tkinter as tk
from tkinter import messagebox

class TuringMachineGUI(tk.Tk):
    def __init__(self, turing_machine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Máquina de Turing')
        self.geometry('800x600')
        
        self.turing_machine = turing_machine
        self.running = False

        self.tape_label = tk.Label(self, text='Fita:', font=('Arial', 14))
        self.tape_label.pack(pady=10)

        self.tape_display = tk.Label(self, text='', font=('Courier', 12))
        self.tape_display.pack(pady=5)

        self.state_label = tk.Label(self, text='Estado Atual:', font=('Arial', 14))
        self.state_label.pack(pady=10)

        self.state_display = tk.Label(self, text='', font=('Courier', 12))
        self.state_display.pack(pady=5)

        self.head_label = tk.Label(self, text='Posição do Cabeçote:', font=('Arial', 14))
        self.head_label.pack(pady=10)

        self.head_display = tk.Label(self, text='', font=('Courier', 12))
        self.head_display.pack(pady=5)

        self.start_button = tk.Button(self, text='Iniciar', command=self.start, font=('Arial', 12))
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(self, text='Pausar', command=self.pause, font=('Arial', 12), state=tk.DISABLED)
        self.pause_button.pack(pady=10)

        self.interval = None

    def start(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self._execute_steps()

    def pause(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            if self.interval:
                self.after_cancel(self.interval)
                
    def _execute_steps(self):
        if self.running:
            current_state = self.turing_machine.initial_q_state.state_name
            current_tape = ''.join(self.turing_machine.tape)
            cabeca_posicao = self.turing_machine.current
            self.state_display.config(text=f'Estado Atual: {current_state}')
            self.tape_display.config(text=current_tape)
            self.head_display.config(text=f'Posição do Cabeçote: {cabeca_posicao}')

            if not self.turing_machine.run_step(): 
                self.running = False
                if self.turing_machine.print_result():
                    result = 'Palavra aceita!'
                else:
                    result = 'Palavra não aceita!'
                    
                messagebox.showinfo('Resultado', result) 
                self.start_button.config(state=tk.NORMAL)
                self.pause_button.config(state=tk.DISABLED)
            else:
                self.interval = self.after(500, self._execute_steps)