# 8. Write a program to illustrate variable scope 
# using local global and nonlocal variables. 


v_global = 10

def abc():
    v_nonlocal = 10
    global v_global
    v_global = 20
    def xyz():
        v_local = 10
        print("local variable: ", v_local)
        nonlocal v_nonlocal
        v_nonlocal = 20    
    xyz()
    print("after changing Nonlocal variable: ", v_nonlocal)
abc()
print("after changing global variable: ", v_global)

     
        
        
