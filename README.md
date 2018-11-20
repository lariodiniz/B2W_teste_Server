StarWarsPlanet
=

    Api REST feito em Python utilizando o microframeowrk Flask que pode conter os dados de planetas do Star Wars 

Técnologias Utilizadas
-
- Python 3.7.1 
- MongoDB
- Flask
- Para mais informações veja [Requeriments](https://github.com/lariodiniz/StarWarsPlanet/blob/master/requeriments.txt) 

Funcionalidades 
-
- Adicionar um planeta (com nome, clima e terreno)
- Busca automaticamente na api [SwApi](https://swapi.co/) em quantos filmes o planeta apareceu quando o planeta é adicionado.
- Listar planetas
- Buscar por nome
- Buscar por ID
- Remover planeta por nome 
- Remover planeta por id

Como Contribuir
-
1) Instale o Git na sua maquina.
<br>Para mais informações sobre o git veja [Git](https://git-scm.com/docs).
2) faça um fork para o seu repositório Git.
3) Clone esse repositório para a sua maquina.
4) Na pasta clonada da sua maquina inicie o git flow.
<br>Para mais informações sobre o git flow veja [Git Flow](https://medium.com/@lariodiniz/tutorial-git-com-git-flow-476ad906c8ae).
5) Crie uma maquina virtual com o python 3.7.1.
6) Instale os Requerimentos.
7) Crie um braço de feature e faça suas modificações, não esqueça de fazer testes para as mesmas.
8) Ao finalizar solicite um Pull Request. 
 
Como Testar
-
1) Entre na pasta sw_server.
2) Com seu ambiente virtual ativado rode o comando no prompt: coverage run -m pytest
<br>As Bibliotecas pytest e coverage devem esta instaladas no seu ambiente virtual.
3) Rode o comando no prompt: coverage html 
4) uma pasta chamada htmlcov será criada dentro da pasta sw_server contendo informações sobre quanto do seu código esta sendo testado.

Licença
-
[MIT](https://github.com/lariodiniz/StarWarsPlanet/blob/master/LICENSE.md)

![Python](https://github.com/lariodiniz/StarWarsPlanet/blob/develop/imgs/python_logo.png)
![Flask](https://github.com/lariodiniz/StarWarsPlanet/blob/develop/imgs/flask_logo.jpg)
![Mongodb](https://github.com/lariodiniz/StarWarsPlanet/blob/develop/imgs/mongodb_logo.png)