
Part 1: Steps for Diagram 1 (Login System)

1. Initialize the Diagram: Open StarUML, select Model > Add Diagram > Activity Diagram from the top menu.
2. Create Swimlanes (Partitions): Select the Swimlane (Vertical) tool from the Toolbox. Draw two columns on your canvas. Double-click their headers to rename them ADMIN and SYSTEM.
3. Add Initial and Final Nodes: Place an Initial Node (solid black circle) at the top of the ADMIN column and a Final Node (bullseye circle) at the bottom.
4. Place Activity Actions: Select the Action tool (rounded rectangle) and place the blocks into their respective columns:
	• ADMIN column: Open Applications, Displays the Login Form, Fill Data, Enter Username and password, and Displays Menus.
	• SYSTEM column: Login View, Registration View, and Check Username and Password.
5. Insert Decision Diamonds: Use the Decision tool (diamond shape) to place two decision nodes:
	• One in ADMIN labeled Already Have an Account ?.
	• One in SYSTEM labeled Succeed.
6. Connect Flow Control Lines: Select the Control Flow tool (solid arrow) to link the activities following the diagram paths.
7. Label Conditional Branches: Double-click on the flow arrows leaving the decision diamonds to type your conditional guard conditions like Yes, No, or loop-backs.

Part 2: Steps for Diagram 2 (Student Course Registration System)

1. Open a New Activity Workspace: Navigate to Model > Add Diagram > Activity Diagram to start a clean layout tab.
2. Setup Columns: Select the Swimlane (Vertical) tool to draw two swimlanes, naming the left column STUDENT and the right column SYSTEM (or ActivityPartition5).
3. Add Start Node & Actions: Drop an Initial Node at the top of the STUDENT column. Use the Action tool to place the operational boxes:
	• STUDENT column: Open Applications, Displays the Login Form, Enter Login Credentials, Enter Username and password, and Display details of the subjects pending.
	• SYSTEM column: Login View, Check Username and Password, and Check Whether the student has cleared past dues.
4. Add Authentication Check: Place a Decision diamond in the SYSTEM column labeled Succeed.
5. Route Control Flows: Connect the sequence using the Control Flow arrow tool:
	• Link Open Applications across to Login View.
	• Connect Check Username and Password down to the Succeed diamond.
	• Draw a loop-back line from the Succeed diamond's No branch back up to Login View.
	• Route the Yes branch down to Check Whether the student has cleared past dues.
