from flask import Flask, request, jsonify

import json
        
import pandas as pd

df=pd.read_csv("df.csv")


app = Flask(__name__)

@app.route('/query',methods=['POST'])
def query():
    req=request.json
    op1=req['operand1']
    op2=req['operand2']
    op=req['operator']
    if op =='>':
        t=list(df.loc[df[op1] > op2]['_id'])
        
    elif op == '==':
        t=list(df.loc[df[op1] == op2]['_id'])
    else:
        t=list(df.loc[df[op1] < op2]['_id'])
    return jsonify({'response':t})
@app.route('/q2',methods=['POST'])
def q2():
    req=request.json
    op1=req['operand1']
    op2=req['operand2']
    op=req['operator']
    if op =='>':
        t=list(df.loc[df[op1] > op2]['discount'])
    elif op == '==':
        t=list(df.loc[df[op1] == op2]['discount'])
    else:
        t=list(df.loc[df[op1] < op2]['discount'])
    t1=len(t)
    t2=sum(t)/len(t)
    return jsonify({'discounted_products_count':t1 , 'avg_discount':t2})
@app.route('/q3',methods=['POST'])
def q3():
    req = request.json
    op1 = req['operand1']
    op2 = req['operand2']
    op = req['operator']
    if op == '>':
        t = list(df.loc[(df[op1] > op2)&(df['competition'] != "0")]['_id'])
    elif op == '==':
        t = list(df.loc[(df[op1] == op2)&(df['competition'] != "0")]['_id'])
    else:
        t = list(df.loc[(df[op1] < op2)&(df['competition'] != "0")]['_id'])
    #filter(lambda a: a != "0", t)
    return jsonify({'expensive_list': t})
@app.route('/q4',methods=['POST'])
def q4():
    req = request.json
    op1 = req['filters'][0]['operand1']
    op2 = req['filters'][0]['operand2']
    op = req['filters'][0]['operator']
    op3 = req['filters'][1]['operand1']
    op4 = req['filters'][1]['operand2']
    ope = req['filters'][1]['operator']
    if op == '>':
        x=df[op1] > op2
    elif op == '==':
        x=df[op1] == op2
    else:
        x=df[op1] < op2
    if ope == '>':
        x1=df[op3] > op4
    elif ope == '==':
        x1=df[op3] == op4
    else:
        x1=df[op3] < op4
    t = list(df.loc[(x)&(x1)&(df['competition'] != "0")]['_id'])
    return jsonify({'competition_discount_diff_list' : t})
if __name__=='__main__':
    app.run(debug=True, port=9090)