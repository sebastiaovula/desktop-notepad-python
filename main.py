import tkinter as tk
from tkinter import filedialog, messagebox

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.root.geometry("800x600")

        # Área de texto
        self.texto = tk.Text(self.root, wrap="word", font=("Arial", 12))
        self.texto.pack(expand=True, fill="both", padx=5, pady=5)

        # Menu
        self.criar_menu()

    def criar_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Menu Arquivo
        menu_arquivo = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

        menu_arquivo.add_command(label="Abrir", command=self.abrir_arquivo)
        menu_arquivo.add_command(label="Salvar", command=self.salvar_arquivo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.root.quit)

    def abrir_arquivo(self):
        caminho = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            try:
                with open(caminho, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                self.texto.delete("1.0", tk.END)          # Limpa a área de texto
                self.texto.insert("1.0", conteudo)        # Coloca o conteúdo
                self.root.title(f"Bloco de Notas - {caminho}")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n{e}")

    def salvar_arquivo(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt"), ("Arquivo pdf", ".pdf"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            try:
                conteudo = self.texto.get("1.0", tk.END)
                with open(caminho, "w", encoding="utf-8") as arquivo:
                    arquivo.write(conteudo)
                self.root.title(f"Bloco de Notas - {caminho}")
                messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BlocoDeNotas(root)
    root.mainloop()