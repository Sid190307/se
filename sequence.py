
Part 1: Steps for Diagram 1 (Music Player App)

1. Initialize a Sequence Workspace: Open StarUML, select Model > Add Diagram > Sequence Diagram from the top menu.
2. Add Lifelines (Objects): Select the Lifeline tool from the left Toolbox and place 3 lifelines horizontally across the top, naming them User, Device, and Database.
3. Draw Synchronous Messages: Select the Message tool (solid line arrow) to draw standard communications between lifelines:
	• From User to Device: 1 : Open Application
	• From User to Device: 4 : Detect Face
	• From Device to Database: 5 : Retrieve Mood and 8 : Retrieve Music
4. Draw Self-Messages (Loops): Select the Self Message tool from the toolbox, click on the Device lifeline box, and label it 2 : Access Webcam.
5. Draw Reply Messages: Select the Reply Message tool (dashed line arrow) to create data returns:
	• From Device to User: 3 : Get Photo and 7 : Display Mood
	• From Database to Device: 6 : Mood and 9 : Generated Playlist
	• From Device to User: 10 : Playlist


Part 2: Steps for Diagram 2 (Student Event Registration Form)

1. Open a New Sequence Canvas: Go to Model > Add Diagram > Sequence Diagram to create a fresh workspace tab.
2. Setup the 5 Lifelines: Use the Lifeline tool to align the 5 system components across the top of your layout: Student - User, Web Portal, Event Registration Server, Student Database, and Notification Service.
3. Map the Forward Request Flow: Use the standard Message tool (solid arrow) to link the step-by-step actions:
	• Student - User \(\rightarrow \) Web Portal: 1 : Opens Portal
	• Student - User \(\rightarrow \) Web Portal: 4 : Fill form and submit
	• Web Portal \(\rightarrow \) Event Registration Server: 5 : Registration Request
	• Event Registration Server \(\rightarrow \) Student Database: 7 : Store Data
	• Event Registration Server \(\rightarrow \) Notification Service: 9 : Send Conformation Email
4. Configure Internal Server Validation: Select the Self Message tool and apply it to the respective lifelines:
	• On Web Portal: 2 : Opens Registration Form
	• On Event Registration Server: 6 : Validate Form
5. Draw the Dash-Line Response Matrix: Select the Reply Message tool (dashed arrow) to map out all downstream confirmation loops:
	• Web Portal \(\rightarrow \) Student - User: 3 : Displays Form
	• Student Database \(\rightarrow \) Event Registration Server: 8 : Registration Saved
	• Notification Service \(\rightarrow \) Student - User: 10 : Conformation Email
	• Event Registration Server \(\rightarrow \) Web Portal: 11 : Success response followed by Web Portal \(\rightarrow \) Student - User: 12 : Registration Successful
	• Event Registration Server \(\rightarrow \) Web Portal: 13 : Error response followed by Web Portal \(\rightarrow \) Student - User: 14 : Registration Failed
