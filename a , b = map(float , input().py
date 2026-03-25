a , b = map(float , input().split())
phep_tinh = input("+ , - , * , /")
if phep_tinh == "+" : 
    print ('Tổng của 2 phép tính :' , a + b )
elif phep_tinh == "-" : 
    print ('Hiệu của 2 phép tính : ' , a-b)
elif phep_tinh == "*"  :
    print ("Tích của 2 phép tính :" , a* b)
else : 
    if b == 0 : 
        print ('Không chia được đâu')
    else : 
        print ('Thương của 2 phép tính :' , a / b)
