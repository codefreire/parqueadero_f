from flask import render_template, request
from app import app
from datetime import datetime, timedelta
from models.models import *

class PaseClass():
    def __init__(self, tipo, cupo, pase):
        self.tipo = tipo
        self.cupo = cupo
        self.pase = pase
        self.costo = round(cupo/pase,2)

mensual = PaseClass('mensual',25,96)
semestral = PaseClass('semestral',50,576)
anual = PaseClass('anual',80,1052)
        
        
@app.route('/', methods=['GET', 'POST'])
def index():
    today = datetime.today().strftime('%Y-%m-%d')
    todayy = datetime.today()
    pases = Pase.query.all()
    consultaPases = []
    if request.method == 'POST':
        initialDate = request.form['initialDate']
        date_aux1 = datetime.strptime(initialDate, '%Y-%m-%d')
        dic = {cp.usuarioPase.usuario_nombre : 0 for cp in pases}
        for p in pases:
            aux = []
            nombre = p.usuarioPase.usuario_nombre
            date_exp = p.fecha_compra + timedelta(days=p.cantidad)
            dias = date_aux1-p.fecha_compra
            quedan = p.cantidad - dias.days
            aux.append(nombre)
            aux.append(date_exp)
            aux.append(quedan)
            consultaPases.append(aux)
            #dic.update({nombre : date_exp : quedan})
        #consultaPases = dic.items()
    context = {
        'pases':pases,
        'today':today,
        'consultaPases':consultaPases
    }
    return render_template('index.html', **context)