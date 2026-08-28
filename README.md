# 🌸 Bloomora Backend

Backend API for **Bloomora**, a florist management platform designed to
manage products, inventory, orders, customers, and day-to-day flower
shop operations.

The backend is built with **FastAPI**, **SQLAlchemy**, and **MySQL**,
with **JWT** for authentication and **LangChain** for future AI-powered
features.

------------------------------------------------------------------------

## 🛠 Tech Stack

  Technology       Purpose
  ---------------- ----------------------------------
  **Python**       Backend programming language
  **FastAPI**      REST API framework
  **SQLAlchemy**   ORM and database interaction
  **MySQL**        Relational database
  **JWT**          Authentication and authorization
  **LangChain**    AI / LLM integration

------------------------------------------------------------------------

## ✨ Features

### Product Management

-   Create products
-   View products
-   Update product information
-   Delete products
-   Manage product categories
-   Track product availability

### Inventory Management

-   Track flower inventory
-   Update stock quantities
-   Configure low-stock thresholds
-   Monitor low-stock products

### Order Management

-   Create and manage orders
-   Update order status
-   View order history
-   Track order details

### Customer Management

-   Store customer information
-   View customer order history
-   Manage customer profiles

### Authentication & Authorization

-   User authentication
-   JWT-based authentication
-   Protected API endpoints
-   Role-based authorization

### AI Integration

LangChain may be used for AI-powered features such as:

-   Bouquet recommendations
-   Inventory insights
-   Product description generation
-   Sales summaries
-   Natural-language queries
-   Florist assistant features

------------------------------------------------------------------------

## 📁 Project Structure

``` text
backend/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── auth.py
│   │   ├── products.py
│   │   ├── categories.py
│   │   ├── inventory.py
│   │   ├── orders.py
│   │   └── customers.py
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── category.py
│   │   ├── inventory.py
│   │   └── order.py
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── product.py
│   │   ├── category.py
│   │   └── order.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── product_service.py
│   │   └── ai_service.py
│   └── core/
│       ├── config.py
│       ├── security.py
│       └── database.py
├── requirements.txt
├── .env
└── README.md
```

------------------------------------------------------------------------

## 🔌 API Endpoints

### Products

``` http
GET     /api/products
GET     /api/products/{id}
POST    /api/products
PATCH   /api/products/{id}
DELETE  /api/products/{id}
```

### Authentication

``` http
POST    /api/auth/register
POST    /api/auth/login
GET     /api/auth/me
```

### Inventory

``` http
GET     /api/inventory
GET     /api/inventory/{id}
PATCH   /api/inventory/{id}
```

### Orders

``` http
GET     /api/orders
GET     /api/orders/{id}
POST    /api/orders
PATCH   /api/orders/{id}
DELETE  /api/orders/{id}
```

------------------------------------------------------------------------

## 🗄 Product Model

  Field                   Type        Description
  ----------------------- ----------- ----------------------------------
  `id`                    BIGINT      Primary key
  `name`                  VARCHAR     Product name
  `sku`                   VARCHAR     Unique SKU
  `description`           TEXT        Product description
  `category_id`           BIGINT      Product category
  `price`                 DECIMAL     Selling price
  `cost_price`            DECIMAL     Cost price
  `stock_quantity`        INT         Current inventory
  `low_stock_threshold`   INT         Low-stock warning threshold
  `unit`                  VARCHAR     Unit such as `stem` or `bouquet`
  `image_url`             VARCHAR     Product image
  `is_active`             BOOLEAN     Product availability
  `created_at`            TIMESTAMP   Creation timestamp
  `updated_at`            TIMESTAMP   Last update timestamp

Example:

``` json
{
  "id": 1,
  "name": "Red Rose",
  "sku": "ROSE-RED-001",
  "description": "Premium red rose",
  "category_id": 1,
  "price": 6.99,
  "cost_price": 2.50,
  "stock_quantity": 120,
  "low_stock_threshold": 20,
  "unit": "stem",
  "image_url": "/images/red-rose.jpg",
  "is_active": true
}
```

------------------------------------------------------------------------

## 🔐 Authentication

Bloomora uses **JSON Web Tokens (JWT)** for authentication.

``` text
User Login
    ↓
Validate Credentials
    ↓
Generate JWT
    ↓
Return Token
    ↓
Client sends token
    ↓
FastAPI validates JWT
    ↓
Protected Resource
```

------------------------------------------------------------------------

## 🗃 Database

Bloomora uses **MySQL** as its relational database and **SQLAlchemy** as
its ORM.

``` text
FastAPI
   ↓
Service Layer
   ↓
SQLAlchemy
   ↓
MySQL
```

------------------------------------------------------------------------

## 🤖 AI Integration

LangChain will be introduced separately from the core business logic.

Potential features include:

-   Inventory insights
-   Bouquet recommendations
-   Product description generation
-   Sales summaries
-   Natural-language business queries

The core application will not depend on LLM availability.

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Create a Virtual Environment

``` bash
python -m venv venv
```

macOS / Linux:

``` bash
source venv/bin/activate
```

Windows:

``` bash
venv\Scripts\activate
```

### 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

``` env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/bloomora
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
OPENAI_API_KEY=your-api-key
```

> **Important:** Never commit the `.env` file to version control.

### 4. Start the Development Server

``` bash
uvicorn main:app --reload
```

FastAPI Swagger documentation is available at `/docs`, and ReDoc at
`/redoc`.

------------------------------------------------------------------------

## 🗺 Roadmap

### Phase 1 --- Core Product System

-   [ ] FastAPI project setup
-   [ ] MySQL database connection
-   [ ] SQLAlchemy configuration
-   [ ] Product model
-   [ ] Product CRUD API
-   [ ] Product validation

### Phase 2 --- Authentication

-   [ ] User model
-   [ ] User registration
-   [ ] User login
-   [ ] Password hashing
-   [ ] JWT authentication
-   [ ] Protected endpoints
-   [ ] Role-based authorization

### Phase 3 --- Business Operations

-   [ ] Categories
-   [ ] Inventory
-   [ ] Customers
-   [ ] Orders
-   [ ] Order status management
-   [ ] Low-stock tracking

### Phase 4 --- Dashboard & Analytics

-   [ ] Sales analytics
-   [ ] Inventory analytics
-   [ ] Revenue reporting
-   [ ] Low-stock alerts
-   [ ] Dashboard API

### Phase 5 --- AI Features

-   [ ] LangChain integration
-   [ ] AI florist assistant
-   [ ] Inventory insights
-   [ ] Bouquet recommendations
-   [ ] Natural-language business queries

------------------------------------------------------------------------

## 🎯 Project Goals

Bloomora is designed to go beyond a basic CRUD application and
demonstrate a production-oriented backend architecture.

The project focuses on:

-   Clean REST API design
-   Relational database modeling
-   Authentication and authorization
-   Maintainable business logic
-   Inventory and order workflows
-   Business analytics
-   AI integration
-   Scalable backend architecture
