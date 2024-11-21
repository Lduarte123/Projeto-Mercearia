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
        self.attributes("-fullscreen", True)
        self.resizable(False, False)

        # Botão "Sair" na parte inferior
        self.close_button = ctk.CTkButton(self, text="Sair", command=self.exit_fullscreen)
        self.close_button.pack(side="bottom", pady=20)

        # Frame para os widgets de login (aumentado)
        self.login_frame = ctk.CTkFrame(self, width=600, height=400, corner_radius=15)  # Aumentando o tamanho
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centralizando o frame

        # Widgets dentro do frame
        self.label_title = ctk.CTkLabel(self.login_frame, text="Login", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)

        self.entry_user = ctk.CTkEntry(self.login_frame, placeholder_text="Usuário", width=300)
        self.entry_user.pack(pady=10)

        self.entry_password = ctk.CTkEntry(self.login_frame, placeholder_text="Senha", show="*", width=300)
        self.entry_password.pack(pady=10)

        self.button_login = ctk.CTkButton(self.login_frame, text="Entrar", command=self.validate_login)
        self.button_login.pack(pady=20)

        # Rodapé na parte inferior
        self.label_footer = ctk.CTkLabel(self, text="Desenvolvido com customtkinter", font=("Arial", 10))
        self.label_footer.pack(side="bottom", pady=10)

    def validate_login(self):
        # Lógica para validar login
        print("Validando login...")

    def exit_fullscreen(self):
        self.attributes("-fullscreen", False)
