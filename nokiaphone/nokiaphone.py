print('1: Phone book')
print('2: Message')
print('3: Chat')
print('4: Call register')
print('5: Tone')
print('6: Settings')
print('7: Call divert')
print('8: Games')
print('9: Calculator')
print('10: Reminders')
print('11: Clock')
print('12: Profiles')
print('13: SIM services')

nokiaphone = int(input('enter option: '))
match(nokiaphone): 
    case 1:
        print('Phone book')
        print('1: Search')
        print('2: Service Nos')
        print('3: Add name')
        print('4: Erase')
        print('5: Edit')
        print('6: Assign tone')
        print('7: Send bcard')
        print('8: Option')
        print('9: Speed dials')
        print('10: Voice tags')
        phonebook = int(input('enter option: '))
        match(phonebook):
            case 1:
                print('1: Search')
            case 2:
                print('2: Service Nos')
            case 3:    
                print('3: Add name')
            case 4:   
                print('4: Erase')
            case 5:   
                print('5: Edit')
            case 6: 
                print('6: Assign tone')
            case 7:
                 print('7: Send bcard')
            case 8:  
                print('Option') 
                print('1: Type of view')
                print('2: Memory status')
        
                option = int(input('enter option: '))
                match(option):
                    case 1:
                        print('2: Type of view')
                    case 2:        
                        print('2: Memory status')
                    case _:
                        print('wrong option')    
                
                
            case 9:   
                print('9: Speed dials')
            case 10:       
                print('10: Voice tags')
            case _:
                print('wrong option')
               
        
    case 2:
        print('Message')
        print('1: write messages')
        print('2: inbox')
        print('3: outbox')
        print('4: picture messages')
        print('5: templates')
        print('6: smileys')
        print('7: message settings')
        print('8: info service')
        print('9: voice mailbox number')
        print('10: service command editor')
        
        messages = int(input('enter option: '))
        match(messages):  
            case 1:
                print('write messages')
            case 2:
                 print('inbox')
            case 3:
                 print('outbox')
            case 4:
                 print('picture messages')
            case 5:
                 print('templates')
            case 6:
                 print('smileys')
            case 7:
                 print('message settings')
                 
                 print('1: setone')
                 print('2: common')
                 messagesettings = int(input('Enter option'))
                 match (messagesettings):      
                    case 1:
                        print('setone')
                        print('1: message centre number')
                        print('2: message sent as')
                        print('3: message validity')
                        
                        setone = int(input('enter option: '))
                        match(setone): 
                            case 1:
                                print('message centre number')
                            case 2:
                                print('message sent as')
                            case 3:
                                print('message validity')              
                
                    case 2:
                        print('common')
                        print('1.Delivery reports')
                        print('2.Reply via same centre')
                        print('3.Character support')
                    
                        common = int(input('enter option: '))
                        match(common): 
                            case 1:
                                print('Delivery reports')
                            case 2:
                                print('Reply via same centre')
                            case 3:
                                print('Character support')    
                            case _:
                                print('wrong option')   
                     
            case 8:
                 print('info service')
            case 9:
                 print('voice mailbox number')
            case 10:
                 print('service command editor')
            case _:
                 print('wrong option') 
        
        
        
        
    case 3:
        print('Chat')   
    case 4:
       
        print('1: missed calls')
        print('2: receieved call')
        print('3: dialled number')
        print('4: erase recent call list')
        print('5: show call duration')
        print('6: show call cost')
        print('7: call cost setting')
        print('8: prepaid credit')
        
        callregister = int(input('enter option: '))
        match(callregister):  
            case 1:
                print('missed calls')
            case 2:
                 print('receieved call')
            case 3:
                 print('dialled number')
            case 4:
                 print('erase recent call list')
            case 5:
                 print('show call duration')
                 print('1: last call duration')
                 print('2: all call duration')
                 print('3: received calls duration')
                 print('4: dialled calls duration')
                 print('5: clear timers')
        showcallduration = int(input('enter option: '))
        match(showcallduration):  
            case 1:
                print('last call duration')
            case 2:
                 print('all call duration')
            case 3:
                 print('received calls duration')
            case 4:
                 print('dialled calls duration')
            case 5:
                 print('clear timers')     
                 
                 
                 
            case 6:
                 print('show call cost')
                 print('1: last call')
                 print('2: all calls cost')
                 print('3: clear counters')
        showcallcost = int(input('enter option: '))
        match(showcallcost):  
            case 1:
                print('last call')
            case 2:
                 print('all calls costall call duration')
            case 3:
                 print('clear counters')    
                 
                 
                 
                 
            case 7:
                 print('call cost setting')
                 print('1: call cost limit')
                 print('2: show costs in')
        callcostsetting = int(input('enter option: '))
        match(callcostsetting):  
            case 1:
                print('call cost limit')
            case 2:
                print('show costs in')     
                 
                 
                 
            case 8:
                 print('prepaid credit')     
            case _:
                 print('wrong option') 
        
        
    case 5:
        print('Tone')
    case 6:
        print('Settings')
    case 7:
        print('Call divert')
    case 8:
        print('Games')
    case 9:
        print('Calculator')
    case 10:
        print('Reminders')
    case 11:
        print('Clock')
    case 12:
        print('Profiles')
    case 13:
        print('SIM services')
    case _:
        print('wrong option') 
        
        
           
        
        
