# Membros
* Cayque Cicarelli - 22.221.005-6

* Bruna Paz - 22.121.020-6

* Matheus Miranda - 22.22.0017-2

***

# Chatbot PIPE FAPESP

Este chatbot foi desenvolvido para ajudar uma empresa e/ou um pesquisador a submeter um projeto PIPE (Pesquisa Inovativa em Pequenas Empresas) e auxiliar um usuário com suas dúvidas.

## Funcionalidades

- Responde a perguntas sobre o programa PIPE da FAPESP.
- Fornece informações sobre como submeter um projeto para a PIPE.
- Explica os benefícios e requisitos para participar da PIPE.
- Inclui um easter egg escondido que inicia um jogo da cobra (Snake).

## Como Baixar o Chatbot

1. **Baixe os arquivos importantes**:
   - Baixe em sua máquina os arquivos `main.py`, `chatbot.py` e `intents.json`.
   - Baixe todas as dependências necessárias como `nltk, tensorflow e keras`.

## Como Usar

1. **Iniciar o Chatbot**:
   - Execute o script `main.py` para iniciar o chatbot (certifique-se de ter todas as extensões instaladas).
   - No terminal, você verá a mensagem de boas-vindas: `Bem vindo ao Chatbot`.

2. **Fazer Perguntas**:
   - Digite suas perguntas no terminal e pressione Enter.
   - O chatbot responderá com base nas intenções definidas no arquivo `intents.json`.

3. **Exemplos de Perguntas**:
   - "O que é a PIPE?"
   - "Como submeter um projeto para a PIPE?"
   - "Quais são os benefícios da PIPE?"
   - "Quais são os requisitos para participar da PIPE?"
   - "Onde posso encontrar mais informações?"

4. **Easter Egg**:
   - Existe um easter egg escondido no projeto.
   - Digite "Easter Egg" no terminal para iniciar um jogo da cobra (Snake).
   - Use as teclas de seta para controlar a cobra e comer a comida.
   - Quando o jogo terminar, a pontuação será exibida e o chatbot continuará a interação.

## Exemplo de Uso

```sh
$ python main.py
Bem vindo ao Chatbot

como posso te ajudar?
> O que é a PIPE?
O Programa FAPESP Pesquisa Inovativa em Pequenas Empresas (PIPE) apoia a execução de pesquisa científica e/ou tecnológica em pequenas empresas no Estado de São Paulo.   [pipe_fapesp]

posso lhe ajudar com algo a mais?
> Como submeter um projeto para a PIPE?
Para submeter um projeto para a PIPE, você deve seguir as diretrizes disponíveis no site da FAPESP e preencher o formulário de submissão online.   [submissao_pipe]

posso lhe ajudar com algo a mais?
> Easter Egg
Uma partida de Snake que acaba quando o jogador perde.
