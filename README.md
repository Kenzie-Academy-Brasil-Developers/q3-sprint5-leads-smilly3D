# Leads

## POST /api/leads

### Registrar um novo Lead no banco de dados.

#### Modelo de requisição:

    POST - localhost:5000/leads

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

    GET - localhost:5000/leads

---

## PATCH /api/leads

### Registrar um novo Lead no banco de dados.

#### Modelo de requisição:

    PATCH - localhost:5000/

    {
        "email": "john@email.com"
    }

---

## DELETE /api/leads

### Registrar um novo Lead no banco de dados.

#### Modelo de requisição:

    DELETE - localhost:5000/

    {
        "email": "john@email.com"
    }
