
Part 1: Steps for Diagram 1 (Railway Management System)

1. Initialize a Class Workspace: Open StarUML, select Model > Add Diagram > Class Diagram from the top menu.
2. Create the Classes: Select the Class tool from the left Toolbox and place 6 classes onto your canvas: Clerk, Passenger, Train, Ticket, Payment, and RailwaySystem.
3. Add Attributes (Variables): Right-click each class, select Add > Attribute, and type the variables prefixed with + for public visibility:
	• Clerk: +id, +name
	• Passenger: +name, +address, +gender, +age
	• Train: +trainNo, +trainName
	• Ticket: +pnrNo, +status, +noOfPerson, +chargeType
	• Payment: +amount
	• RailwaySystem: +id
4. Add Operations (Methods): Right-click a class, select Add > Operation, and input its functions with parentheses:
	• Clerk: +form_detail(), +cancellation_form()
	• Passenger: +searchTrain(), +bookTicket(), +cancelTrain(), +payCharges(), +modifyForm(), +Operation1()
	• Ticket: +newTicket(), +deleteTicket()
	• RailwaySystem: +response()
5. Draw Associations: Select the Association tool from the Toolbox and click-and-drag lines to connect your classes. Double-click the middle of the lines to add relationship text labels like Works, Makes, Books, and Cancels.



Part 2: Steps for Diagram 2 (Online Movie Ticket Booking System)

1. Open a New Class Canvas: Go to Model > Add Diagram > Class Diagram to open a fresh workspace tab.
2. Place All 9 Classes: Use the Class tool to place the blocks onto the screen: User, Admin, Booking, Movie, Screen, Seat, Payment, Theater, and Shows.
3. Insert Attributes (+): Right-click each class box, select Add > Attribute, and add the fields exactly as illustrated:
	• User & Admin: Add their respective names, IDs (+userId / +adminId).
	• Booking: +bookingId, +movieName_FK.
	• Movie: +name, +duration.
	• Screen: +screenNo, +qulaity.
	• Seat: +topRow, +middleRow, +lastRow, +cost.
	• Payment: +paymentId, +userId, +bookingId, +showId, +amount.
	• Theater: +name, +location, +slots.
	• Shows: +showId, +time, +screenNo.
4. Insert Operations (Methods): Right-click the classes, choose Add > Operation, and fill out the execution blocks:
	• User: +login(), +register(), +search_movies(), +book_Tickets(), +cancel_Booking().
	• Admin: +add_movie(), +remove_movie(), +update_movie(), +set_show_timings().
5. Apply Composition & Associations:
	• Use the standard Association tool to connect links like User to Booking or Admin to Movie. Double-click lines to type relationship names (adds, is played, has, leads to, etc.).
	• Use the Composition tool (line with a filled diamond) to connect Booking to Screen and Screen to Seat as indicated by the dark diamond shapes.
6. Set Multiplicity Labels: Click any association line, navigate to the Properties panel on the right, and input the structural multiplicities for End1 and End2 (e.g., 1, *).
