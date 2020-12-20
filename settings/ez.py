x = open("settings.py",'r')
y = x.read()
for i in range(50):
    f = open("settings" + str(i) + ".py",'w');
    f.write(y)  
    f.close();
x.close()
