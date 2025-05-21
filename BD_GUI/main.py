import interface
import banco

if __name__ == "__main__":
    try:
        interface.iniciar_interface()
    finally:
        banco.fechar_conexao()
