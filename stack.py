stack=[]

def push():
    if len(stack)==n:
        print("List is full!")
    element=input("Enter the element: ")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is empty!")
    else:
        e=stack.pop()
        print("Removed element: ",e)
        print(stack)
n=int(input("Enter limit of stack: "))
while True:
    print("Select the Operation: \n 1.Push \n 2.Pop \n 3.Quit")
    choice=int(input("Enter Choice: "))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct Operation!")
