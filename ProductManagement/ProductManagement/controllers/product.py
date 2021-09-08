from django.shortcuts import render
def addProduct(request):
    return render(request,"addProduct.html")
def getBill(request):
    a = request.GET
    id = a['id']
    name = a['name']
    type = a['type']
    rate = int(a['rate'])
    qty = int(a['qty'])
    gst = int(a['gst'])
    gstamt=rate*qty*gst/100
    netamt=rate*qty+gstamt
    return render(request,"bill.html",{"id":id,"name":name,"type":type,"rate":rate,"qty":qty,"gst":gst,"gstamt":gstamt,"netamt":netamt,"amt":netamt-gstamt})
