## Recursos Utilizados

- **Navegador:** Microsoft Edge (escolhido pela melhor performance em relação ao Chrome).
- **Linguagem:** Python.
- **Bibliotecas:** 
  - Selenium
  - Tkinter
  - Time
  - OS
- **Ambiente:** venv
- **Repositório:** GitHub

---

## Vantagens

- Permite selecionar quantos cursos você quiser completar.
- Execução rápida e eficiente.

## Desvantagens

- Necessita executar o script, ao invés de um arquivo .exe.
- Se não quiser concluir todas as aulas, feche o navegador ao atingir a tarefa desejada.

---

## Passo a Passo para Utilização

1. Clone o repositório localmente:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Acesse o diretório do projeto e abra o terminal.
3. Navegue até o ambiente virtual `venv`:
   ```bash
   cd '.\venv'
   ```
4. Ative o ambiente virtual:
   ```bash
   .\Scripts\activate
   ```
5. Instale as dependências do projeto:
   ```bash
   python.exe -m pip install -r requirements.txt
   ```
6. Edite o arquivo `.env` com suas credenciais de acesso à plataforma OneBitCode:
   ```plaintext
   EMAIL=seu_email
   PASSWORD=sua_senha
   ```
   *Observação: suas informações estarão armazenadas apenas no arquivo `.env` em sua máquina, sem cache ou logs.*
   
7. Se necessário, instale o navegador Microsoft Edge [aqui](https://www.microsoft.com/pt-br/edge/download?form=MA13FJ).
8. Execute o arquivo `app.py` pelo terminal:
   ```bash
   python .\app.py
   ```
9. Aguarde a interface do Tkinter abrir com os cursos disponíveis. Se nenhum curso aparecer, repita o passo anterior.
10. Selecione os cursos que deseja completar e pressione OK. Confirme na janela de diálogo.
11. Aguarde a finalização do script.

---

## Observações

- Se você acompanhar o terminal durante a execução, não se preocupe com mensagens de atenção; elas não afetam a automação.
- Para aumentar o timeout devido a uma conexão lenta, edite o parâmetro `timeout` na função `verify_and_click_conclusion_button`.

---

## Dificuldades

A principal dificuldade foi contornar o overlay da página quando o tempo de resposta era maior que o tempo de execução. Isso foi minimizado usando `time.sleep()` e funções de espera do Selenium.

---

## Futuras Melhorias

- Implementar uma interface gráfica para login, evitando a necessidade de armazenar informações pessoais no arquivo `.env`.
- Trabalhar na criptografia de senhas para tornar a distribuição do aplicativo mais escalável.

---

