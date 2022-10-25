# Steps to run the app
1. git clone https://github.com/tara-9/budget-builder
2. cd budget-builder
3. py -m venv .venv
4. pip install -r requirements.txt
5. flask run
6. curl --location --request GET 'http://localhost:5000' --header 'Content-Type: application/json' --data-raw '{"gender": "male"}'. Hit this curl command
