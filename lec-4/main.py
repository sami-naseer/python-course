a=123 #integer
b=12.4 #floating
c="SAmi" #string
# boolean = true or false / 1 or 0 / yes or no

        # 0        1   2     3                indexing for list only
listt=["sami","ammad",123,{"rollno":"124"}]  #order of list matters a lot

dictionary={
    "rollno":123,
    "name":"sami",
    "class":"bsi",
}#dictionary mein hum order agy peechy kr skty hein Q ky  hum usko uski location ki  base py access nahi krty

#cd .. #ye aik step pichli file mein jany ky liye hy
#import krny sy pehly hum cd + space + folder name dalein gy then pyhton click kr ky fr import option py jain gy

with open("tem.txt","r") as file: 
    content=file.read()
    print(content)