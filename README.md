# 🚀 Mini IDP – Scaffolding Platform

> **Mini Internal Developer Platform (IDP)** para geração automática de projetos de software a partir de templates padronizados.

Este projeto foi desenvolvido no âmbito de uma **cadeira universitária**, com o objetivo de aplicar conceitos modernos de **engenharia de software**, **automação** e **Internal Developer Platforms**.

---

## 📌 Motivação

Em muitos contextos académicos e profissionais, a criação de novos projetos é feita através de **cópia manual de repositórios**, o que frequentemente resulta em:

* Erros de configuração
* Estruturas inconsistentes
* Perda de tempo
* Falta de padronização

A **Mini IDP** resolve este problema ao fornecer um **gerador automático de projetos (scaffolding)**, garantindo rapidez, consistência e organização.

---

## ✨ Funcionalidades Principais

✔ Geração automática de projetos
✔ Templates reutilizáveis
✔ Interface Web simples e intuitiva
✔ Catálogo de projetos criados
✔ Download do projeto em formato **ZIP**
✔ Estrutura padronizada pronta para uso

---

## 🧩 Templates Disponíveis

### 🟦 API Python

* Flask
* Estrutura base para APIs REST
* `requirements.txt`
* `Dockerfile`
* `README.md`

### 🟩 Fullstack Python

* Backend Flask
* Frontend HTML
* Estrutura base para aplicações web
* Suporte a Docker

---

## 🖥️ Interface Web

A plataforma disponibiliza uma interface web onde o utilizador pode:

1. Introduzir o nome do projeto
2. Escolher o template
3. Definir o responsável
4. Gerar o projeto automaticamente
5. Fazer o download do projeto em `.zip`

📦 **Tudo em poucos cliques**

---

## 🗂️ Catálogo de Projetos

Todos os projetos criados são registados automaticamente num catálogo (`catalog.json`) contendo:

* Nome do projeto
* Tipo de template
* Responsável
* Data de criação

O catálogo pode ser consultado diretamente pela interface web.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Flask**
* **HTML5**
* **CSS / Bootstrap**
* **Bootstrap Icons**
* **Docker** (nos templates)
* **Git & GitHub**

---

## 📁 Estrutura do Projeto

```
mini-idp-scaffolding/
├── web/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── catalog.json
│
├── templates/
│   ├── api-python/
│   └── fullstack-python/
│
├── generated/   (ignorado no Git)
├── README.md
└── .gitignore
```

---

## ▶️ Como Executar o Projeto

```bash
cd web
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Aceder no navegador:

```
http://127.0.0.1:5000
```

---

## 🎓 Contexto Académico

Este projeto foi desenvolvido como projeto  **PLATAFORMA DE DESENVOLVIMENTO DE SOFTWARE**, com foco em:

* Internal Developer Platforms (IDP)
* Automação do desenvolvimento
* Boas práticas de engenharia de software
* Organização e reutilização de código

---

## 🔮 Trabalhos Futuros

* Autenticação de utilizadores
* Integração com GitHub/GitLab
* Mais templates (Node.js, Java, PHP)
* Persistência em base de dados
* Pipeline CI/CD

---

## 👨‍💻 Autor

**Domingos Bié**


---

## ⭐ Conclusão

A **Mini IDP – Scaffolding Platform** demonstra que é possível aplicar conceitos modernos de plataformas internas de desenvolvimento mesmo em contextos académicos, promovendo **produtividade**, **qualidade** e **padronização** no desenvolvimento de software.

---
