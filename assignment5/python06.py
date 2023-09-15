# Write a function translate() that will translate a text into "rövarspråket"
# (Swedish for "robber's language"). That is, double every consonant and place an
# occurrence of "o" in between. For example, translate("this is fun") should return
# the string "tothohisos isos fofunon".

def translate():
    input_str = input("Enter a string")
    str1=''
    for i in input_str:
        if(i=='a' or i=='e' or i=='o' or i=='u' or i=='i' or i==' '):
            str1+=i
        else:
            str1+=i
            str1+='o'
            str1+=i
    print(str1)


translate()