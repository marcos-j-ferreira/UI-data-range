import tkinter as tk
from tkinter import ttk

class RangeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Data Range")
        self.root.geometry("900x600")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.frame_main = ttk.Frame(root)
        self.frame_main.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        self.frame_main.columnconfigure(0, weight=1)
        self.frame_main.columnconfigure(1, weight=2)
        self.frame_main.rowconfigure(0, weight=2)
        self.frame_main.rowconfigure(1, weight=1)
        self.frame_main.rowconfigure(2, weight=3)

        self.frame_config = ttk.LabelFrame(self.frame_main, text="Configuração")
        self.frame_config.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        for i in range(4):  # Permitir expansão das linhas de entrada
            self.frame_config.rowconfigure(i, weight=1)
        self.frame_config.columnconfigure(1, weight=1)

        ttk.Label(self.frame_config, text="IP:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_ip = ttk.Entry(self.frame_config)
        self.entry_ip.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_config, text="HOST:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_host = ttk.Entry(self.frame_config)
        self.entry_host.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_config, text="TEMPO:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_tempo = ttk.Entry(self.frame_config)
        self.entry_tempo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_config, text="VEZES:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_vezes = ttk.Entry(self.frame_config)
        self.entry_vezes.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.btn_save_config = ttk.Button(self.frame_config, text="Salvar configuração")
        self.btn_save_config.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        self.frame_graph = ttk.LabelFrame(self.frame_main, text="Gráfico")
        self.frame_graph.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.frame_graph.columnconfigure(0, weight=1)
        self.frame_graph.rowconfigure(0, weight=1)

        self.canvas_graph = tk.Canvas(self.frame_graph, bg="white")
        self.canvas_graph.pack(fill="both", expand=True, padx=5, pady=5)

        self.frame_controls = ttk.LabelFrame(self.frame_main, text="Controles")
        self.frame_controls.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        self.btn_run_test = ttk.Button(self.frame_controls, text="Executar Teste")
        self.btn_run_test.pack(side="left", padx=5, pady=5)

        self.frame_results = ttk.LabelFrame(self.frame_main, text="Log")
        self.frame_results.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.frame_results.columnconfigure(0, weight=1)
        self.frame_results.rowconfigure(0, weight=1)

        self.text_results = tk.Text(self.frame_results)
        self.text_results.pack(fill="both", expand=True, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = RangeApp(root)
    root.mainloop()