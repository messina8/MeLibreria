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
- User (users):
  - `id`
  - `email`
  - `password`
  - `active_account`
  - `role`

Autenticacion: no permitir registros nuevos, un usuario admin por default que se verifica que exista cada vez que se reinicia la aplicación. Para crear nuevos usuarios lo hace este usuario u otro al cual se le asignen los permisos para hacerlo. Sesiones de DB para las sesiones de autenticación. (Con cookies? JWT?)

Endpoints que usan cuentas de MELI: al recibir la request revisar el valor de `active_account` del usuario y trabajar el pedido sobre esa cuenta.

Autorizacion de cuentas de MELI:

- Endpoint para pedir la URL de autorizacion con los parametros necesarios + el state por seguridad.
- Endpoint para recibir el Code de ML a intercambiar por las access_tokens , y el state que tiene que ser verificado.
- Pensar como manejar permisos para usar X cuenta por Y usuario. (una tabla intermedia de users_meli_accounts_allowed?)

Endpoint de notificaciones de MELI:

- Tiene que recibir POST request que meli envia con notificaciones sobre eventos sucedidos en la plataforma, hay que distingir entre los tipos de eventos y procesarlos de las manera necesaria. (orders, items, questions) (optimo seria que esto se procese con una queue para tener retries y no estar corriendo el codigo en el ciclo de la request)
