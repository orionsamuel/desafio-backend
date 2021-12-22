CRUD para cadastro de alunos de uma escola.

O CRUD foi desenvolvido em Python com o framework Django;

O banco de dados utilizado foi o SQLite;

A aplicação conta com um sistema de login. O usuário de para acessar a aplicação se chama 'teste' e a senha é 'AbC123789';

O CRUD contém os seguintes campos: 

-Pasta: um valor numérico para a referência de uma pasta onde o nome do aluno ficaria;
-Ano: ano de ingresso do aluno na escola:
-Nome: nome do aluno;
-Filiação: nome de um dos pais do aluno;

O sistema conta com um botão de cadastro de aluno. Depois de cadastrado o aluno em questão aparecerá listado na tela inicial, juntamente de mais dois botões, um de alterar os dados cadastrados e outro para excluir o cadastro;

Para acessar o sistema precisa ter o Python instalado no computador. Todas as libs necessárias estão presentes no ambiente virtual Python;

Abra o terminal dentro da pasta do projeto e digite o comando 'source venv/bin/activate' para entrar no ambiente virtual;

Já dentro do ambiente virtual executar o comando 'python manage.py runserver'. Para inciar a aplicação precisa digitar no navegador o endereço 'localhost:8000';
