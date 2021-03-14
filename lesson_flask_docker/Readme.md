This is an application for hosting own passwords aon own servers to eliminate any access of 3rd parties.

TODO:
1. Add user auth
2. Add encryption
3. Move encryption to the client side not to send a password not encrypted via the network.

To run in develop,emt:  
docker-compose up  

To run in production:
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
