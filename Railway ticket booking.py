class Railway :
     
    seat = [x for x in range (1,1001)] # list of all seats.
    
    train_Name = 'Howrah-Chakradharpur' 
    
    def __init__ (self, name, b_station, d_station) :
        self.name = name            # Passenger Name
        self.b_station = b_station  # Boarding Station Name
        self.d_station = d_station  # Destination Station Name
        self.seat_no = 0            # initially seat no. is 0
        
        
    def info(self):
        print ()
        print (f'Passenger Name - {self.name}.')
        print (f'Boarding Station  - {self.b_station}.')
        print (f'Destination Station - {self.d_station}.')
        print (f'Train Name - {self.train_Name}.')
    
    
    def book_seat(self):           # This is a Seat Booking Function
        
        if len(Railway.seat) >= 1 :
            self.seat_no = Railway.seat[0]
            del Railway.seat[0]
            print (f'Your Seat No. is {self.seat_no}.')
            print ()
        else :
            print ('Sorry! All seats are booked.')
        
    
    def book_ticket (self):  # This is Ticket Booking Function
        self.info()
        self.book_seat()
       
    
    def cancel_ticket(self): # implementing cancel ticket function 
        Railway.seat.append (self.seat_no) # append the the seat
        Railway.seat = sorted (Railway.seat) # sort the seat each time
        print ('Your Ticket has been cancelled.')
        print (f'Seat No. {self.seat_no} is now available to book.')


if __name__ == '__main__' :
    
    while True :
        try :
            passenger_number = int (input ("How many passengers? : "))        
            break
        except ValueError: # using try except for handing value error
            print ('Please Enter a Number')
    ticket_instances = [] #.      
    for _ in range (passenger_number) :
        
            name = input("Enter your name : ")          
            b_station = input ("Enter Boarding Station Name : ")
            d_station = input ("Enter Boarding Station Name : ")
            ticket_instances.append(Railway (name, b_station, d_station))
        
    for instance in ticket_instances :
        instance.book_ticket()
