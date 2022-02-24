# Leads
## base api: https://entrega-19-leads15.herokuapp.com

## POST /api/leads

### Registrar um novo Lead no banco de dados.

#### Modelo de requisição:

    POST - https://entrega-19-leads15.herokuapp.com/api/leads

    {
        "name": "John Doe",
        "email": "john@email.com",
        "phone": "(41)90000-0000"
    }

#### Modelo de resposta:

    {
        "name": "John Doe",
        "email": "john@email.com",
        "phone": "(41)90000-0000",
        "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
        "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
        "visits": 1
    }

---

## GET /api/leads

### Listar todos os LEADS por ordem de visitas, do maior para o menor.

#### Modelo de requisição:

    GET - https://entrega-19-leads15.herokuapp.com/api/leads

---

## PATCH /api/leads

### Registrar um novo Lead no banco de dados.

#### Modelo de requisição:

    PATCH - https://entrega-19-leads15.herokuapp.com/api/leads

    {
        "email": "john@email.com"
    }

---

## DELETE /api/leads

### Registrar um novo Lead no banco de dados.

#### Modelo de requisição:

    DELETE - https://entrega-19-leads15.herokuapp.com/api/leads

    {
        "email": "john@email.com"
    }
