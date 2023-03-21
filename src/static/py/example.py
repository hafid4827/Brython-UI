from browser import document, bind, alert


dcoumet_temp = document.getElementById("temporal")

@bind(dcoumet_temp, 'click')
def temporal(event):
    alert("hola mundo")




