ChimpTech - Gerador de Orçamento

Aplicação web para gerar orçamentos de serviços de assistência técnica, desenvolvida em Python com Streamlit. Permite adicionar múltiplos serviços, aplicar desconto configurável e baixar o orçamento final em .txt.

App publicado: https://chimptech-orcamento.streamlit.app

- Funcionalidades
Cadastro do nome do cliente
Adição de múltiplos serviços (um por vez, com nome e valor)
Cálculo automático do valor total
Desconto configurável por percentual (aplicado sobre orçamentos acima de R$ 500)
Geração e download do orçamento em arquivo .txt
Botão para iniciar um novo orçamento sem recarregar a página

- Tecnologias
Python
Streamlit — interface web
Programação Orientada a Objetos — lógica encapsulada na classe Orcamento

Como rodar localmente

1. Clone o repositório:
git clone https://github.com/lucasfollmann/chimptech-orcamento.git
cd chimptech-orcamento

2. Instale as dependências:
pip install streamlit

3. Execute o app:
streamlit run app.py

4. Acesse http://localhost:8501 no navegador.


Sobre o projeto

Este projeto foi desenvolvido como forma de aplicar na prática os fundamentos de Python 
(lógica, listas, laços, funções, POO) em uma ferramenta real,
usada no dia a dia da ChimpTech (assistência técnica, desenvolvimento web e automação de processos).  

Autor

Lucas Ademir Follmann Técnico de Suporte de TI | Estudante de Análise e Desenvolvimento de Sistemas
Linkedin - https://www.linkedin.com/in/lucas-follmann/