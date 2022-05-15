from flask import Flask,request,jsonify
import joblib
import pandas as pd

# Create Flask APP
app=Flask(__name__)


# Connect Post API CALL --> Predict() Function
@app.route('/predict',methods=['POST'])
def predict():
    
    # Get Json Request
    feat_data=request.json
    
    #Convert Json to pandas DF (col names)
    df=pd.DataFrame(feat_data)
    df=df.reindex(columns=col_names)
    
    #predict
    prediction=list(model.predict(df))
    
    return jsonify({'predicyion':str(prediction)})

# Load My Model And Load Column Names
if __name__=='__main__':
    
    model=joblib.load("final_model.pkl")
    columns=joblib.load('col_names.pkl')
    
    app.run(debug=True)