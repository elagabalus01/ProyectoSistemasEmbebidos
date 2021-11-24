from flask import jsonify

class LedHab():
    def __init__(self,app,led):
        self.led=led
        @app.route('/api/ledhab', methods=['GET', 'POST'])
        def dash_ladhab():
            try:
                data = dict()
                data['ledhab'] = self.led.value
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})
        
        @app.route('/api/accion/ledhab', methods=['GET', 'POST'])
        def accion_ledhab():
            try:
                if self.led.value==1:
                    self.led.value=0
                else:
                    self.led.value=1
                data={'status_ledhab':True}
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify(data={'status_ledhab':False})
