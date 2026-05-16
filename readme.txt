# Little Lemon Backend Capstone Project

Here are the API endpoints configured for this project:

## Static Content
- Homepage: http://127.0.0.1:8000/restaurant/

## Menu API (Generic Views)
- Menu List & Create (GET/POST): http://127.0.0.1:8000/restaurant/menu/
- Single Menu Item (GET/PUT/DELETE): http://127.0.0.1:8000/restaurant/menu/<id>

## Table Booking API (ViewSet & Router)
- Bookings List & Create (GET/POST): http://127.0.0.1:8000/restaurant/booking/tables/
- Note: This endpoint is secured with Token Authentication.

## User Authentication (Djoser & Token Auth)
- User Registration (POST): http://127.0.0.1:8000/auth/users/
- User Login/Token Generation (POST): http://127.0.0.1:8000/restaurant/api-token-auth/
- Alternative Djoser Token Login (POST): http://127.0.0.1:8000/auth/token/login/
