from django.shortcuts import render
def getStudent(request):
    return render(request,"studentRecord.html")
def getMarkSheet(request):
    a=request.GET
    sname=a['sname']
    fname=a['fname']
    gender=a['gender']
    school=a['scname']
    maths=a['maths']
    physics=a['physics']
    chemistry=a['chemistry']
    hindi=a['hindi']
    english=a['english']
    total=(int(maths)+int(chemistry)+int(physics)+int(hindi)+int(english))
    prefix=getPrefix(gender)
    return render(request,"marksheet.html",{"sname":sname,"fname":fname,"school":school,"maths":maths,"english":english,"hindi":hindi,"chemistry":chemistry,"physics":physics,"marks":total,"percentage":total/5,"grade":getGrade(total),"prefix":prefix[0],"fprefix":prefix[1]})
def getPrefix(gender):
    return ['Master',"S/O"] if(gender=="Male") else ["Miss","D/O"]
def getGrade(total):
    total=total/5
    if(total>=60 and total<=100):return "A"
    elif(total>=48 and total<60):return "B"
    elif(total>=33 and total<48):return "C"
    else:return "D"