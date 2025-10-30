# 📦 LT_Pedidos

Sistema de gerenciamento de pedidos com upload de planilhas Excel e geração de relatórios profissionais.

## 🎯 Objetivo do Projeto

O **LT_Pedidos** é uma aplicação fullstack que permite:
- Upload e processamento de planilhas Excel com dados de pedidos
- Validação e normalização automática de dados
- Armazenamento em banco de dados relacional
- Geração de relatórios em PDF e Excel
- Interface web moderna para visualização e gestão

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.11+**
- **Astral uv 0.8.17+** - Gerenciador de pacotes Python
- **FastAPI** - Framework web moderno e rápido
- **Pandas** - Processamento de dados Excel
- **SQLAlchemy** - ORM para banco de dados
- **Pytest** - Testes automatizados (ainda não implementado, mas na rota)
- **ReportLab** - Geração de PDFs
- **Commitizen** - Para padronização de commits e gerenciamento de versões

### Frontend
- **Next.js 14** - Framework React com TypeScript
- **TailwindCSS** - Estilização
- **shadcn/ui** - Componentes UI
- **React Hook Form** - Gerenciamento de formulários
- **Axios** - Requisições HTTP

### DevOps
- **Docker** - Containerização
- **GitHub Actions** - CI/CD
- **Vercel** - Deploy do frontend
- **Render/Railway** - Deploy do backend

## 📁 Estrutura do Projeto

A estrutura principal do projeto é dividida entre `back_lt_pedidos` (Backend) e `front_lt_pedidos` (Frontend).

## 📁 Estrutura do Projeto

```
lt-pedidos/
.
├── back_lt_pedidos/
│ ├── .cz.toml # Configuração do Commitizen
│ ├── CHANGELOG.md # Histórico de mudanças (gerado automaticamente)
│ ├── LICENSE
│ ├── README.md
│ ├── app/ # Código principal da aplicação FastAPI
│ │ ├── init.py
│ │ ├── main.py # Ponto de entrada da API
│ │ ├── models/ # Definições de modelos de dados e schemas (Pydantic, SQLAlchemy)
│ │ │ └── schemas.py
│ │ ├── routes/ # Endpoints da API (FastAPI Routers)
│ │ ├── services/ # Lógica de negócio, processamento de dados, interações com BD
│ │ └── utils/ # Funções utilitárias gerais
│ ├── examples/ # Scripts de exemplo e arquivos de dados para testes
│ │ ├── ORDEMDECOMPRAS.xlsx
│ │ ├── cotacao-compra.pdf
│ │ ├── cotacao-compra.xlsx
│ │ ├── main.py # Exemplo de script
│ │ ├── main2.py # Exemplo de script
│ │ ├── main3.py # Exemplo de script
│ │ └── ... (outros arquivos de exemplo/scripts)
│ ├── pyproject.toml # Dependências, metadados do projeto e configs de ferramentas (uv, Commitizen)
│ ├── tests/ # Testes unitários e de integração (ainda não implementado)
│ └── uv.lock # Lock file do Astral UV para dependências
└── front_lt_pedidos/ # Código do frontend (Next.js)
├── README.md
└── front_lt_pedidos
    ├── README.md
    ├── eslint.config.mjs
    ├── next-env.d.ts
    ├── next.config.ts
    ├── node_modules
    ├── package-lock.json
    ├── package.json
    ├── postcss.config.mjs
    ├── public
    ├── src
    └── tsconfig.json
```

## 🚀 Como Rodar Localmente

### Pré-requisitos
- Python 3.11+
- Node.js 18+
- Git

### Configuração do Projeto
1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/leocsbh007/back_lt_pedidos.git # (Substitua pelo URL correto do seu projeto completo se for um monorepo)
    cd back_lt_pedidos
    ```
    *   **Importante:** Se o frontend e o backend estiverem em repositórios separados, clone ambos. Se for um monorepo (`lt-pedidos/`), clone apenas a raiz e navegue para `back_lt_pedidos` ou `front_lt_pedidos` conforme necessário. As instruções abaixo assumem que você está no diretório `back_lt_pedidos`.

2.  **Instale as dependências do backend com Astral UV:**
    ```bash
    uv sync
    ```
    *   **Explicação:** Este comando instala todas as dependências listadas no `pyproject.toml` (incluindo as de desenvolvimento se você estiver em ambiente de dev) e garante que o `uv.lock` esteja atualizado.

### Backend
1.  **Navegue para o diretório do backend:**
    ```bash
    cd back_lt_pedidos # Se você não estiver já nele
    ```
2.  **Execute a API FastAPI:**
    ```bash
    uv run fastapi dev app.main:app
    ```
    *   A API estará disponível em `http://127.0.0.1:8000`.
    *   A documentação interativa (Swagger UI) pode ser acessada em `http://127.0.0.1:8000/docs`.

### Frontend
1.  **Navegue para o diretório do frontend:**
    ```bash
    cd ../front_lt_pedidos # Ou o caminho correto para o seu frontend
    ```
2.  **Instale as dependências:**
    ```bash
    npm install
    ```
3.  **Inicie a aplicação frontend:**
    ```bash
    npm run dev
    ```
    *   A aplicação frontend estará disponível em `http://localhost:3000` (ou outra porta padrão do Next.js).

## 📝 Contribuições e Boas Práticas (Conventional Commits)

Este projeto adota **Conventional Commits** para padronizar as mensagens de commit. Isso facilita o rastreamento de mudanças, a geração automática de `CHANGELOG.md` e a compreensão do histórico do projeto.

-   **Use `uv run cz commit`**: Para criar seus commits, garantindo que as mensagens sigam o padrão. O Commitizen irá guiá-lo interativamente.

    ```bash
    uv run cz commit
    ```

-   **Exemplo de Tipos de Commit:**
    -   `feat`: Uma nova funcionalidade.
    -   `fix`: Correção de um bug.
    -   `docs`: Mudanças na documentação.
    -   `chore`: Mudanças na construção, dependências ou ferramentas.
    -   `refactor`: Mudança no código que não corrige um bug nem adiciona uma feature.
    -   `perf`: Melhoria de performance.
    -   `test`: Adição ou refatoração de testes.
    -   `build`: Mudanças que afetam o sistema de build ou dependências externas.
    -   `ci`: Mudanças nos arquivos e scripts de CI.
    -   `revert`: Reversão de um commit anterior.

-   **Geração de Changelog e Versionamento:**
    O `CHANGELOG.md` é gerado automaticamente e o versionamento é gerenciado com o comando `uv run cz bump`, que incrementa a versão (PATCH, MINOR, MAJOR) com base nos tipos de commits e nas breaking changes.

    ```bash
    uv run cz bump
    ```

## 📊 Status do Projeto

🚧 **Em desenvolvimento** - Etapa 1: Fundação e Arquitetura

## 👨‍💻 Autor

**Leonardo Castro de Souza**
- GitHub: [leocsbh007](https://github.com/leocsbh007)
- LinkedIn: [Leonardo Souza](https://www.linkedin.com/in/leonardo-souza-2a83b11a/)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
