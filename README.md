<!-- 
# comp-calendar
Ele trabalha om a logica de construção de compiladores pra criar comandos que serão uteis para API Google Calendar
-->

> Projeto de Construção de Compiladores, 2ee, 2025.1

# Compilador para comandos ao Google Calendar API
## Alunos
- Claudio Roberto
- Ruan de Melo
- Sócrates Farias
- Vinícius Ribeiro

### O que faz?
Permite fazer...

### qual o Intuito
Que um usuário possa...

> foco: facilitar

### Como ultilizar?
Siga o flow abaixo, para ultiliza-lo direto do codespaces!

1. abra o terminal do codespaces e use:
    - ```bash
      pip install antlr4-python3-runtime    # o reconhecedor
      pip install google-api-python-client  # a API do google
      pip install google-auth               # pack para autenticação
      ```
      para instalar as dependencias 

    - `cd src`, para navegar a pasta
<!--2. descopacte o `token.zip` ou coloque um `token.json` da sua conta -->
2. considere colocar um `token.json` de outra conta ou entre na nossa: ...
3. coloque os seus comandos no `input.txt`
    COMANDOS DISPONIVEIS:
    - `criar evento "NOME" DD-MM-AAAA HH:MM DD-MM-AAAA HH:MM` que cria evento
        <br>ex: `criar evento "Projeto compiladores" 04-07-2025 08:50 04-07-2025 10:30`
        <br>onde:
        - `"NOME"` é o nome do seu evento
        - `DD-MM-AAAA HH:MM` é o formato de dia e hora do seu evento
            > note que no comando você tem que coloar o dia/hora do inicio e o dia/hora do fim do evento
        <br>

    - `deletar evento DD-MM-AAAA` que deleta o evento do dia
    <br>ex: deletar evento 04-07-2025
    <br>

3. inicie o script no formato `python main.py input.txt`...
<!--4. ultilize o comando `tal` para...-->
4. abra o [Google Calendar]() e confira!<!--TODO: POR O LINK-->

<!--ver o que luis pediu pra ser feito-->

---