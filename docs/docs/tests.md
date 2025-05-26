---
id: tests
title: Testes
sidebar_position: 6
---

# Testes

O projeto Tasks Composer inclui testes automatizados para garantir a qualidade e o funcionamento correto das principais funcionalidades. Os testes estão localizados no arquivo `core/tests.py` e cobrem os seguintes aspectos:

- **Página Inicial**: Verifica se a página inicial é carregada corretamente.
- **Página de Login**: Testa se a página de login é exibida corretamente.
- **Página de Registro**: Garante que a página de registro está acessível.
- **Redirecionamento de Usuários Não Autenticados**: Verifica se usuários não autenticados são redirecionados para a página de login ao tentar acessar o dashboard.
- **Dashboard para Usuários Autenticados**: Testa se o dashboard é carregado corretamente para usuários autenticados.

## Como Executar os Testes

1. Certifique-se de que todas as dependências estão instaladas e o ambiente virtual está ativado.
2. Execute o seguinte comando na raiz do projeto:
   ```bash
   python manage.py test
   ```
3. O Django executará todos os testes e exibirá os resultados no terminal.

Manter os testes atualizados é essencial para garantir a estabilidade do projeto à medida que novas funcionalidades são adicionadas.