import pickle
import os
import pathlib


class Ticket:
    name = ''
    email = ''
    event = ''
    reference = 200000

    def bookTicket(self):
        self.name = input("Enter Customer Name: ")
        self.email = input("Enter Customer Email: ")
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)

            self.reference = input("Enter Reference Code(10000 - 50000) : ")
            while True:
                if int(self.reference) <= 10000:
                    print("Warning: Please Enter Valid Reference Code")
                    self.reference = input("Enter Reference Code(10000 - 50000) : ")
                else:
                    break

        for event in eventdetails:
            print("Available Event Code : " + event.eventcode + " Event Name : " + event.eventname)
        infile.close()
        self.event = input("Enter Event Code: ")

    def check(self):
        file = pathlib.Path("tickets.data")
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.email == self.email and ticket.event == self.event:
                    return True
            infile.close()

    def gettotalticketcount(self):
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)
            for event in eventdetails:
                if event.eventcode == self.event:
                    return int(event.eventTotalAvaibleSeat)
            infile.close
        else:
            return 0

    def getBookedSeatCount(self):
        file = pathlib.Path("tickets.data")
        counter = 0
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.event == self.event:
                    counter = counter + 1
            return int(counter)
        return 0


class Event:
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10

    def createEvent(self):
        self.eventname = input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")
        print("\n\n ------> Event Created!")


def bookEventTicket():
    ticket = Ticket()
    ticket.bookTicket()
    if ticket.check():
        print("Warning : You Already Book A Seat")

    elif ticket.getBookedSeatCount() >= ticket.gettotalticketcount():
        print("Warning : All Ticket Sold Out")

    else:
        print("Sucess : Ticket Booked!")
        saveTicketDetiails(ticket)


def saveTicketDetiails(ticket):
    file = pathlib.Path("tickets.data")
    if file.exists():
        infile = open('tickets.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(ticket)
        infile.close()
        os.remove('tickets.data')
    else:
        oldlist = [ticket]
    outfile = open('tempTicket.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempTicket.data', 'tickets.data')


def getTicketDetails():
    file = pathlib.Path("tickets.data")
    if file.exists():
        infile = open('tickets.data', 'rb')
        ticketdetails = pickle.load(infile)
        print("---------------TICKET DETAILS---------------------")
        print("T-Ref    C-Name    C-Email    E-Code")
        for ticket in ticketdetails:
            print(ticket.reference, "\t", ticket.name, "\t", ticket.email, "\t", ticket.event)
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else:
        print("NO TICKET RECORDS FOUND")


def createEvent():
    event = Event()
    event.createEvent()
    saveEventDetails(event)


def saveEventDetails(event):
    file = pathlib.Path("events.data")
    if file.exists():
        infile = open('events.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(event)
        infile.close()
        os.remove('events.data')
    else:
        oldlist = [event]
    outfile = open('tempevents.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempevents.data', 'events.data')


def getEventsDetails():
    file = pathlib.Path("events.data")
    if file.exists():
        infile = open('events.data', 'rb')
        eventdetails = pickle.load(infile)
        print("---------------EVENT DETAILS---------------------")
        print("E-Name    E-Code    E-Total-Seats")
        for event in eventdetails:
            print(event.eventname, "\t", event.eventcode, "\t", event.eventTotalAvaibleSeat)
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else:
        print("NO EVENTS RECORDS FOUND")


def getEventsSummary():
    filetickets = pathlib.Path("tickets.data")
    if filetickets.exists():
        infiletickets = open('tickets.data', 'rb')
        ticketdetails = pickle.load(infiletickets)

    fileEvents = pathlib.Path("events.data")
    if fileEvents.exists():
        infileEvents = open('events.data', 'rb')
        eventdetails = pickle.load(infileEvents)

        print("---------------REPORTS---------------------")
        for event in eventdetails:
            print("\n\nEvent Name : " + event.eventname + " | Total Seats : " + event.eventTotalAvaibleSeat + " \n")
            for ticket in ticketdetails:
                if event.eventcode == ticket.event:
                    print(ticket.reference, "\t", ticket.name, "\t", ticket.email)

        infileEvents.close()
        infiletickets.close()

        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else:
        print("NO EVENTS RECORDS FOUND")


ch = ''
num = 0
while ch != 8:
    print("\t\t\t\t-----------------------")
    print("\t\t\t\tEVENT MANAGEMENT SYSTEM")
    print("\t\t\t\t-----------------------")
    print("\tMAIN MENU")
    print("\t1. BOOK TICKET")
    print("\t2. VIEW TICKET")
    print("\t3. CREATE EVENTS")
    print("\t4. VIEW EVENTS")
    print("\t5. SHOW SUMMARY")
    print("\t6. QUIT")
    print("\tSelect Your Option (1-6) ")
    ch = input()

    if ch == '1':
        bookEventTicket()
    elif ch == '2':
        getTicketDetails()
    elif ch == '3':
        createEvent()
    elif ch == '4':
        getEventsDetails()
    elif ch == '5':
        getEventsSummary()

    elif ch == '6':
        break
