from flask import Flask, jsonify, render_template
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import *
app = Flask(__name__)
spec = FlaskPydanticSpec(app)

@app.route('/<tipo>/<quantidade>')
def index(tipo, quantidade ):
    """
         API para calcular a validade

         ## Endpoint
         /datas/<tipo>/<quantidade>



         ### Resposta (JSON):
         '''json
        {
        "data": 27-03-25
        "validade": 5
        }
        :quantidade: quantidade
        :tipo tipo (mes, ano, dia, semanas)
    """
    prazo = int(quantidade)
    meses = datetime.today() + relativedelta(months=prazo)
    anos = datetime.today() + relativedelta(years=prazo)
    semanas = datetime.today() + relativedelta(weeks=prazo)
    dias = datetime.today() + relativedelta(days=prazo)

    validade = ""

    if tipo == 'meses':
        validade = meses
    elif tipo == 'anos':
        validade = anos
    elif tipo == 'semanas':
        validade = semanas
    elif tipo == 'dias':
        validade = dias


    return jsonify({
        "data": datetime.today().strftime("%d-%m-%Y"),
        'validade': validade.strftime("%d-%m-%Y"),
    })

    # iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)