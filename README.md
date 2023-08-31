The Project is about "Simulate THE CDN upload and retrieval processes"

There is two part of the project :
1. The 'venv' file contains all python files.
2. The 'Kong API Gateway' contains docker-compose which can run Kong service.

To build Kong service(In Linux environment):
1. git clone https://github.com/elvis8546/Novatech_Project.git
2. cd ./Novatech_Project
3. cd docker-kong/compose/
4. KONG_DATABASE=postgres docker-compose --profile database up

Some command to operation in Kong:
1. Create a Service:
  curl -i -X POST --url http://localhost:8001/services/ --data 'name=your-service' --data 'url=http://my-backend-api.com'
2. Create a Route:
  curl -i -X POST --url http://localhost:8001/services/your-service/routes --data 'paths[]=/my-api'
3. Test Your API:
  curl http://localhost:8000/my-api
4. To list all services:
  curl -i http://localhost:8001/services (Can open in web browser with URL) 
5. To list all routes:
  curl -i http://localhost:8001/routes (Can open in web browser with URL) 

Some default setting create by me:
1. name=CDN-service
2. url=http://CDN-api.com
3. 'paths[]=/test-CDN-api'

Back to the Python run:
1. simulateCDN.py includes all functions to interact with Kong.
2. API URL setting in line#5
3. main.py is the start point of program
4. In terminal,cd under the 'venv' and type python main.py(with python2.x) or python3 main.py(with python3.x) to run the program!

