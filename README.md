# exam-hanter-digital-2
# run 
`docker compose up -d`
## files
dal.py  for all queries.
routes.py for endpoints.
## flue
server up in main.py using in lifespan of fastapi wight for mysql connection 
in each endpoint we send the client to function execute_query that create cursor and return the result in list from mysql server  
