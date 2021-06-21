import socket 
# import socket module /library to create 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# what is my receiver address
recv_addr=("127.0.0.1",9999)
# Now i want to send message
user_data=input("enter your message :- ")
# converting data into ascii code
newdata=user_data.encode('ascii')
# now you can send data 
s.sendto(newdata, recv_addr)
print("your message has been sent..")
