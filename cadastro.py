import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QDateEdit
)

class FormularioInscricao(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inscrição na Newsletter")
        self.setFixedSize(400, 300)

        # Título
        self.label_titulo = QLabel("Inscreva-se na Saga EPIC")

        # Labels e campos
        self.label_nome = QLabel("Nome:")
        self.label_email = QLabel("E-mail:")
        self.label_cpf = QLabel("CPF:")
        self.label_data_nascimento = QLabel("Data de Nascimento:")

        self.lineEdit_nome = QLineEdit()
        self.lineEdit_email = QLineEdit()
        self.lineEdit_cpf = QLineEdit()
        self.dateEdit_data_nascimento = QDateEdit()

        self.button_inscrever = QPushButton("Inscrever-se")

        # Layout em grade
        layout = QGridLayout()
        layout.addWidget(self.label_titulo, 0, 0, 1, 2)

        layout.addWidget(self.label_nome, 1, 0)
        layout.addWidget(self.lineEdit_nome, 1, 1)

        layout.addWidget(self.label_email, 2, 0)
        layout.addWidget(self.lineEdit_email, 2, 1)

        layout.addWidget(self.label_cpf, 3, 0)
        layout.addWidget(self.lineEdit_cpf, 3, 1)

        layout.addWidget(self.label_data_nascimento, 4, 0)
        layout.addWidget(self.dateEdit_data_nascimento, 4, 1)

        layout.addWidget(self.button_inscrever, 5, 0, 1, 2)

        self.setLayout(layout)

# Inicialização da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = FormularioInscricao()
    form.show()
    sys.exit(app.exec())