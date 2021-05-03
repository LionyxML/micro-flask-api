# micro-flask-api

Uma micro API escrita em python/flask para usar de esqueleto.

A micro API written in Python/Flask to use as an skelethon.

# Uso / Usage


```.../api/usuario/todos
```

Retorna toda a tabela / Returns the entire Table:

```
[{"habilidade":"Programar apis","id":0,"nascimento":"07/08/1986","nome":"Rahul","sobrenome":"Juliato"},{"habilidade":"Programar churrasco","id":1,"nascimento":"07/08/1955","nome":"Beto","sobrenome":"Juliato"},{"habilidade":"Desenhi coisi legalzi","id":2,"nascimento":"10/10/1982","nome":"Menini","sobrenome":"Piologui"}]
```

##

```.../api/usuario?id=0
```
or
```.../api/usuario/?id=0
```


Retorna informação do usuário de id 0 / Returns info of user with id 0:

```
[{"habilidade":"Programar apis","id":0,"nascimento":"07/08/1986","nome":"Rahul","sobrenome":"Juliato"}]
```
