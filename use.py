
Part 1: Steps for Diagram 1 (Food Management System)

1. Initialize the Diagram: Open StarUML, select Model > Add Diagram > Use Case Diagram from the top menu.
2. Place the Actors: Choose the Actor tool from the left Toolbox and place 4 stick figures onto the canvas: Waiter, Client, Cashier, and Chef.
3. Create Core Use Cases: Use the Use Case tool (oval shape) to draw the primary system functions: Order Food, Serve Food, Eat Food, and Pay For Food.
4. Create Conditional Use Cases: Draw the remaining wine-specific ovals to the right of the food ovals: Order Wine, Serve Wine, Drink Wine, and Pay for Wine.
5. Draw Associations: Select the standard Association tool to connect the actors to their respective core use cases (e.g., connect Client to Order Food, Eat Food, and Pay For Food). Double-click a line to type text labels like +place order or +pay.
6. Apply Extend Relationships: Select the Extend tool (dashed arrow). Click on each Wine use case and drag the arrow pointing back to its corresponding Food use case (e.g., from Order Wine \(\rightarrow \) Order Food) so the <<extend>> label appears automatically.


Part 2: Steps for Diagram 2 (Library Management System)

1. Open a New Use Case Workspace: Navigate to Model > Add Diagram > Use Case Diagram to clear the canvas for your second system layout.
2. Place the 3 Main Actors: Select the Actor tool to place Student on the left, Librarian at the bottom, and Admin on the right side of the canvas.
3. Draw the Use Case Ovals: Use the Use Case tool to map out all 11 action blocks across the canvas as shown in the layout (e.g., Register, Authentication, Book Issue, Return Book, Manage Members, etc.).
4. Connect Actors to Actions: Use the Association line tool to link actors to their permissible paths (e.g., Admin to Manage Members and Librarian Accounts). Double-click to insert pathway directions like +Borrow Book or +checks whether student has returned book.
5. Add Include Dependency: Select the Include tool from the Toolbox. Click on Book Issue and drag it pointing to Authentication to attach the required <<include>> dependency line.
6. Add Extend Dependencies & Constraints: Select the Extend tool and drag the dashed arrows between the dependent nodes:
	• From Book Issue \(\rightarrow \) Search Book
	• From Check Due Date \(\rightarrow \) Return Book
	• From Pay Fine \(\rightarrow \) Check Due Date
	• Optional: Click the Text tool in the annotation toolbox to type the conditional text if due date exceeded right underneath the fine extension arrow.
