# Fast Todo

![imagem-do-projeto](/images/imagem-do-projeto)

Gerenciador de tarefas com boas práticas do FastAPI

> **Nota:** Esse projeto foi feito com base no
> [Curso Básico de FastAPI do Zero](https://fastapidozero.dunossauro.com)

## Iniciar Projeto
```sh
docker-compose up
```

## Contribuir com o desenvolvimento

### Dependências
- Python 11
- Poetry
- Docker


### Iniciar o projeto
```sh
# Instala as dependências do projeto
poetry install

# Inicia as tarefas de testes
task test

# Inicia as tarefas do linter
task lint

# Inicia o Projeto
task start
```

### Git Flow

Utilizando alguns padrões do
[conventional commits em português](https://www.conventionalcommits.org/pt-br/v1.0.0)

- Commits <ação>: <mensagem> `(ex: feat: criação de crud em /users)`
- Branches <ação>-<usuário>-<mensagem> `(ex: feat-brunodavi-crud-user)`
- Pull Requests [ <AÇÃO> ] <Titulo> `(ex: [ FEATURE ] Criação de CRUD na rota de usuários)`
- Issues <Titulo> `(ex: Ouve um problema na criação de usuários)`
  1. Veja se o problema já foi resolvido
  2. Descreva o que aconteceu e o que você já tentou fazer