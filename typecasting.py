#Type Cast->Data Type Conversion
#Types: 1) Implicit-automatic conversion means interpreter does
#2) Explicit->by user forcefully

#1) Implicit
# a=4
# b=5
# print(a,b)
# division=a/b
# print(division,type(division)) #0.8 <class 'float'>

# print(3/3) #1.0

# n=1,2,3
# print(n,type(n)) #tuple

#Explicit
# print("-------int to float,complex,bool,str")
# n=1234
# print(n,type(n)) #1234 <class 'int'>

# n_float=float(n)
# print(n_float,type(n_float)) #1234.0 <class 'float'>

# n_complex=complex(n)
# print(n_complex,type(n_complex)) #(1234+0j) <class 'complex'>

# n_bool=bool(n)
# print(n_bool,type(n_bool)) #True <class 'bool'> 

# n_bool=bool(0)
# print(n_bool,type(n_bool)) #False <class 'bool'> 

# n_bool=bool("")
# print(n_bool,type(n_bool)) #False <class 'bool'>

# n_bool=bool(None)
# print(n_bool,type(n_bool)) #False <class 'bool'>

# n_str=str(n)
# print(n_str,type(n_str)) #1234 <class 'str'>

# n_none=None(n) #TypeError: 'NoneType' object is not callable
# print(n_none,type(n_none))

#-------------------------------------------------

# print("-------float to int,complex,bool,str")
# n=1234.746456
# print(n,type(n)) #1234.746456 <class 'float'>

# n_int=int(n)
# print(n_int,type(n_int)) #1234 <class 'int'>

# n_complex=complex(n)
# print(n_complex,type(n_complex))  #(1234.746456+0j) <class 'complex'>

# n_bool=bool(n)
# print(n_bool,type(n_bool)) #True <class 'bool'>

# n_str=str(n)
# print(n_str,type(n_str)) #1234.746456 <class 'str'>

#-------------------------------------------------

# print("-------complex to int,float,bool,str")
# n=1234j
# print(n,type(n)) #1234j <class 'complex'>

# n_int=int(n) #error not possible
# print(n_int,type(n_int)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# n_float=float(n) #error not possible
# print(n_float,type(n_float))  #TypeError: float() argument must be a string or a real number, not 'complex'

# n_bool=bool(n)
# print(n_bool,type(n_bool)) # True <class 'bool'>

# n_str=str(n)
# print(n_str,type(n_str)) #1234j <class 'str'> 

#----------------------------------------------

# print("-------boolean to int,float,bool,str")
# n=True
# print(n,type(n)) #True <class 'bool'> 

# n_int=int(n)
# print(n_int,type(n_int)) #1 <class 'int'>

# n_complex=complex(n)
# print(n_complex,type(n_complex))  #(1+0j) <class 'complex'>

# n_float=float(n)
# print(n_float,type(n_float)) # 1.0 <class 'float'> 

# n_str=str(n)
# print(n_str,type(n_str)) # True <class 'str'>    


#-----------------------------------------------

print("-------str to int,float,complex,bool")
n="welcome"
print(n,type(n)) #welcome <class 'str'>

n_int=int(n) #error not possible
print(n_int,type(n_int)) # ValueError: invalid literal for int() with base 10: 'welcome'

n_complex=complex(n) #error not possible
print(n_complex,type(n_complex))  #ValueError: complex() arg is a malformed string

n_float=float(n) #error not possible
print(n_float,type(n_float)) #ValueError: could not convert string to float: 'welcome'

n_bool=bool(n)
print(n_bool,type(n_bool)) #True <class 'bool'> 