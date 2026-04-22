import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # O usuario ouviu falar de um novo aplicativo de tarefas online. 
        # Ele decide verificar a página inicial do aplicativo.
        self.browser.get("http://localhost:8000")

        # Ele percebe que o título da página e o cabeçalho mencionam "To-Do".
        assert "To-Do" in self.browser.title

        # ele é convidado a inserir um item na lista
        self.fail("Finish the test!")  


        # ele digitta "Comprar um livro de python" na caixa de texto

        # quando ele aperta enter, a página é atualizada e agora a página lista "1: Comprar um livro de python" como um item em uma lista de tarefas

        # Continua aparecendo uma caixa de texto convidando-o a adicionar outro item. Ele digita "Comprar um livro de django"  

        # a página é atualizada novamente, mostrando ambos os itens em sua lista.

        # satisfeito, ele volta para a cama e adormece
        
if __name__ == "__main__":  
    unittest.main() 