import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget

class Inicio(QStackedWidget):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("Aplicación de Inicio")
        self.pantalla_inicio = PantallaInicio(self)
        #self.pantalla_login = PantallaLogin(self)
        #self.pantalla_registro = PantallaRegistro(self)

        #self.addWidget(self.pantalla_login)
        #self.addWidget(self.pantalla_registro)

    def mostrar_pantalla(self, indice):
        self.setCurrentIndex(indice)

class PantallaInicio(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("Aplicación de Inicio")

        
        self.boton_login = QPushButton("Iniciar sesión")
        self.boton_login.clicked.connect(self.pantalla_login)
        self.boton_registro = QPushButton("Registro")
        self.boton_registro.clicked.connect(self.pantalla_registro)

        self.layout.addWidget(self.boton_login)

        self.layout.addWidget(self.boton_registro)

    def pantalla_login(self):
        self.parent().mostrar_pantalla(1)

    def pantalla_registro(self):
        self.parent().mostrar_pantalla(2)

class PantallaLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("Login")

        self.etiqueta_usuario = QLabel("Usuario:")
        self.entrada_usuario = QLineEdit()
        self.etiqueta_password = QLabel("Contraseña:")
        self.entrada_password = QLineEdit()
        self.entrada_password.setEchoMode(QLineEdit.Password)
        self.boton_login = QPushButton("Iniciar sesión")
        self.boton_login.clicked.connect(self.iniciar_sesion)

        self.layout.addWidget(self.etiqueta_usuario)
        self.layout.addWidget(self.entrada_usuario)
        self.layout.addWidget(self.etiqueta_password)
        self.layout.addWidget(self.entrada_password)
        self.layout.addWidget(self.boton_login)

    def iniciar_sesion(self):
        # Implementa aquí la lógica para verificar las credenciales del usuario
        usuario = self.entrada_usuario.text()
        contrasena = self.entrada_password.text()
        if usuario == "usuario123" and contrasena == "contraseña123":
            self.parent().mostrar_pantalla(2)
        else:
            QMessageBox.critical(self, "Error", "Credenciales incorrectas", QMessageBox.Ok)

class PantallaRegistro(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("Registro")

        self.etiqueta_usuario = QLabel("Usuario:")
        self.entrada_usuario = QLineEdit()
        self.etiqueta_password = QLabel("Contraseña:")
        self.entrada_password = QLineEdit()
        self.entrada_password.setEchoMode(QLineEdit.Password)
        self.boton_registrar = QPushButton("Registrarse")
        self.boton_registrar.clicked.connect(self.registrar)

        self.layout.addWidget(self.etiqueta_usuario)
        self.layout.addWidget(self.entrada_usuario)
        self.layout.addWidget(self.etiqueta_password)
        self.layout.addWidget(self.entrada_password)
        self.layout.addWidget(self.boton_registrar)

    def registrar(self):
        # Implementa aquí la lógica para registrar al usuario
        usuario = self.entrada_usuario.text()
        contrasena = self.entrada_password.text()
        # Puedes almacenar los datos en una base de datos, archivo, o simplemente en variables en memoria
        QMessageBox.information(self, "Registro exitoso", "Usuario registrado correctamente", QMessageBox.Ok)
        self.parent().mostrar_pantalla(3)


def main():
    app = QApplication(sys.argv)
    ventana = Inicio()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
