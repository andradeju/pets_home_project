# Projeto Abrigo de Animais | Pet's Home

Este projeto é parte do Bootcamp de Back-End da WoMakersCode e tem como objetivo criar um site para um abrigo de animais utilizando Python e o framework Django aplicando as melhores práticas e conceitos de controle de versão.

## Sobre o Projeto

O projeto final deste Bootcamp de Back-End visa consolidar e aplicar o conhecimento adquirido em GitHub, HTML5, CSS3, Bancos de Dados e o Framework Django.  

## Tecnologias

- **Python**
- **Django**
- **HTML5, CSS3 e Bootstrap**
- **SQLite**


## Estrutura e Requisitos

O projeto inclui as seguintes funcionalidades:

- **Página Inicial**: Página inicial com todos os animais disponíveis para adoção.
- **Páginas de Detalhes**: Para visualização individual dos animais, incluindo informações como nome, espécie, idade, raça, histórico de saúde e imagens.
- **Gestão de Adoções**: Sistema de gerenciamento de adoções, onde os interessados podem solicitar a adoção de um animal e os responsáveis pelo abrigo podem aprovar ou recusar as solicitações.
- **Barra de Pesquisa**: Barra de pesquisa que permite aos usuários procurar animais disponíveis para adoção por palavras-chave, espécie, raça, etc.

## Deploy do Site
O site está disponível online, clique aqui: **[Pet's Home](https://julianasantos.pythonanywhere.com/)** <br>
Visite o link para explorar as funcionalidades e conhecer os animais disponíveis para adoção.

## Rodando o Projeto Localmente

1. **Clone o Repositório:**
```bash
git clone https://github.com/andradeju/pets_home_project.git
```   
2. **Crie e Ative o Ambiente Virtual:**
```bash
python -m venv venv
```
  No Windows:  *.\venv\Scripts\activate* <br>
  No Mac/Linux:  *source venv/bin/activate*

3. **Instale as Dependências:**
```bash
pip install -r requirements.txt
```
```bash
pip freeze > requirements.txt
```
4. **Aplicar Migrações:**
```bash   
python manage.py migrate
```
5. **Iniciar o Servidor:**
```bash
python manage.py runserver
```
Agora, você pode acessar o seu projeto em **http://localhost:8000/**


