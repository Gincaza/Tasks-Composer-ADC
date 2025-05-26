---
id: authentication-authorization
title: Autenticação e Autorização
sidebar_position: 7
---

# Autenticação e Autorização

O projeto Tasks Composer implementa um sistema de autenticação e autorização para garantir que apenas usuários autenticados possam acessar determinadas funcionalidades. Abaixo estão os principais aspectos desse sistema:

## Autenticação

- **Registro de Usuário**:
  - Os usuários podem se registrar através da página de registro (`/register/`).
  - O formulário de registro inclui campos como nome de usuário, nome completo e senha.

- **Login**:
  - Usuários registrados podem fazer login na página de login (`/login/`).
  - Após o login, os usuários são redirecionados para o dashboard.

- **Logout**:
  - Os usuários podem fazer logout clicando no botão de logout disponível no menu lateral.

## Autorização

- **Acesso Restrito**:
  - Apenas usuários autenticados podem acessar páginas como o dashboard, gerenciamento de tarefas e configurações.
  - Usuários não autenticados que tentarem acessar essas páginas serão redirecionados para a página de login.

- **Redirecionamento**:
  - Após o login, os usuários são redirecionados para a página que tentaram acessar antes de serem autenticados.

## Implementação Técnica

- **Middleware**:
  - O Django utiliza o middleware de autenticação para verificar se o usuário está autenticado antes de acessar determinadas views.

- **Decoradores**:
  - O decorador `@login_required` é usado para proteger views que requerem autenticação.

- **URLs Relevantes**:
  - `/register/`: Página de registro.
  - `/login/`: Página de login.
  - `/logout/`: Endpoint para logout.
  - `/dashboard/`: Página inicial para usuários autenticados.

Manter o sistema de autenticação e autorização atualizado é essencial para garantir a segurança e a privacidade dos dados dos usuários.