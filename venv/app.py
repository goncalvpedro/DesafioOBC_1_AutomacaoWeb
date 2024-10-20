from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os
import interface

load_dotenv()

# Carregar credenciais e XPaths das variáveis de ambiente
email = os.getenv('EMAIL')
email_xpath = os.getenv('XPATH_EMAIL')
password = os.getenv('PASSWORD')
password_xpath = os.getenv('XPATH_PASSWORD')
submit_xpath = os.getenv('XPATH_SUBMIT')
login_path = os.getenv('LOGIN_PATH')
courses_path = os.getenv('COURSES_PATH')
button_xpath = "//button[@type='submit']"


# Função para conectar ao navegador Edge
def connect_to_edge():
    options = Options()
    options.add_argument("--disable-features=RendererCodeIntegrity")
    options.add_argument("--disable-gpu")
    options.add_argument('--ignore-certificate-errors')
    return webdriver.Edge(options=options)

# Função genérica para aguardar o carregamento de um elemento pelo seu XPATH
def wait_for_element_by_xpath(driver, xpath, timeout=20):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

# Função para fazer login na plataforma
def login(driver):
    driver.get(login_path)
    wait_for_element_by_xpath(driver, email_xpath).send_keys(email)
    wait_for_element_by_xpath(driver, password_xpath).send_keys(password)
    wait_for_element_by_xpath(driver, submit_xpath).click()
    driver.maximize_window()

# Função para navegar até a página de cursos
def navigate_to_courses(driver):
    wait_for_element_by_xpath(driver, "//a[text()='Cursos']").click()

# Função para buscar cursos disponíveis
def fetch_courses(driver):
    try:
        time.sleep(2)  # Permitir que a página carregue
        courses = driver.find_elements(By.CLASS_NAME, "line-clamp-2")
        return [course.text for course in courses if course.text]  # Filtrar títulos vazios
    except Exception as e:
        print(f'Erro ao carregar os cursos: {e}')
        return []

# Função para clicar em um curso pelo seu título
def click_course_by_title(driver, course_title):
    try:
        xpath = f"//span[@title='{course_title}']/ancestor::a"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()
    except Exception as e:
        print(f"Erro ao acessar o curso {course_title}: {e}")

# Função para clicar na primeira aula do curso selecionado
def click_first_class_in_course(driver):
    try:
        first_class_xpath = "(//a[contains(@class, 'flex w-full items-center space-x-2 p-4 cursor-pointer')])[1]"
        wait_for_element_by_xpath(driver, first_class_xpath).click()
    except Exception as e:
        print(f"Erro ao acessar a primeira aula: {e}")

# Função para verificar e clicar no botão de conclusão
def verify_and_click_conclusion_button(driver, button_xpath, courses_path, timeout=15, max_retries=3):
    attempt = 0
    while attempt <= max_retries:
        try:
            print(f'Tentativa {attempt + 1}/{max_retries} para clicar no botão de conclusão.')
            footer_button = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, "//footer//button"))
            )
            
            if footer_button.is_displayed() and footer_button.is_enabled():
                footer_button_text = footer_button.text
                if footer_button_text in ['Concluída', 'Concluir aula']:
                    footer_button.click()
                    print(f'Clicado no botão: {footer_button_text}')
                    time.sleep(1.5)

                    # Verificar se precisamos retornar à lista de cursos
                    conclusion_button = wait_for_element_by_xpath(driver, button_xpath)
                    if 'Voltar ao currículo' in conclusion_button.text:
                        print('Todas as aulas deste curso foram concluídas.')
                        driver.get(courses_path)
                        break
            else:
                print("Botão não disponível ainda, tentando novamente...")
                attempt += 1
                
            time.sleep(1.5)

        except Exception as e:
            print(f'Erro ao tentar clicar no botão: {e}')
            time.sleep(1)
            attempt += 1

    driver.get(courses_path)    

# Função principal para executar o script
def main():
    driver = connect_to_edge()
        
    try:
        login(driver)
        navigate_to_courses(driver)
        time.sleep(5)
        available_courses = fetch_courses(driver)
        selected_courses = interface.show_selected_courses(available_courses)

        for course in selected_courses:
            print(f'Concluindo tarefas do curso {course}')
            click_course_by_title(driver, course)
            time.sleep(1)
            click_first_class_in_course(driver)
            time.sleep(1.5)
            verify_and_click_conclusion_button(driver, button_xpath, courses_path)
        

    except Exception as e:
        print(f'Erro: {e}')
    finally:
        print('Automação encerrada.')
        driver.quit()

if __name__ == "__main__":
    main()
