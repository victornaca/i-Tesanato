-- Inserts for a table customer
INSERT INTO customer (customer_id, customer_name, customer_email, customer_cpf, customer_cellphone, customer_password, customer_cep, customer_date_created, customer_date_modified)
VALUES
(4, 'Emily Johnson', 'emily.johnson@example.com', '45678901234', '456-789-0123', 'password123', '45678', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 'Michael Brown', 'michael.brown@example.com', '56789012345', '567-890-1234', 'password456', '56789', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(6, 'Sophia Davis', 'sophia.davis@example.com', '67890123456', '678-901-2345', 'password789', '67890', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(7, 'Matthew Wilson', 'matthew.wilson@example.com', '78901234567', '789-012-3456', 'passwordabc', '78901', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(8, 'Olivia Taylor', 'olivia.taylor@example.com', '89012345678', '890-123-4567', 'passworddef', '89012', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(9, 'Daniel Martinez', 'daniel.martinez@example.com', '90123456789', '901-234-5678', 'passwordghi', '90123', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(10, 'Ava Anderson', 'ava.anderson@example.com', '01234567890', '012-345-6789', 'passwordjkl', '01234', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(11, 'William Thomas', 'william.thomas@example.com', '12345678901', '123-456-7890', 'passwordmno', '12345', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(12, 'Emma Garcia', 'emma.garcia@example.com', '23456789012', '234-567-8901', 'passwordpqr', '23456', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(13, 'James Rodriguez', 'james.rodriguez@example.com', '34567890123', '345-678-9012', 'passwordstu', '34567', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(14, 'Isabella Lopez', 'isabella.lopez@example.com', '45678901234', '456-789-0123', 'passwordvwx', '45678', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(15, 'Sophia Hernandez', 'sophia.hernandez@example.com', '56789012345', '567-890-1234', 'passwordyz', '56789', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Inserts for a table product
INSERT INTO product (product_id, product_name, product_short_description, product_description, product_price_suggested, product_category, product_created, product_modified, customer_id)
VALUES
(4, 'Handcrafted Vase', 'Beautiful handcrafted vase', 'This exquisite vase is handcrafted by skilled artisans, adding elegance to any space.', 40.00, 'Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 4),
(5, 'Vintage Armchair', 'Elegant vintage armchair', 'Add a touch of vintage charm to your home with this beautifully upholstered armchair.', 150.00, 'Furniture', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 5),
(6, 'Artisanal Serving Tray', 'Unique artisanal serving tray', 'Serve your guests in style with this handcrafted serving tray, featuring intricate designs.', 25.00, 'Kitchen & Dining', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 6),
(7, 'Abstract Canvas Painting', 'Contemporary abstract canvas painting', 'Enhance your walls with this vibrant abstract canvas painting, perfect for modern interiors.', 80.00, 'Art', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 7),
(8, 'Handmade Throw Pillow', 'Cozy handmade throw pillow', 'Add comfort and style to your living room with this handcrafted throw pillow, featuring a unique pattern.', 20.00, 'Home Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 8),
(9, 'Rustic Wooden Shelf', 'Rustic wooden shelf', 'Display your favorite decor items with this rustic wooden shelf, crafted from reclaimed wood.', 45.00, 'Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 9),
(10, 'Vintage Desk Lamp', 'Vintage desk lamp', 'Illuminate your workspace with this vintage-inspired desk lamp, featuring an adjustable arm.', 30.00, 'Lighting', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 10),
(11, 'Handwoven Area Rug', 'Handwoven area rug', 'Add warmth and texture to your floors with this handwoven area rug, crafted from natural fibers.', 60.00, 'Home Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 11),
(12, 'Ceramic Plant Pot', 'Ceramic plant pot', 'Bring nature indoors with this elegant ceramic plant pot, perfect for housing your favorite houseplants.', 15.00, 'Garden', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 12),
(13, 'Minimalist Wall Clock', 'Minimalist wall clock', 'Keep track of time in style with this minimalist wall clock, featuring a sleek design.', 35.00, 'Home Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 13),
(14, 'Handmade Soap Set', 'Luxurious handmade soap set', 'Pamper yourself with this luxurious handmade soap set, featuring natural ingredients and soothing scents.', 25.00, 'Bath & Body', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 14),
(15, 'Industrial Bar Stool', 'Industrial bar stool', 'Add an industrial touch to your kitchen or bar area with this sturdy metal bar stool, featuring a vintage-inspired design.', 50.00, 'Furniture', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 15),
(16, 'Artisanal Cheese Board', 'Artisanal cheese board', 'Entertain in style with this artisanal cheese board, crafted from high-quality wood and featuring a built-in knife holder.', 40.00, 'Kitchen & Dining', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 4),
(17, 'Bohemian Wall Tapestry', 'Bohemian wall tapestry', 'Add a bohemian flair to your space with this colorful wall tapestry, featuring intricate patterns and fringe details.', 35.00, 'Home Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 5),
(18, 'Handblown Glass Vase', 'Handblown glass vase', 'Elevate your floral arrangements with this handblown glass vase, featuring a unique organic shape.', 55.00, 'Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 6),
(19, 'Scandinavian Throw Blanket', 'Scandinavian throw blanket', 'Stay cozy on chilly nights with this Scandinavian-inspired throw blanket, featuring a classic striped design.', 30.00, 'Home Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 7),
(20, 'Modern Wall Mirror', 'Modern wall mirror', 'Add depth and style to your space with this modern wall mirror, featuring a sleek frameless design.', 70.00, 'Home Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 8);

-- Inserts for a table stock
INSERT INTO stock (stock_id, stock_quantity, stock_date_created, stock_date_modified, product_id)
VALUES
(4, 15, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 4),
(5, 8, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 5),
(6, 12, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 6),
(7, 20, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 7),
(8, 25, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 8),
(9, 10, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 9),
(10, 18, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 10),
(11, 30, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 11),
(12, 22, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 12),
(13, 40, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 13),
(14, 15, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 14),
(15, 20, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 15),
(16, 10, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 16),
(17, 25, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 17),
(18, 20, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 18),
(19, 30, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 19),
(20, 15, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 20);

-- Inserts for a table store
INSERT INTO store (store_id, store_name, store_description, store_category, store_date_created, store_date_modified, customer_id)
VALUES
(1, 'Crafty Creations', 'Handmade jewelry and accessories', 'Fashion', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1),
(2, 'Rustic Elegance', 'Custom-made wooden furniture', 'Home Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 2),
(3, 'Artisanal Wonders', 'Unique artisanal kitchenware', 'Kitchen & Dining', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3),
(4, 'Eco-Friendly Finds', 'Sustainable home decor and accessories', 'Eco-Friendly', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 4),
(5, 'Boho Chic', 'Bohemian-inspired decor and accessories', 'Decor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 5);

-- Inserts for a table store_product
INSERT INTO store_product (store_product_id, store_id, product_id, store_product_price)
VALUES
(1, 1, 4, 40.00),   -- Crafty Creations: Handcrafted Vase
(2, 1, 5, 150.00),  -- Crafty Creations: Vintage Armchair
(3, 1, 6, 25.00),   -- Crafty Creations: Artisanal Serving Tray
(4, 1, 7, 80.00),   -- Crafty Creations: Abstract Canvas Painting
(5, 1, 8, 20.00),   -- Crafty Creations: Handmade Throw Pillow
(6, 1, 9, 45.00),   -- Crafty Creations: Rustic Wooden Shelf
(7, 1, 10, 30.00),  -- Crafty Creations: Vintage Desk Lamp
(8, 1, 11, 60.00),  -- Crafty Creations: Handwoven Area Rug
(9, 1, 12, 15.00),  -- Crafty Creations: Ceramic Plant Pot
(10, 1, 13, 35.00), -- Crafty Creations: Minimalist Wall Clock
(11, 1, 14, 25.00), -- Crafty Creations: Handmade Soap Set
(12, 1, 15, 50.00), -- Crafty Creations: Industrial Bar Stool
(13, 1, 16, 40.00), -- Crafty Creations: Artisanal Cheese Board
(14, 1, 17, 35.00), -- Crafty Creations: Bohemian Wall Tapestry
(15, 1, 18, 55.00), -- Crafty Creations: Handblown Glass Vase
(16, 1, 19, 30.00), -- Crafty Creations: Scandinavian Throw Blanket
(17, 1, 20, 70.00), -- Crafty Creations: Modern Wall Mirror
(18, 2, 4, 40.00),  -- Rustic Elegance: Handcrafted Vase
(19, 2, 5, 150.00), -- Rustic Elegance: Vintage Armchair
(20, 2, 6, 25.00),  -- Rustic Elegance: Artisanal Serving Tray
(21, 2, 7, 80.00),  -- Rustic Elegance: Abstract Canvas Painting
(22, 2, 8, 20.00),  -- Rustic Elegance: Handmade Throw Pillow
(23, 2, 9, 45.00),  -- Rustic Elegance: Rustic Wooden Shelf
(24, 2, 10, 30.00), -- Rustic Elegance: Vintage Desk Lamp
(25, 2, 11, 60.00), -- Rustic Elegance: Handwoven Area Rug
(26, 2, 12, 15.00), -- Rustic Elegance: Ceramic Plant Pot
(27, 2, 13, 35.00), -- Rustic Elegance: Minimalist Wall Clock
(28, 2, 14, 25.00), -- Rustic Elegance: Handmade Soap Set
(29, 2, 15, 50.00), -- Rustic Elegance: Industrial Bar Stool
(30, 2, 16, 40.00), -- Rustic Elegance: Artisanal Cheese Board
(31, 2, 17, 35.00), -- Rustic Elegance: Bohemian Wall Tapestry
(32, 2, 18, 55.00), -- Rustic Elegance: Handblown Glass Vase
(33, 2, 19, 30.00), -- Rustic Elegance: Scandinavian Throw Blanket
(34, 2, 20, 70.00), -- Rustic Elegance: Modern Wall Mirror
(35, 3, 4, 40.00),  -- Artisanal Wonders: Handcrafted Vase
(36, 3, 5, 150.00), -- Artisanal Wonders: Vintage Armchair
(37, 3, 6, 25.00),  -- Artisanal Wonders: Artisanal Serving Tray
(38, 3, 7, 80.00),  -- Artisanal Wonders: Abstract Canvas Painting
(39, 3, 8, 20.00),  -- Artisanal Wonders: Handmade Throw Pillow
(40, 3, 9, 45.00),  -- Artisanal Wonders: Rustic Wooden Shelf
(41, 3, 10, 30.00), -- Artisanal Wonders: Vintage Desk Lamp
(42, 3, 11, 60.00), -- Artisanal Wonders: Handwoven Area Rug
(43, 3, 12, 15.00), -- Artisanal Wonders: Ceramic Plant Pot
(44, 3, 13, 35.00), -- Artisanal Wonders: Minimalist Wall Clock
(45, 3, 14, 25.00), -- Artisanal Wonders: Handmade Soap Set
(46, 3, 15, 50.00), -- Artisanal Wonders: Industrial Bar Stool
(47, 3, 16, 40.00), -- Artisanal Wonders: Artisanal Cheese Board
(48, 3, 17, 35.00), -- Artisanal Wonders: Bohemian Wall Tapestry
(49, 3, 18, 55.00), -- Artisanal Wonders: Handblown Glass Vase
(50, 3, 19, 30.00), -- Artisanal Wonders: Scandinavian Throw Blanket
(51, 3, 20, 70.00), -- Artisanal Wonders: Modern Wall Mirror
(52, 4, 4, 40.00),  -- Eco-Friendly Finds: Handcrafted Vase
(53, 4, 5, 150.00), -- Eco-Friendly Finds: Vintage Armchair
(54, 4, 6, 25.00),  -- Eco-Friendly Finds: Artisanal Serving Tray
(55, 4, 7, 80.00),  -- Eco-Friendly Finds: Abstract Canvas Painting
(56, 4, 8, 20.00),  -- Eco-Friendly Finds: Handmade Throw Pillow
(57, 4, 9, 45.00),  -- Eco-Friendly Finds: Rustic Wooden Shelf
(58, 4, 10, 30.00), -- Eco-Friendly Finds: Vintage Desk Lamp
(59, 4, 11, 60.00), -- Eco-Friendly Finds: Handwoven Area Rug
(60, 4, 12, 15.00), -- Eco-Friendly Finds: Ceramic Plant Pot
(61, 4, 13, 35.00), -- Eco-Friendly Finds: Minimalist Wall Clock
(62, 4, 14, 25.00), -- Eco-Friendly Finds: Handmade Soap Set
(63, 4, 15, 50.00), -- Eco-Friendly Finds: Industrial Bar Stool
(64, 4, 16, 40.00), -- Eco-Friendly Finds: Artisanal Cheese Board
(65, 4, 17, 35.00), -- Eco-Friendly Finds: Bohemian Wall Tapestry
(66, 4, 18, 55.00), -- Eco-Friendly Finds: Handblown Glass Vase
(67, 4, 19, 30.00), -- Eco-Friendly Finds: Scandinavian Throw Blanket
(68, 4, 20, 70.00), -- Eco-Friendly Finds: Modern Wall Mirror
(69, 5, 4, 40.00),  -- Boho Chic: Handcrafted Vase
(70, 5, 5, 150.00), -- Boho Chic: Vintage Armchair
(71, 5, 6, 25.00),  -- Boho Chic: Artisanal Serving Tray
(72, 5, 7, 80.00),  -- Boho Chic: Abstract Canvas Painting
(73, 5, 8, 20.00),  -- Boho Chic: Handmade Throw Pillow
(74, 5, 9, 45.00),  -- Boho Chic: Rustic Wooden Shelf
(75, 5, 10, 30.00), -- Boho Chic: Vintage Desk Lamp
(76, 5, 11, 60.00), -- Boho Chic: Handwoven Area Rug
(77, 5, 12, 15.00), -- Boho Chic: Ceramic Plant Pot
(78, 5, 13, 35.00), -- Boho Chic: Minimalist Wall Clock
(79, 5, 14, 25.00), -- Boho Chic: Handmade Soap Set
(80, 5, 15, 50.00), -- Boho Chic: Industrial Bar Stool
(81, 5, 16, 40.00), -- Boho Chic: Artisanal Cheese Board
(82, 5, 17, 35.00), -- Boho Chic: Bohemian Wall Tapestry
(83, 5, 18, 55.00), -- Boho Chic: Handblown Glass Vase
(84, 5, 19, 30.00), -- Boho Chic: Scandinavian Throw Blanket
(85, 5, 20, 70.00); -- Boho Chic: Modern Wall Mirror


-- Inserts for a table order
INSERT INTO "order" (order_id, order_date, order_quantity, customer_id, store_store_product_id)
VALUES
(1, '2024-04-01', 1, 4, 1),
(2, '2024-04-01', 2, 5, 2),
(3, '2024-04-01', 3, 6, 3),
(4, '2024-04-02', 1, 7, 4),
(5, '2024-04-02', 2, 8, 5),
(6, '2024-04-02', 3, 9, 6),
(7, '2024-04-03', 1, 10, 7),
(8, '2024-04-03', 2, 11, 8),
(9, '2024-04-03', 3, 12, 9),
(10, '2024-04-04', 1, 13, 10),
(11, '2024-04-04', 2, 14, 11),
(12, '2024-04-04', 3, 15, 12),
(13, '2024-04-05', 1, 4, 13),
(14, '2024-04-05', 2, 5, 14),
(15, '2024-04-05', 3, 6, 15),
(16, '2024-04-06', 1, 7, 16),
(17, '2024-04-06', 2, 8, 17),
(18, '2024-04-06', 3, 9, 18),
(19, '2024-04-07', 1, 10, 19),
(20, '2024-04-07', 2, 11, 20),
(21, '2024-04-07', 3, 12, 21),
(22, '2024-04-08', 1, 13, 22),
(23, '2024-04-08', 2, 14, 23),
(24, '2024-04-08', 3, 15, 24),
(25, '2024-04-09', 1, 4, 25),
(26, '2024-04-09', 2, 5, 26),
(27, '2024-04-09', 3, 6, 27),
(28, '2024-04-10', 1, 7, 28),
(29, '2024-04-10', 2, 8, 29),
(30, '2024-04-10', 3, 9, 30),
(31, '2024-04-11', 1, 10, 31),
(32, '2024-04-11', 2, 11, 32),
(33, '2024-04-11', 3, 12, 33),
(34, '2024-04-12', 1, 13, 34),
(35, '2024-04-12', 2, 14, 35),
(36, '2024-04-12', 3, 15, 36),
(37, '2024-04-13', 1, 4, 37),
(38, '2024-04-13', 2, 5, 38),
(39, '2024-04-13', 3, 6, 39),
(40, '2024-04-14', 1, 7, 40),
(41, '2024-04-14', 2, 8, 41),
(42, '2024-04-14', 3, 9, 42),
(43, '2024-04-15', 1, 10, 43),
(44, '2024-04-15', 2, 11, 44),
(45, '2024-04-15', 3, 12, 45),
(46, '2024-04-16', 1, 13, 46),
(47, '2024-04-16', 2, 14, 47),
(48, '2024-04-16', 3, 15, 48),
(49, '2024-04-17', 1, 4, 49),
(50, '2024-04-17', 2, 5, 50),
(51, '2024-04-17', 3, 6, 51),
(52, '2024-04-18', 1, 7, 52),
(53, '2024-04-18', 2, 8, 53),
(54, '2024-04-18', 3, 9, 54),
(55, '2024-04-19', 1, 10, 55),
(56, '2024-04-19', 2, 11, 56),
(57, '2024-04-19', 3, 12, 57),
(58, '2024-04-20', 1, 13, 58),
(59, '2024-04-20', 2, 14, 59),
(60, '2024-04-20', 3, 15, 60),
(61, '2024-04-21', 1, 4, 61),
(62, '2024-04-21', 2, 5, 62),
(63, '2024-04-21', 3, 6, 63),
(64, '2024-04-22', 1, 7, 64),
(65, '2024-04-22', 2, 8, 65),
(66, '2024-04-22', 3, 9, 66),
(67, '2024-04-23', 1, 10, 67),
(68, '2024-04-23', 2, 11, 68),
(69, '2024-04-23', 3, 12, 69),
(70, '2024-04-24', 1, 13, 70),
(71, '2024-04-24', 2, 14, 71),
(72, '2024-04-24', 3, 15, 72),
(73, '2024-04-25', 1, 4, 73),
(74, '2024-04-25', 2, 5, 74),
(75, '2024-04-25', 3, 6, 75),
(76, '2024-04-26', 1, 7, 76),
(77, '2024-04-26', 2, 8, 77),
(78, '2024-04-26', 3, 9, 78),
(79, '2024-04-27', 1, 10, 79),
(80, '2024-04-27', 2, 11, 80),
(81, '2024-04-27', 3, 12, 81),
(82, '2024-04-28', 1, 13, 82),
(83, '2024-04-28', 2, 14, 83),
(84, '2024-04-28', 3, 15, 84),
(85, '2024-04-29', 1, 4, 85),
(86, '2024-04-29', 1, 8, 1),
(87, '2024-04-29', 2, 10, 2),
(88, '2024-04-30', 3, 6, 3),
(89, '2024-04-30', 4, 9, 4),
(90, '2024-04-30', 5, 5, 5),
(91, '2024-04-01', 2, 4, 6),
(92, '2024-04-01', 3, 5, 7),
(93, '2024-04-01', 1, 6, 8),
(94, '2024-04-02', 2, 7, 9),
(95, '2024-04-02', 3, 8, 10),
(96, '2024-04-02', 1, 9, 11),
(97, '2024-04-03', 2, 10, 12),
(98, '2024-04-03', 3, 11, 13),
(99, '2024-04-03', 1, 12, 14),
(100, '2024-04-04', 2, 13, 15),
(101, '2024-04-04', 3, 14, 16),
(102, '2024-04-04', 1, 15, 17),
(103, '2024-04-05', 2, 4, 18),
(104, '2024-04-05', 3, 5, 19),
(105, '2024-04-05', 1, 6, 20),
(106, '2024-04-06', 2, 7, 21),
(107, '2024-04-06', 3, 8, 22),
(108, '2024-04-06', 1, 9, 23),
(109, '2024-04-07', 2, 10, 24),
(110, '2024-04-07', 3, 11, 25),
(111, '2024-04-07', 1, 12, 26),
(112, '2024-04-08', 2, 13, 27),
(113, '2024-04-08', 3, 14, 28),
(114, '2024-04-08', 1, 15, 29),
(115, '2024-04-09', 2, 4, 30),
(116, '2024-04-09', 3, 5, 31),
(117, '2024-04-09', 1, 6, 32),
(118, '2024-04-10', 2, 7, 33),
(119, '2024-04-10', 3, 8, 34),
(120, '2024-04-10', 1, 9, 35),
(121, '2024-04-11', 2, 10, 36),
(122, '2024-04-11', 3, 11, 37),
(123, '2024-04-11', 1, 12, 38),
(124, '2024-04-12', 2, 13, 39),
(125, '2024-04-12', 3, 14, 40),
(126, '2024-04-12', 1, 15, 41),
(127, '2024-04-13', 2, 4, 42),
(128, '2024-04-13', 3, 5, 43),
(129, '2024-04-13', 1, 6, 44),
(130, '2024-04-14', 2, 7, 45),
(131, '2024-04-14', 3, 8, 46),
(132, '2024-04-14', 1, 9, 47),
(133, '2024-04-15', 2, 10, 48),
(134, '2024-04-15', 3, 11, 49),
(135, '2024-04-15', 1, 12, 50),
(136, '2024-04-16', 2, 13, 51),
(137, '2024-04-16', 3, 14, 52),
(138, '2024-04-16', 1, 15, 53),
(139, '2024-04-17', 2, 4, 54),
(140, '2024-04-17', 3, 5, 55),
(141, '2024-04-17', 1, 6, 56),
(142, '2024-04-18', 2, 7, 57),
(143, '2024-04-18', 3, 8, 58),
(144, '2024-04-18', 1, 9, 59),
(145, '2024-04-19', 2, 10, 60),
(146, '2024-04-19', 3, 11, 61),
(147, '2024-04-19', 1, 12, 62),
(148, '2024-04-20', 2, 13, 63),
(149, '2024-04-20', 3, 14, 64),
(150, '2024-04-20', 1, 15, 65),
(151, '2024-04-21', 2, 4, 66),
(152, '2024-04-21', 3, 5, 67),
(153, '2024-04-21', 1, 6, 68),
(154, '2024-04-22', 2, 7, 69),
(155, '2024-04-22', 3, 8, 70),
(156, '2024-04-22', 1, 9, 71),
(157, '2024-04-23', 2, 10, 72),
(158, '2024-04-23', 3, 11, 73),
(159, '2024-04-23', 1, 12, 74),
(160, '2024-04-24', 2, 13, 75),
(161, '2024-04-24', 3, 14, 76),
(162, '2024-04-24', 1, 15, 77),
(163, '2024-04-25', 2, 4, 78),
(164, '2024-04-25', 3, 5, 79),
(165, '2024-04-25', 1, 6, 80),
(166, '2024-04-26', 2, 7, 81),
(167, '2024-04-26', 3, 8, 82),
(168, '2024-04-26', 1, 9, 83),
(169, '2024-04-27', 2, 10, 84),
(170, '2024-04-27', 3, 11, 85),
(171, '2024-04-27', 1, 12, 1),
(172, '2024-04-28', 2, 13, 2),
(173, '2024-04-28', 3, 14, 3),
(174, '2024-04-28', 1, 15, 4),
(175, '2024-04-29', 2, 4, 20),
(176, '2024-04-29', 3, 5, 31),
(177, '2024-04-29', 1, 6, 56),
(178, '2024-04-30', 2, 7, 16),
(179, '2024-04-30', 3, 8, 76),
(180, '2024-04-30', 1, 9, 32),
(181, '2024-04-01', 2, 10, 15),
(182, '2024-04-01', 3, 11, 21),
(183, '2024-04-01', 1, 12, 67),
(184, '2024-04-02', 2, 13, 62),
(185, '2024-04-02', 3, 14, 45),
(186, '2024-04-02', 1, 15, 40),
(187, '2024-04-03', 2, 4, 30),
(188, '2024-04-03', 3, 5, 25),
(189, '2024-04-03', 1, 6, 70),
(190, '2024-04-04', 2, 7, 80),
(191, '2024-04-04', 3, 8, 82),
(192, '2024-04-04', 1, 9, 84),
(193, '2024-04-05', 2, 10, 8),
(194, '2024-04-05', 3, 11, 12),
(195, '2024-04-05', 1, 12, 17),
(196, '2024-04-06', 2, 13, 26),
(197, '2024-04-06', 3, 14, 42),
(198, '2024-04-06', 1, 15, 34),
(199, '2024-04-07', 2, 4, 67),
(200, '2024-04-07', 3, 5, 75);

