Hola Tomas!

Respuestas estandar de la API

Exito:

```json
   {
      "status": "success",
      "statusCode": 200-299,
      "data": {
         "...."
      } | [{
         "...."
      }]
      "meta": {}
   }
```

Error:

```json
   {
      "status": "error",
      "statusCode": 300-599,
      "errors": [{
         "code": "MEANINGFULL STRING",
         "message": "Meaningfull message",
         "meta": {}
      }],
      "type": "VALIDATION" | null,
      "displayMessage": "algo a mostrar al usuario"
   }

```

Base de datos:

Tablas:

- MeliAccount (meli_accounts):
  - `id` -> integer primary key (mismo ID que maneja mercado libre)
  - `nickname` -> string (nombre de usuario de ML)
  - `access_token` -> string encriptado
  - `refresh_token` -> string encriptado
  - `token_expiration` -> string | integer (fecha en la que expira el access token)
  - `hello` -> string (mensaje de saludo para responder preguntas, si podria ir en otra tabla)
  - `signature` -> string (mensaje de despedida para responder preguntas, si podria ir en otra tabla)
- ItemDescription (item_descriptions):
  - `id` -> primary key uuid o formato de ID que te guste
  - `account_id` -> integer referencia a `meli_accounts`
  - `text` -> text (texto de la descripcion)
  - `description` -> string (descripcion de la descripcion, para reconocerla)
  - `name` -> string (nombre de la descripcion para reconocerla)
- QuickAnswer (quick_answers):
  - `id` -> primary key uuid o formato de ID que te guste
  - `account_id` -> integer refencia a `meli_accounts`
  - `text` -> string (contenido de la respuesta rapida)
  - `color` -> string (color de la respuesta rapida)
  - `name` -> string
  - `order` -> integer (para ver si logramos que sean reordenables)
- AutomaticMessage (automatic_messages):
  - `id` -> primary key uuid o formato de ID que te guste
  - `account_id` -> integer refencia a `meli_accounts`
  - `text` -> text (bueno creo que se entiende que es)
  - `enabled` -> boolean (define esta activo o no al momento de mandarlo)
  - `description` -> string (para reconocerlo bien)
  - `name` -> string (para que tenga nombre)
  - `trigger` -> string (en que evento se enviaria nosotros definimos cuales son los eventos disponibles por ahora "on_pickup_sale" o el nombre que mas te gusta)
- Question (questions):
  - `id` -> integer primary key (mismo ID que usa ML para la pregunta)
  - `seller_id` || `account_id` -> integer con referencia a `meli_accounts`
  - `date_created` -> timestamp
  - `from_id` -> integer
  - `item_id` -> string
  - `status` -> string
  - `answer` -> json (`{ text: string, date_created: string | timestamp, status: string }`)
