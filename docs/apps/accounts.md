# Aplicativo de Contas (accounts)

O aplicativo `accounts` é responsável por toda a gestão de usuários, incluindo autenticação, registro e perfis.

## Funcionalidades

-   **Registro de Usuário:** Novos usuários podem criar uma conta fornecendo informações básicas.
-   **Autenticação:** Usuários podem fazer login e logout de forma segura.
-   **Gerenciamento de Perfil:** Após o login, os usuários podem visualizar e atualizar suas informações de perfil, como biografia, foto e dados pessoais.

## Modelos

### `Profile`

O modelo `Profile` estende o modelo de usuário padrão do Django (`User`) para incluir informações adicionais.

-   `user`: Relacionamento um-para-um com o modelo `User`.
-   `bio`: Uma breve biografia do usuário.
-   `location`: Localização do usuário (limitado a `Brasil` ou `Estados Unidos`).
-   `phone`: Número de telefone.
-   `birth_date`: Data de nascimento.
-   `picture`: Foto de perfil.

## Views

-   `RegisterView`: Controla a página de registro de novos usuários.
-   `UserLoginView`: Gerencia o processo de login.
-   `UserLogoutView`: Gerencia o processo de logout.
-   `ProfileDetailView`: Exibe os detalhes do perfil de um usuário.
-   `ProfileUpdateView`: Permite que um usuário autenticado edite seu próprio perfil.

## Endpoints (URLs)

| Rota                      | Nome da URL        | View Responsável      | Descrição                                      |
| ------------------------- | ------------------ | --------------------- | ---------------------------------------------- |
| `/accounts/login/`        | `login`            | `UserLoginView`       | Página de login do usuário.                    |
| `/accounts/logout/`       | `logout`           | `UserLogoutView`      | Rota para deslogar o usuário.                  |
| `/accounts/register/`     | `register`         | `RegisterView`        | Página de registro de um novo usuário.         |
| `/accounts/profile/<int:pk>/` | `profile_detail`   | `ProfileDetailView`   | Exibe o perfil do usuário com o `pk` informado. |
| `/accounts/profile/<int:pk>/update/` | `profile_update`   | `ProfileUpdateView`   | Página para atualizar o perfil do usuário.     |
