# fabric

```
docker-compose up --build -d
```

Не забудте создать суперпользователя в системе чтобы управлять опросами.

http://0.0.0.0:8000/admin/poll/ - GET, POST  
  GET - список всех опросов  
  POST - добавление опроса  
    Пример:  
```
 {  
    "poll": {  
          "name": "test",  
          "begin_date": "2020-12-05",  
          "end_date": "2020-12-25",  
          "description": "test description"  
      }  
  }  
```

http://0.0.0.0:8000/admin/poll/{id}/ - GET, DELETE, PUT  
  GET - один опрос с заданным id  
  DELETE - удаление опроса с заданным id  
  PUT - изменение опроса с заданным id (можно частично), при изменении begin_date это поле будет проигнорированно  

http://0.0.0.0:8000/admin/question/  
http://0.0.0.0:8000/admin/question/{id}/  
  Аналогично опросам управление вопросами  
  Пример:  
```
{
  "question": {
        "poll": 1,
        "text": "Test Question",
        "type": 1,
        "choices": [
          "aba",
          "caba"
        ]
    }
}
```
  0 type - это ответ текстом, 1 - выбор из списка, 2 - множественный выбор. При type=0 поле choices можно оставить null.  

http://0.0.0.0:8000/poll/ - GET  
  Не требует авторизации, выдает список не истекших опросов с вопросами в них  

http://0.0.0.0:8000/answer/{id}/ - GET, POST  
  GET - Получение списка всех своих ответов с информацией о том, к каким опросам и вопросам они относились  
  POST - Добавление ответа (изменение ответа или добавление другого не предусмотрено)  
    Примеры:  

```
Если тип вопроса 0: {
  "answer": {
        "question": 1,
        "answer": "Test Answer"
    }
}

Если тип вопроса 1: {
  "answer": {
        "question": 1,
        "answer": ["Test Choice"]
    }
}

Если тип вопроса 2: {
  "answer": {
        "question": 1,
        "answer": ["Test Choice1", "Test Choice2", "Test Choice3"]
    }
}
```
