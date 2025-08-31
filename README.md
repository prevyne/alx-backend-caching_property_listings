# Django Property Listings with Multi-Level Caching
This project is a Django-based property listing application that demonstrates various caching strategies to optimize performance and reduce database load. It uses Docker to containerize a PostgreSQL database for data persistence and a Redis server for caching, creating a robust and scalable development environment.

The application implements caching at multiple levels:

View-Level Caching: Caching the entire HTTP response of the property list view.

Low-Level Queryset Caching: Caching the database query result for all properties.

Cache Invalidation: Using Django signals to automatically clear the cache when property data changes, ensuring data consistency.

Learning Objectives
Implement multi-level caching strategies (view-level and low-level) in a Django application.

Configure and integrate Redis as a high-performance cache backend.

Set up and manage containerized services (PostgreSQL, Redis) using Docker and Docker Compose.

Understand and implement cache invalidation techniques using Django signals to maintain data integrity.

Analyze cache performance by retrieving and interpreting Redis metrics like hit/miss ratios.

Develop efficient database query patterns that leverage caching to minimize database load.

Tools and Libraries
Framework: Django

Database: PostgreSQL

Cache: Redis

Containerization: Docker

Python Packages:

django-redis: Provides a Redis cache backend for Django.

psycopg2-binary: PostgreSQL adapter for Python.

⚙️ Project Setup and Installation
Follow these steps to set up and run the project locally.

Prerequisites
Docker

Docker Compose

Installation Steps
Clone the Repository:

Bash

git clone https://github.com/your-username/alx-backend-caching_property_listings.git
cd alx-backend-caching_property_listings
Build and Run Docker Containers:
This command will build the Django application image (if you have a Dockerfile for it) and start the PostgreSQL and Redis services defined in docker-compose.yml.

Bash

docker-compose up --build -d
The -d flag runs the containers in detached mode.

Run Database Migrations:
Apply the database schema from your models to the PostgreSQL database.

Bash

docker-compose exec web python manage.py makemigrations properties
docker-compose exec web python manage.py migrate
(Note: The command assumes your Django service is named web in docker-compose.yml)

🚀 How to Run and Test
Running the Application
Once the containers are running and migrations are applied, the Django development server will be available at:

URL: http://localhost:8000/properties/

Testing the Cache
First Request (Cache Miss):
Access http://localhost:8000/properties/. Check the logs of your Django container (docker-compose logs web). You should see a message indicating a cache miss and that data was fetched from the database.

Second Request (Cache Hit):
Refresh the page. Check the logs again. This time, you should see a message for a cache hit, indicating that the data was served from Redis.

Test Cache Invalidation:

Access the Django admin shell:

Bash

docker-compose exec web python manage.py shell
Create a new property in the shell:

Python

from properties.models import Property
Property.objects.create(title='New Beach House', description='A lovely house by the sea.', price=500000.00, location='Malindi')
exit()
Check the logs. You will see a message confirming that the cache was invalidated due to the model change.

Refresh http://localhost:8000/properties/. The logs will show a cache miss again as the application fetches the updated list, and the new property will be displayed.

Checking Cache Metrics
You can add a view or management command to call the get_redis_cache_metrics() function from properties/utils.py to see the current hit/miss ratio.