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
- **Astral uv 0.8.17+** - Gerenciador de pacotes python
- **FastAPI** - Framework web moderno e rápido
- **Pandas** - Processamento de dados Excel
- **SQLAlchemy** - ORM para banco de dados
- **Pytest** - Testes automatizados
- **ReportLab** - Geração de PDFs

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

```
lt-pedidos/
.
├── back_lt_pedidos
│   ├── LICENSE
│   ├── README.md
│   ├── app
│   ├── pyproject.toml
│   └── uv.lock
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

### Backend
```bash
git clone https://github.com/leocsbh007/back_lt_pedidos.git
cd back_lt_pedid/app/
uv run fastapi dev main.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📊 Status do Projeto

🚧 **Em desenvolvimento** - Etapa 1: Fundação e Arquitetura

## 👨‍💻 Autor

**Leonardo Castro de Souza**
- GitHub: [leocsbh007](https://github.com/leocsbh007)
- LinkedIn: [Leonardo Souza](https://www.linkedin.com/in/leonardo-souza-2a83b11a/)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
