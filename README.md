# Advertisement Management System

This project is an Advertisement Management System that allows users to create, view, edit, and delete ads. Users can also comment on ads and interact with the system after authentication. The system is built as a RESTful API using Python, with PostgreSQL as the database, and incorporating ORM (Object Relational Mapping) for data management.

## Features

- **Authentication:** Users need to authenticate to perform actions such as adding ads and comments. Registration requires a unique email as the username and password.
- **Commenting:** Each user can only comment on an ad once.
- **Viewing Ads:** Users can view ads and their related comments without logging in.
- **Editing and Deleting Ads:** Users can edit and delete their own ads.

## Technical Specifications

- **Framework:** The project is built using the popular Python web frameworks (Django).
- **Database:** PostgreSQL is used as the database management system.
- **ORM:** Object Relational Mapping is employed for database interactions.
- **Testing:** Tests are implemented for the APIs to ensure functionality.
- **OpenAPI Specification:** The project adheres to OpenAPI specifications for API documentation.

## Docker Setup and Installation

1. **Clone the Repository:**

   git clone <git@github.com:farhadbaghban/CBR5-2050.git>

2. **Build Docker Images:**

   docker-compose build

3. **Run Docker Containers:**

   docker-compose up

4. **Access the Application:**
   The application will be accessible at `http://localhost:8000`.

## API Documentation

    API documentation is provided through the OpenAPI Specification. After running the server, visit `/swagger` or `/redoc` endpoint to view the API documentation in Swagger UI or ReDoc respectively.

## Testing

To run the tests:

    docker-compose
    docker exec  app  -it sh
    python manage.py test

## Contributing

Contributions are welcome. If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
