CREATE TABLE
    categories (
        id CHAR(36) PRIMARY KEY NOT NULL DEFAULT 'UUID()',
        name VARCHAR(255) NOT NULL UNIQUE
    );

CREATE TABLE
    customers (
        id CHAR(36) PRIMARY KEY NOT NULL DEFAULT 'UUID()',
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        address VARCHAR(255),
        phone VARCHAR(50)
    );

CREATE TABLE
    products (
        id CHAR(36) PRIMARY KEY NOT NULL DEFAULT 'UUID()',
        generic_name VARCHAR(255) NOT NULL,
        category_id CHAR(36) NOT NULL,
        description TEXT,
        image_url VARCHAR(255),
        availability BOOLEAN DEFAULT TRUE,
        is_best_seller BOOLEAN DEFAULT FALSE,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    );

CREATE TABLE
    product_details (
        id CHAR(36) PRIMARY KEY NOT NULL DEFAULT 'UUID()',
        product_id CHAR(36) NOT NULL,
        brand_name VARCHAR(255) NOT NULL,
        strength VARCHAR(50) NOT NULL,
        composition TEXT,
        supply_type VARCHAR(50) NOT NULL,
        manufacturer VARCHAR(255) NOT NULL,
        other_brand_names TEXT,
        price DECIMAL(10, 2) NOT NULL,
        stock INT NOT NULL,
        packaging TEXT DEFAULT NULL,
        quantity_per_pack TEXT DEFAULT NULL,
        FOREIGN KEY (product_id) REFERENCES products (id)
    );

CREATE TABLE
    orders (
        id CHAR(36) PRIMARY KEY NOT NULL DEFAULT 'UUID()',
        customer_id CHAR(36) NOT NULL,
        order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        status VARCHAR(50) NOT NULL,
        total_amount DECIMAL(10, 2) DEFAULT 0,
        payment_status VARCHAR(50),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    );

CREATE TABLE
    order_items (
        id CHAR(36) PRIMARY KEY NOT NULL DEFAULT 'UUID()',
        order_id CHAR(36) NOT NULL,
        product_id CHAR(36) NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (product_id) REFERENCES products (id)
    );