-- Tabela: customer
CREATE TABLE customer (
    customer_id int NOT NULL,
    customer_name varchar(200) NOT NULL,
    customer_email varchar(200) NOT NULL,
    customer_cpf varchar(11) NOT NULL,
    customer_cellphone varchar(12) NOT NULL,
    customer_password varchar(256) NOT NULL,
    customer_cep varchar(8) NOT NULL,
    customer_date_created timestamp NOT NULL,
    customer_date_modified timestamp NOT NULL,
    CONSTRAINT pk_customer_id PRIMARY KEY (customer_id)
);


-- Tabela: store
CREATE TABLE store (
    store_id int NOT NULL,
    store_name varchar(200) NOT NULL,
    store_description varchar(1000) NULL,
    store_category varchar(200) NOT NULL,
    store_date_created timestamp NOT NULL,
    store_date_modified timestamp NOT NULL,
    customer_id int NOT NULL,
    CONSTRAINT pk_store_id PRIMARY KEY (store_id),
    CONSTRAINT fk_store_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

-- Tabela: product
CREATE TABLE product (
    product_id int NOT NULL,
    product_name varchar(200) NOT NULL,
    product_short_description varchar(1000) NOT NULL,
    product_description text NULL,
    product_price_suggested decimal(10,2) NOT NULL,
    product_category varchar(200) NOT NULL,
    product_created timestamp NOT NULL,
    product_modified timestamp NOT NULL,
    customer_id int NOT NULL,
    CONSTRAINT pk_product_id PRIMARY KEY (product_id),
    CONSTRAINT fk_product_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

-- Tabela: stock
CREATE TABLE stock (
    stock_id int NOT NULL,
    stock_quantity decimal(10,2) NOT NULL,
    stock_date_created timestamp NOT NULL,
    stock_date_modified timestamp NOT NULL,
    product_id int NOT NULL,
    CONSTRAINT pk_stock_id PRIMARY KEY (stock_id),
    CONSTRAINT fk_stock_product FOREIGN KEY (product_id) REFERENCES product (product_id)
);

-- Tabela: store_product
CREATE TABLE store_product (
    store_product_id int NOT NULL,
    store_id int NOT NULL,
    product_id int NOT NULL,
    store_product_price decimal(10,2) NOT NULL,
    CONSTRAINT uk_store_product UNIQUE (store_id, product_id),
    CONSTRAINT pk_store_product_id PRIMARY KEY (store_product_id),
    CONSTRAINT fk_store_product_store FOREIGN KEY (store_id) REFERENCES store (store_id),
    CONSTRAINT fk_store_product_product FOREIGN KEY (product_id) REFERENCES product (product_id)
);

-- Tabela: "order"
CREATE TABLE order_product (
    order_id int NOT NULL,
    order_date timestamp NOT NULL,
    order_quantity int NOT NULL,
    customer_id int NOT NULL,
    store_store_product_id int NOT NULL,
    CONSTRAINT pk_order_id PRIMARY KEY (order_id),
    CONSTRAINT fk_order_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
    CONSTRAINT fk_order_store_product FOREIGN KEY (store_store_product_id) REFERENCES store_product (store_product_id)
);
