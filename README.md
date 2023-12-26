# Fast Todo

![imagem-do-projeto](/images/imagem-do-projeto)

Gerenciador de tarefas com boas práticas do FastAPI

> **Nota:** Esse projeto foi feito com base no
> [Curso Básico de FastAPI do Zero](https://fastapidozero.dunossauro.com)


### Iniciar Projeto
```sh
docker-compose up
```

### Boas práticas abordadas
- Criação da documentação
- Desenvolvimento baseado em testes (TDD)
- Banco de dados evolutivo (Migrations)
- Injeção de dependências
- ORM com SQLAlchemy
- Conteinerização do Projeto
- Deploy no Fly.io
- Integração Continua (CI/CD)

### Contribuir com o desenvolvimento

#### Dependências
- [Python3.11.6](https://www.python.org/downloads)
  - Pode ser usado com o [pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/docs/#installation)
  - Gerencia o projeto e suas dependências
- [Docker](https://www.docker.com)
  - Gerencia o ambiente da aplicação


### Para inciar o projeto
```sh
# Instale as dependências do projeto
poetry install
```

#### Automações de tarefas
```sh
# Inicia a verificação de estilo do código
task lint

# Inicia as correções do estilo do código
task format

# Inicia os testes
task test

# Gera um arquivo de cobertura de testes em html
task post_test

# Cria uma nova migração
task db_migration -m '<mensagem>'

# Cria o banco de dados
task db_init

# Atualiza a próxima migração
task db_up +1

# Retorna a migração anterior
task db_down -1

# Inicia o projeto
task run
```

#### Git Flow

Utilizando alguns padrões do
[conventional commits em português](https://www.conventionalcommits.org/pt-br/v1.0.0)

- Commits
  - Escopo: `<ação>: <mensagem>`
  - Exemplo: `feat: criação de crud em /users`
- Branches
  - Escopo: `<ação>-<usuário>-<mensagem>`
  - Exemplo: `feat-brunodavi-crud-da-rota-users`
- Pull Requests
  - Escopo: `[ <AÇÃO> ] <Titulo>`
  - Exemplo:`[ FEAT ] Criação de CRUD na rota de usuários`
- Issues
  - Regras: 
    - 1. Veja se o problema já foi resolvido
    - 2. Descreva o que aconteceu e o que você já tentou fazer
  - Escopo: `<Titulo>`
  - Exemplo: `Ouve um problema na criação de usuários`
