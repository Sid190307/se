
Part 1: Steps for Diagram 1 (Example 1)

1. Initialize the Project: Open StarUML, select Model > Add Diagram > ER Diagram from the top menu to create a blank database workspace.
2. Place the Entities: Select the Entity tool from the left Toolbox and place 8 entities onto the canvas: CUSTOMER, ITEM, COMPANY, ORDER, SHOPPING CART, SHIPPING, CREDIT CARD, and E-COMMERCE.
3. Insert Columns (Attributes): Right-click each entity, select Add > Column, and type the attributes shown in the ovals:
	• CUSTOMER: Name, Address, E-mail
	• ITEM: Name, Price
	• COMPANY: Name
	• ORDER: Order Number
4. Connect with Relationships: Select the Relationship tool from the Toolbox, click and drag lines between the matching entities, and double-click the lines to label them (ORDERS, CONTAINS, PRODUCES, SHIPS ITEM, etc.).
5. Adjust Cardinality: Click on each relationship line, go to the right-hand Properties panel, and configure End1.Multiplicity and End2.Multiplicity to add the correct lines and crow's foot notations (e.g., 1, 0..*, 1..*).






Part 2: Steps for Diagram 2 (Online Bookstore System)

1. Create a New Diagram Canvas: Go to Model > Add Diagram > ER Diagram to open a fresh, second canvas tab.
2. Place the 7 Core Entities: Use the Entity tool to place the 7 core blocks for the bookstore: USER, BOOK, CATEGORY, AUTHOR, CART, CART ITEM, and ORDER ITEM.
3. Add Complete Keys & Attributes: Right-click each entity and use Add > Column to fill in their primary keys and fields:
	• USER: User ID (PK), Email, Password, Name, Address, Phone
	• BOOK: Book ID (PK), Title, Price, Stock Count, ISBN, Author ID, Category ID
	• CATEGORY: Category ID (PK), Category Name
	• AUTHOR: Author ID (PK), Name, Bio
	• CART: Cart ID (PK), User ID
	• CART ITEM: Cart Item ID (PK), Cart ID, Book ID, Quantity
	• ORDER ITEM: Order Item ID (PK), Order ID, Book ID, Quantity, Subtotal
4. Add Order & Payment Entities: Place the final two entities, ORDER and PAYMENT, adding their columns:
	• ORDER: Order ID (PK), User ID, Order Date, Total Amount, Status
	• PAYMENT: Payment ID (PK), Order ID, Payment Date, Amount, Payment Mode
5. Establish Relationships & Multiplicities: Drag Relationship lines between connected entities (e.g., USER to CART, BOOK to CART ITEM). In the Properties panel, set the multiplicities (like 1-to-many or 1-to-1) to display the crow's foot markers exactly as shown in the layout.
