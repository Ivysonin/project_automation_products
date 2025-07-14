# 🤖 Automação de Cadastro de Produtos e Clientes

Projeto feito para automatizar o processo repetitivo de cadastro de **produtos** e **clientes** em um sistema web. Ideal para eliminar tarefas manuais e economizar tempo com processos que normalmente levariam horas.

## 📖 Resumo

Sabe aquela tarefa chata de ficar o dia todo cadastrando produto por produto, cliente por cliente?
Este projeto resolve isso com um script em Python que acessa um site, faz login e preenche automaticamente os formulários de cadastro a partir de uma planilha `.csv` com os dados.

Foi utilizado um site base de um curso online, já com banco de dados e layout prontos, focando exclusivamente na prática de **automação com PyAutoGUI** e **manipulação de dados com pandas**.

## 🚀 Funcionalidades

* Abertura automática do navegador e acesso à página de login
* Login com e-mail e senha
* Leitura de dados a partir de uma planilha `produtos.csv`
* Preenchimento automático dos campos de cadastro:

  * Código
  * Marca
  * Tipo
  * Categoria
  * Preço unitário
  * Custo
  * Observações
* Submissão automática do formulário para cada item da lista

## 🛠 Tecnologias Utilizadas

* Python
* pandas
* pyautogui
* time

## 📷 Programa Funcionando
Veja uma demonstração do script em ação:
https://github.com/user-attachments/assets/a01941f7-96ce-4014-854e-1c9402978848

## 📖 Aprendizados

Durante o desenvolvimento, pratiquei conceitos importantes de:

* Automação de processos com **PyAutoGUI**
* Manipulação de planilhas com **pandas**
* Simulação de interações humanas (cliques, digitação, scroll, etc.)
* Controle de fluxo e espera entre ações
* Aplicação prática de Python em cenários reais do dia a dia

Esse projeto mostrou como pequenas soluções automatizadas podem economizar um tempo enorme em tarefas repetitivas e manuais.
