from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


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
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text) 

        # ele é convidado a inserir um item na lista
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # ele digitta "Comprar um livro de python" na caixa de texto
        inputbox.send_keys("Comprar um livro de python")

        # quando ele aperta enter, a página é atualizada e agora a página lista "1: Comprar um livro de python" como um item em uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == "1: Comprar um livro de python" for row in rows), "New to-do item did not appear in table"
        )


        # Continua aparecendo uma caixa de texto convidando-o a adicionar outro item. Ele digita "Comprar um livro de django"  

        self.fail("Finish the test")

        # a página é atualizada novamente, mostrando ambos os itens em sua lista.

        # satisfeito, ele volta para a cama e adormece
        
if __name__ == "__main__":  
    unittest.main() 