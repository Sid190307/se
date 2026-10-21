
Part 1: Steps for Diagram 1 (ATM Machine System)

1. Initialize the Diagram: Open StarUML, select Model > Add Diagram > Statechart Diagram from the top menu.
2. Add Initial and Final Nodes: Place an Initial State (black dot) on the left and a Final State (bullseye) in the center-top area.
3. Place the Core States: Use the State tool to add the primary states: Idle, Account Activity, Dispense Money, and Print Receipt.
4. Create a Composite State: Use the Submachine State or regular State tool to draw a large bounding box at the bottom. Name it Verify Account.
5. Add Inner Sub-states: Inside the Verify Account container, add five sub-states: Verify Card, Card Valid, VerifyPin, PinCorrect, and PinIncorrect.
6. Insert Internal State Actions: Right-click Verify Card and VerifyPin, select Add > Do Activity, and type out the operations (e.g., do/CardSubmitted, do/ReadCard, do/returnCard).
7. Add Choice Diamonds: Use the Choice tool (diamond shape) to place condition nodes inside the container (Card Valid and Pin Valid).
8. Connect Transition Flows: Use the Transition tool to route arrow lines connecting all states and choice elements according to the flow, adding conditional guard text like [tries < maxtries] / tries+++ where required.


Part 2: Steps for Diagram 2 (Smart E-Commerce Order Fulfillment System)

1. Open a Fresh Diagram Tab: Go to Model > Add Diagram > Statechart Diagram to open a clean canvas.
2. Setup Start/End Points: Drop an Initial State at the top center and a Final State at the very bottom center.
3. Map Out Linear Operational States: Select the State tool and place the primary chronological states vertically down the page: Checkout, Payment Processing, Inventory Check, Packing, Shipping, and Out for Delivery.
4. Map Out Terminal Exception States: Place the side-branch states to manage alternate paths:
	• Near payment: Failed
	• Near inventory: Out of Stock and Order Cancelled
	• Near delivery: Delivered, Cancelled, and Return Refund
5. Insert Decision Nodes: Select the Choice tool (diamond shape) and insert three logic junctions down the main path: Payment ?, Stock ?, and Delivery ?.
6. Connect System Logic Transitions: Select the Transition line tool to link all elements sequentially. Double-click the branching arrows leaving the choice diamonds to label their outcomes (Success, Failed, Available, Out of Stock, Delivered).
7. Route to Final Node: Drag terminating transition lines from Failed, Order Cancelled, Delivered, and Return Refund directly into the bottom Final State circle to close out all possible lifecycle endpoints.
