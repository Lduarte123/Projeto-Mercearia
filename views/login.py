import customtkinter as ctk
from tkinter.messagebox import showinfo

# Configuração inicial
ctk.set_appearance_mode("Dark")  # Modo claro ou escuro
ctk.set_default_color_theme("blue")  # Tema de cores padrão (blue, green, dark-blue)


class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Login")
        self.geometry("400x300")
        self.resizable(False, False)

        # Widgets na janela de login
        self.label_title = ctk.CTkLabel(self, text="Bem-vindo!", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)

        self.entry_user = ctk.CTkEntry(self, placeholder_text="Usuário", width=300)
        self.entry_user.pack(pady=10)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=300)
        self.entry_password.pack(pady=10)

        self.button_login = ctk.CTkButton(self, text="Entrar", command=self.validate_login)
        self.button_login.pack(pady=20)

        self.label_footer = ctk.CTkLabel(self, text="Desenvolvido com customtkinter", font=("Arial", 10))
        self.label_footer.pack(side="bottom", pady=10)

    def validate_login(self):
        # Pegando os dados dos campos
        username = self.entry_user.get()
        password = self.entry_password.get()

        # Verificando credenciais (exemplo fixo)
        if username == "admin" and password == "1234":
            showinfo("Login", "Login realizado com sucesso!")
        else:
            showinfo("Erro", "Usuário ou senha incorretos.")


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
