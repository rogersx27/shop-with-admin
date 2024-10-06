CREATE TABLE
    categories (
        id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );

CREATE TABLE
    customers (
        id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        address VARCHAR(255),
        phone VARCHAR(50)
    );

CREATE TABLE
    products (
        id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        category_id CHAR(36) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        description TEXT,
        image_url VARCHAR(255),
        quantity VARCHAR(50),
        availability BOOLEAN DEFAULT TRUE,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    );

CREATE TABLE
    orders (
        id CHAR(36) PRIMARY KEY,
        customer_id CHAR(36) NOT NULL,
        order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        status VARCHAR(50) NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    );

CREATE TABLE
    order_items (
        id CHAR(36) PRIMARY KEY,
        order_id CHAR(36) NOT NULL,
        product_id CHAR(36) NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (product_id) REFERENCES products (id)
    );