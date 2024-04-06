1- Consistency:

GET https://api.example.com/v1/users
POST https://api.example.com/v1/users
PUT https://api.example.com/v1/users
DELETE https://api.example.com/v1/users


GET /GetUsersInfo
PUT /UpdateUserInfo
DELETE /DeleteUserInfo
POST /CreateUserInfo

2- Error handling:
{"user not found"}
{"user already exists"}
{"endpoint not found"}
{"method not allowed"}
/users/{id} -> {"user not found"} {"not allowed to acces the information"}
/users/8637867863 -> {"user exists"}

3- Security:
API_KET / API_SECRET
JWT
OAuth2
Basic Auth
token

4. INPUT VALIDATION:
- Validate the input data
"naoufal@naoufal.com" -> "Select * from users where email = ?"

5. Response formatting:
- JSON
UPDATE /users/{ID}
'{"status": "Added correctly"}'


6- Pagination and filtering
GET /users/{city}?date=2025-01-01&limit=10&offset=20


7- Documentation:
8- Testing and monitoring:
9- version control:

10- Use singular nouns for resource names
- Good: /user/{ID}
- Bad: /users/{ID}
- good : /product/{ID}
- bad : /products/{ID}
- good : /orders
- good : /user/{ID}/orders/{order_id}/title
- bad : /getOrderByUserID/{ID}
- bad : /getOrderByUserTitle/{TITLE}
