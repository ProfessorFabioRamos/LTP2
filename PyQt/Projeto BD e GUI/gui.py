import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,
  QVBoxLayout, QListWidget
import db
class InventarioApp(QWidget):
  def __init__(self):
  super().__init__()
  self.setWindowTitle("Inventário")
  self.nome_input = QLineEdit()
  self.qtd_input = QLineEdit()
  self.add_btn = QPushButton("Adicionar Item")
  self.lista = QListWidget()
  layout = QVBoxLayout()
  layout.addWidget(QLabel("Nome do item:"))
  layout.addWidget(self.nome_input)
  layout.addWidget(QLabel("Quantidade:"))
  layout.addWidget(self.qtd_input)
  layout.addWidget(self.add_btn)
  layout.addWidget(QLabel("Itens no inventário:"))
  layout.addWidget(self.lista)
  self.setLayout(layout)
  self.add_btn.clicked.connect(self.adicionar_item)
  self.atualizar_lista()
  
  def adicionar_item(self):
    nome = self.nome_input.text()
    qtd = self.qtd_input.text()
    if nome and qtd.isdigit():
      db.inserir_item(nome, int(qtd))
      self.nome_input.clear()
      self.qtd_input.clear()
      self.atualizar_lista()
      
  def atualizar_lista(self):
    self.lista.clear()
    for item in db.listar_itens():
      self.lista.addItem(f"{item[1]} - Quantidade: {item[2]}")
      
if __name__ == "__main__":
app = QApplication(sys.argv)
janela = InventarioApp()
janela.show()
sys.exit(app.exec_())
