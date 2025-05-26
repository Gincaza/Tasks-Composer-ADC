# Tasks Composer

Tasks Composer é uma aplicação web desenvolvida para ajudar os usuários a gerenciar suas tarefas de forma eficiente e organizada. Este projeto foi criado como parte da disciplina de Ambiente e Desenvolvimento Colaborativo da Universidade do Algarve.

## Funcionalidades

- **Criação e edição de tarefas**: Adicione tarefas com descrição e data de vencimento.
- **Marcação de tarefas como concluídas**: Atualize o status das tarefas facilmente.
- **Resumo visual**: Veja um resumo das tarefas pendentes e concluídas no dashboard.
- **Gerenciamento de informações pessoais**: Atualize seu nome.
- **Modo claro e escuro**: Alterne entre temas para uma melhor experiência visual.

## Tecnologias Utilizadas

- **Backend**: Django 5.2.1
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Banco de Dados**: SQLite

## Estrutura do Projeto

- `core/`: Contém a lógica principal da aplicação, incluindo modelos, views e templates.
- `config/`: Configurações do projeto Django.
- `static/`: Arquivos estáticos como CSS, JavaScript e imagens.
- `templates/`: Templates HTML para renderização das páginas.

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

## Documentação

Este projeto inclui uma documentação gerada com o Docusaurus, localizada na pasta `docs/`. Para iniciar o servidor de documentação localmente, execute os seguintes comandos:

1. Navegue até a pasta `docs/`:
   ```bash
   cd docs
   ```

2. Instale as dependências do Docusaurus:
   ```bash
   npm install
   ```

3. Inicie o servidor de desenvolvimento do Docusaurus:
   ```bash
   npm start
   ```

4. Acesse a documentação no navegador em `http://localhost:3000/`.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
