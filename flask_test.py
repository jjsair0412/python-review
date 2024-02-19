from flask import Flask, request

class cal:
    def __init__(self,myscore) -> None:
        self.myscore = int(myscore)

    def calScore(self):
        realScore = self.myscore

        match realScore :
            case realScore if realScore > 0 and realScore < 10:
                return "F"
            
            case realScore if realScore > 11 and realScore < 20 :
                return "E"
            
            case _:
                return "null"

# Flask 앱 정의
app = Flask(__name__)


@app.route('/')
def root():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No Parameter'
    elif len(parameter_dict) > 0:
        for _,value in parameter_dict.items():
            try:
                score_cal = cal(value)
                return score_cal.calScore()
            except ValueError: # 에러처리
                return "input value error"

    else:
        return 'error !'
    

if __name__ == '__main__':
    app.run(debug=True)
