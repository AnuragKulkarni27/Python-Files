## Queue IMPLIMENTATION ##

'''Queue implimented as a list
  front : integer having position of 1st(Firstmost) element in stack
  rear : integer having position of last element in queue'''

def cls():
          print("\t")
def isEmpty(Qu):
          if Qu==[]:
                    return True
          else:
                    return False

def Enqueue(Qu,item):
          Qu.append(item)
          if len(Qu)==1:
                    front=rear=0
          else:
                    rear=len(Qu)-1

def Dequeue(Qu):
          if isEmpty(Qu):
                    return "Underflow"
          else:
                    item=Qu.pop(0)
                    if len(Qu)==0:
                              front=rear=none
                    return item
def Peek(Qu):
          if isEmpty(Qu):
                    return "Underflow"
          else:
                    front=0
                    return Qu[front]

def Display(Qu):
          if isEmpty(Qu):
                    print("Queue Empty")
          elif len(Qu)==1:
                    print(Qu[0],"<---Front,rear")
          else:
                    front=0
                    rear=len(Qu)-1
                    print(Qu[front],"<--Front")
                    for a in range(1,rear):
                              print(Qu[a])
                    print(Qu[rear],"<--Rear")
## __Main__Program_##

queue=[]
front=None

while True:
          cls()
          print("QUEUE OPERATIONS")
          print("1. Enqueue")
          print("2. Dequeue")
          print("3. Peek")
          print("4. Display Queue")
          print("5. Exit)")
          ch=int(input("Enter your Choice(1-5) : " ))
          if ch==1:
                    item=int(input("Enter item : "))
                    Enqueue(queue,item)
                    input("Press Enter to Continue...")
          elif ch==2:
                    item=Dequeue(queue)
                    if item=="Underflow":
                              print("Underflow! Queue is Empty.")
                    else:
                              print("Dequeue-ed item is",item)
                    input("Press Enter to Continue...")         
          elif ch==3:
                    item=Peek(queue)
                    if item=="Underflow":
                              print("Underflow! Queue is Empty.")
                    else:
                              print("Frontmost item is",item)
                    input("Press Enter to Continue...")  
          elif ch==4:
                    Display(queue)
                    input("Press Enter to Continue...") 
          elif ch==5:
                    break
          else:
                    print("Invalid Choice!")
                    input("Press Enter to Continue...") 
                    
