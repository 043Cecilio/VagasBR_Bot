<div align="center">

# TechVagas Bot

### Bot de Notificações Automáticas de Vagas Tech via Telegram

*Monitorando o mercado. Notificando oportunidades. Automatizando a busca.*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram_Bot_API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

</div>

---

## 📌 Sobre o Projeto

**TechVagas Bot** é um robô desenvolvido em Python que monitora periodicamente vagas de emprego na área de tecnologia no mercado nacional e envia notificações automáticas diretamente para o Telegram, mantendo o usuário sempre atualizado sem a necessidade de buscas manuais repetitivas.

> **Contexto:** Projeto desenvolvido para automatizar e otimizar a rotina de busca por oportunidades de trabalho em tecnologia, eliminando a necessidade de checar múltiplas plataformas manualmente.

---

## Arquitetura e Estrutura de Pastas

O projeto adota uma **arquitetura serverless orientada a eventos**, onde o GitHub Actions atua como agendador (scheduler), executando o script Python em intervalos definidos sem necessidade de servidor dedicado.

```
techvagas-bot/
│
├── .github/
│   └── workflows/
│       └── bot.yml                # 🔵 Workflow de automação (cron job)
│
├── src/
│   ├── main.py                    # Ponto de entrada do bot
│   ├── scraper.py                 # Coleta e parsing das vagas
│   ├── telegram_notifier.py       # Envio de mensagens via Telegram API
│   ├── filters.py                 # Filtros de palavras-chave e área tech
│   └── storage.py                 # Controle de vagas já notificadas
│
├── data/
│   └── sent_jobs.json             # Histórico de vagas já enviadas
│
├── .env.example                   # Modelo de variáveis de ambiente
├── requirements.txt
└── README.md
```

---

## Status de Desenvolvimento

### Back-end — Python + Telegram Bot API

| Funcionalidade | Status |
|---|---|
| Coleta automática de vagas em fontes tech | ✅ Concluído |
| Filtro por palavras-chave (linguagens, senioridade, área) | ✅ Concluído |
| Integração com Telegram Bot API | ✅ Concluído |
| Controle de duplicidade (não reenviar vagas já notificadas) | ✅ Concluído |
| Formatação de mensagens (título, empresa, link, localização) | ✅ Concluído |
| Tratamento de erros e logs de execução | ✅ Concluído |

### Automação — GitHub Actions

| Funcionalidade | Status |
|---|---|
| Workflow agendado (cron) para execução periódica | ✅ Concluído |
| Gerenciamento de variáveis sensíveis via Secrets | ✅ Concluído |
| Cache de dependências Python | ✅ Concluído |
| Persistência do histórico entre execuções | ✅ Concluído |
| Execução manual via workflow_dispatch | ✅ Concluído |

---

## Destaques Técnicos

### Automação Sem Servidor via GitHub Actions
O bot não depende de infraestrutura própria ou serviços de hospedagem pagos. O GitHub Actions executa o script Python em containers temporários, seguindo um cron schedule pré-definido, garantindo execuções recorrentes com custo zero e alta confiabilidade.

### Controle de Duplicidade de Notificações
Cada vaga coletada é identificada por um hash único (gerado a partir do título, empresa e link). Esse identificador é armazenado em `sent_jobs.json` e versionado entre as execuções, garantindo que a mesma vaga nunca seja notificada duas vezes ao usuário.

### Filtros Inteligentes de Área Tech
O sistema aplica filtros configuráveis por palavras-chave (ex: "desenvolvedor", "júnior", "backend", "frontend", "Python", "Java"), permitindo que o usuário receba apenas notificações relevantes ao seu perfil profissional, reduzindo ruído e aumentando a assertividade.

---

## Roadmap

```
[✅] Coleta automática de vagas tech
[✅] Integração com Telegram Bot API
[✅] Filtros por palavras-chave e área de atuação
[✅] Controle de vagas duplicadas
[✅] Agendamento via GitHub Actions (cron)
[ ] Suporte a múltiplas fontes de vagas simultâneas
[ ] Filtro por localização (remoto, presencial, híbrido)
[ ] Painel de configuração via comandos no Telegram
[ ] Dashboard de estatísticas (vagas enviadas, fontes ativas)
```

---

## ▶️ Como Executar Localmente

Siga os passos abaixo para configurar e testar o bot em ambiente de desenvolvimento.

### Pré-requisitos

Certifique-se de ter:

- [Python 3.10+](https://www.python.org/)
- [Git](https://git-scm.com/)
- Um bot criado no Telegram via [@BotFather](https://t.me/BotFather) (Token de acesso)
- O `chat_id` do canal, grupo ou usuário que receberá as notificações

---

### 1. Clone o repositório

```bash
git clone https://github.com/043Cecilio/techvagas-bot.git
cd techvagas-bot
```

---

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

No Windows:
```bash
.\venv\Scripts\activate
```

No Mac / Linux:
```bash
source venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

---

### 5. Execute o bot manualmente

```bash
python src/main.py
```

---

## ⚙️ Configuração da Automação (GitHub Actions)

Para que o bot rode automaticamente em intervalos definidos, é necessário configurar os **Secrets** do repositório:

1. Acesse **Settings → Secrets and variables → Actions**
2. Adicione os seguintes secrets:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`

O workflow em `.github/workflows/bot.yml` já está configurado para executar o script periodicamente via `cron`, podendo também ser disparado manualmente pela aba **Actions** do repositório.

---

## Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.10+ |
| Notificações | Telegram Bot API |
| Automação / CI | GitHub Actions (cron + workflow_dispatch) |
| Armazenamento | JSON (histórico de vagas) |
| Gerenciamento de Segredos | GitHub Secrets |
| Versionamento | Git e GitHub |


<div align="center">

Desenvolvido por **Gabriel Cecilio Menezes**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/gabriel-cecilio-bb938035b)

</div>
