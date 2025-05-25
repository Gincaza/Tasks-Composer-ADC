---
id: overview
title: Visão Geral do Projeto
sidebar_position: 1
---

# Tasks Composer

Tasks Composer é uma aplicação web desenvolvida para ajudar os usuários a gerenciar suas tarefas de forma eficiente e organizada. Este projeto foi criado como parte da disciplina de Ambiente e Desenvolvimento Colaborativo da Universidade do Algarve.

## Funcionalidades

- **Criação e edição de tarefas**: Adicione tarefas com descrição e data de vencimento.
- **Marcação de tarefas como concluídas**: Atualize o status das tarefas facilmente.
- **Resumo visual**: Veja um resumo das tarefas pendentes e concluídas no dashboard.
- **Gerenciamento de informações pessoais**: Atualize seu nome e avatar.
- **Modo claro e escuro**: Alterne entre temas para uma melhor experiência visual.

## Tecnologias Utilizadas

- **Backend**: Django 5.2.1
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Banco de Dados**: SQLite

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Gincaza/Tasks-Composer-ADC.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Tasks-Composer-ADC
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse o projeto no navegador em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

O projeto Tasks Composer está organizado da seguinte forma:

### Diretórios Principais

- **`core/`**: Contém a lógica principal da aplicação, incluindo:
  - **`models.py`**: [Define os modelos de dados, como `Task` e `CustomUser`](./models.md).
  - **`views.py`**: Contém as funções de visualização para lidar com as requisições HTTP.
  - **`templates/`**: Armazena os templates HTML para renderização das páginas.
  - **`static/`**: Contém arquivos estáticos como CSS, JavaScript e imagens.

- **`config/`**: Configurações do projeto Django, incluindo:
  - **`settings.py`**: Configurações globais do projeto.
  - **`urls.py`**: Define as rotas do projeto.
  - **`wsgi.py`** e **`asgi.py`**: Arquivos para configuração de servidores WSGI e ASGI.

- **`docs/`**: Documentação do projeto gerada com Docusaurus, incluindo:
  - **`docusaurus.config.js`**: Configurações do Docusaurus.
  - **`docs/`**: Contém os arquivos de documentação em Markdown.
  - **`src/`**: Arquivos de personalização e componentes React para o site de documentação.

### Arquivos Importantes

- **`manage.py`**: Script de gerenciamento do Django.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Informações gerais sobre o projeto.
- **`LICENSE`**: Licença do projeto.

Essa estrutura foi projetada para manter o código organizado e facilitar a colaboração entre desenvolvedores.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.