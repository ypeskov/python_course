# Password Manager  

This is an application for hosting own passwords aon own servers to eliminate any access of 3rd parties.

---
To run in development:  
**docker-compose up**  

To run in production:  
**docker-compose -f docker-compose.yml -f docker-compose.prod.yml up**

---
TODO:
1. Add user auth
2. Add encryption
3. Move encryption to the client side not to send a password not encrypted via the network.
4. Change delete functionality from HTTP GET -> POST


