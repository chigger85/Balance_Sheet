import numpy as np


class Attendee:
    
    instances = []
    
    def __init__(self,name,paid):
        self.name = name
        self.paid = paid
        Attendee.instances.append(self)

        

keir = Attendee('Keir',130)
chigs = Attendee('Chigger', 5016)
muz = Attendee('Muz',220)
olam = Attendee('Olam',412.2)
gaz = Attendee('Gaz',51)
pete = Attendee('Pete',57)
dan = Attendee('Dan',150)
jdm = Attendee('JDM',509)
ant = Attendee('Ant',1003)
benj = Attendee('Benj',120)
fletch = Attendee('fletch',650)
matt = Attendee('Matt',2013)

def get_paid(name):
    return name.paid
    
total = 0

for i in Attendee.instances:
    total+=get_paid(i)
    
debt = round(total/(len(Attendee.instances)),2)

for i in Attendee.instances:
        i.balance = i.paid-debt


 
attendees = Attendee.instances

def get_creditors(people):
    creditors = []
    for i in people:
        if i.balance>0:
            creditors.append(i)
    return creditors
    
def get_debtors(people):
    debtors = []
    for i in people:
        if i.balance<0:
            debtors.append(i)
    return debtors

# for i in get_debtors(attendees):
#     while i.balance<0:
#         for j in get_creditors(attendees):
#             while j.balance>0:
#                j.balance = j.balance

def transaction(n,p):
    #n and p are the initial list index of the debtors and the creditors
    ppl_in_debt = get_debtors(attendees)
    ppl_in_cred = get_creditors(attendees)
    
    data = []
    
    while len(ppl_in_debt)>0:
    
        giver_name = ppl_in_debt[n].name
        giver_balance_i = ppl_in_debt[n].balance
        receiver_name = ppl_in_cred[p].name
        receiver_balance_i = ppl_in_cred[p].balance
        
        
        if np.abs(giver_balance_i)<= np.abs(receiver_balance_i):
            receiver_balance_f = receiver_balance_i+giver_balance_i
            giver_balance_f = 0
            get_debtors(attendees)[n].balance = giver_balance_f
            get_creditors(attendees)[p].balance = receiver_balance_f
            
        else:
            giver_balance_f = giver_balance_i+receiver_balance_i
            receiver_balance_f = 0
            get_creditors(attendees)[p].balance = receiver_balance_f
            get_debtors(attendees)[n].balance = giver_balance_f

    

        trans = giver_name, round(giver_balance_i,2),round(giver_balance_f,2), receiver_name, round(receiver_balance_i,2),round(receiver_balance_f,2)
        data.append(trans)
    
        ppl_in_debt = get_debtors(attendees)
        ppl_in_cred = get_creditors(attendees)
    
    transactions = []
    for i in range(len(data)):
        transactions.append(data[i][0]+" give "+str(round(data[i][2]-data[i][1],2))+" to "+ data[i][3])
        
    return data,transactions
        




    
    
    
    
    
    
    
        
        
       
    
        

