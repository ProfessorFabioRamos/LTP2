import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout
)

class SomaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Soma")
        # Criação dos widgets
        self.label1 = QLabel("Número 1:")
        self.input1 = QLineEdit()
        self.label2 = QLabel("Número 2:")
        self.input2 = QLineEdit()

        self.botao = QPushButton("Somar")
        self.resultado = QLabel("Resultado: ")
        # Conectar botão ao método de soma
        self.botao.clicked.connect(self.calcular_soma)

        # Layouts
        layout = QVBoxLayout()

        linha1 = QHBoxLayout()
        linha1.addWidget(self.label1)
        linha1.addWidget(self.input1)

        linha2 = QHBoxLayout()
        linha2.addWidget(self.label2)
        linha2.addWidget(self.input2)

        linha3 = QHBoxLayout()
        linha3.addWidget(self.botao)
        linha3.addWidget(self.resultado)

        layout.addLayout(linha1)
        layout.addLayout(linha2)
        layout.addLayout(linha3)

        self.setLayout(layout)
    
    def calcular_soma(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            soma = num1 + num2
            self.resultado.setText(f"Resultado: {soma}")
        except ValueError:
            self.resultado.setText("Insira números válidos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = SomaApp()
    janela.show()
    sys.exit(app.exec_())
