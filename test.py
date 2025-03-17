import tkinter as tk
from tkinter import ttk

class WifiSignalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Sinal Wi-Fi")
        self.root.geometry("800x500")

        # Seção principal
        self.frame_main = ttk.Frame(root)
        self.frame_main.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Seção de Configuração
        self.frame_config = ttk.LabelFrame(self.frame_main, text="Configuração")
        self.frame_config.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        
        ttk.Label(self.frame_config, text="IP:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_ip = ttk.Entry(self.frame_config)
        self.entry_ip.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.frame_config, text="Host:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_host = ttk.Entry(self.frame_config)
        self.entry_host.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.frame_config, text="Tempo:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_time = ttk.Entry(self.frame_config)
        self.entry_time.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.frame_config, text="Rodadas:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_run = ttk.Entry(self.frame_config)
        self.entry_run.grid(row=3, column=1, padx=5, pady=5)
        
        self.btn_save_config = ttk.Button(self.frame_config, text="Salvar Configuração")
        self.btn_save_config.grid(row=4, column=0, columnspan=2, pady=10)

        # Espaço para o gráfico
        self.frame_graph = ttk.LabelFrame(self.frame_main, text="Gráfico")
        self.frame_graph.grid(row=0, column=1, sticky="ne", padx=5, pady=5)
        self.canvas_graph = tk.Canvas(self.frame_graph, bg="white", width=300, height=150)
        self.canvas_graph.pack(fill="both", expand=True, padx=5, pady=5)

        # Seção de Controles
        self.frame_controls = ttk.LabelFrame(self.frame_main, text="Controles")
        self.frame_controls.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        self.btn_run_test = ttk.Button(self.frame_controls, text="Executar Teste")
        self.btn_run_test.pack(side="left", padx=5, pady=5)

        self.btn_clear_logs = ttk.Button(self.frame_controls, text="Limpar Logs")
        self.btn_clear_logs.pack(side="left", padx=5, pady=5)
        
        self.btn_show_results = ttk.Button(self.frame_controls, text="Mostrar Resultados")
        self.btn_show_results.pack(side="left", padx=5, pady=5)

        # Seção de Log ao Vivo
        self.frame_results = ttk.LabelFrame(self.frame_main, text="Log ao Vivo do Teste")
        self.frame_results.grid(row=2, column=0, columnspan=2, sticky="snew", padx=5, pady=5)
        
        self.text_results = tk.Text(self.frame_results, height=10)
        self.text_results.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Botão Fechar
        self.btn_close = ttk.Button(root, text="Fechar", command=root.quit)
        self.btn_close.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = WifiSignalGUI(root)
    root.mainloop()
