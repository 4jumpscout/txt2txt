with open('jobs-broken.txt','r') as f2:
    data = f2.read()
    data2=data.replace("}","},")
with open('jobsfinal.txt', 'w') as f3:
    f3.write(data2)

