from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        data = request.get_json()
        expressao = data.get('expressao', '').strip()
        
        if not expressao:
            return jsonify({'erro': 'Expressão vazia'}), 400
        
        # Validar caracteres permitidos
        caracteres_validos = set('0123456789+-*/.() ')
        if not all(c in caracteres_validos for c in expressao):
            return jsonify({'erro': 'Caracteres inválidos'}), 400
        
        # Calcular resultado
        resultado = eval(expressao)
        
        # Formatar resultado
        if isinstance(resultado, float):
            resultado = round(resultado, 10)
        
        return jsonify({'resultado': resultado})
    
    except ZeroDivisionError:
        return jsonify({'erro': 'Divisão por zero!'}), 400
    except SyntaxError:
        return jsonify({'erro': 'Expressão inválida'}), 400
    except Exception as e:
        return jsonify({'erro': 'Erro ao calcular'}), 400

if __name__ == '__main__':
    app.run(debug=True)
