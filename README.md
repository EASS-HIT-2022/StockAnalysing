# Stock Analysing
aplication will analyze text sentiment of twiter posts about stock
# Design 
![Alt text](pictures/design.drawio.png?raw=true "Design")

# How to run :
## beckend :
```bash
docker-compose up -d --build  
```
navigat to ```http://localhost:8888/docs```

![Alt text](pictures/fastapi.png?raw=true "FastApi")

## response with cloudflare stock:
![Alt text](pictures/search.png?raw=true "Search")
list of last 24 hours twits
## tests :
```bash
docker-compose exec web pytest .  
```
at now there are two tests 
![Alt text](pictures/tests.png?raw=true "Search")
