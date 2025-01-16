import tkinter as tk
from tkinter import messagebox

class TuringMachineGUI(tk.Tk):
    def __init__(self, turing_machine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Máquina de Turing')
        self.geometry('800x600')
        
        self.turing_machine = turing_machine
        self.running = False

        self.fita_label = tk.Label(self, text='Fita:', font=('Arial', 14))
        self.fita_label.pack(pady=10)

        self.fita_display = tk.Label(self, text='', font=('Courier', 12))
        self.fita_display.pack(pady=5)

        self.estado_label = tk.Label(self, text='Estado Atual:', font=('Arial', 14))
        self.estado_label.pack(pady=10)

        self.estado_display = tk.Label(self, text='', font=('Courier', 12))
        self.estado_display.pack(pady=5)

        self.cabeca_label = tk.Label(self, text='Posição do Cabeçote:', font=('Arial', 14))
        self.cabeca_label.pack(pady=10)

        self.cabeca_display = tk.Label(self, text='', font=('Courier', 12))
        self.cabeca_display.pack(pady=5)

        self.botao_iniciar = tk.Button(self, text='Iniciar', command=self.iniciar, font=('Arial', 12))
        self.botao_iniciar.pack(pady=10)

        self.botao_pausar = tk.Button(self, text='Pausar', command=self.pausar, font=('Arial', 12), state=tk.DISABLED)
        self.botao_pausar.pack(pady=10)

        self.intervalo = None

    def iniciar(self):
        if not self.running:
            self.running = True
            self.botao_iniciar.config(state=tk.DISABLED)
            self.botao_pausar.config(state=tk.NORMAL)
            self._executar_passos()

    def pausar(self):
        if self.running:
            self.running = False
            self.botao_iniciar.config(state=tk.NORMAL)
            self.botao_pausar.config(state=tk.DISABLED)
            if self.intervalo:
                self.after_cancel(self.intervalo)
                
    def _executar_passos(self):
        if self.running:
            estado_atual = self.turing_machine.initial_q_state.state_name
            fita_atual = ''.join(self.turing_machine.band)
            cabeca_posicao = self.turing_machine.current
            self.estado_display.config(text=f'Estado Atual: {estado_atual}')
            self.fita_display.config(text=fita_atual)
            self.cabeca_display.config(text=f'Posição do Cabeçote: {cabeca_posicao}')

            if not self.turing_machine.run_step(): 
                self.running = False
                if self.turing_machine.print_result():
                    resultado = 'Palavra reconhecida!'
                else:
                    resultado = 'Palavra não reconhecida.'
                    
                messagebox.showinfo('Resultado', resultado) 
                self.botao_iniciar.config(state=tk.NORMAL)
                self.botao_pausar.config(state=tk.DISABLED)
            else:
                self.intervalo = self.after(500, self._executar_passos)

    def atualizar_display(self):
        estado_atual = self.turing_machine.initial_q_state.state_name
        fita_atual = ''.join(self.turing_machine.band)
        cabeca_posicao = self.turing_machine.current
        self.estado_display.config(text=f'Estado Atual: {estado_atual}')
        self.fita_display.config(text=fita_atual)
        self.cabeca_display.config(text=f'Posição do Cabeçote: {cabeca_posicao}')