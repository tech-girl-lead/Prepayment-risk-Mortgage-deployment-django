from django.shortcuts import render
import joblib
from joblib import load
model_path = "/Users/SalmaDkier/Desktop/TechnoDeployment/savedModels/model.joblib"
model = joblib.load(model_path)


def predictor(request):
    if request.method == 'POST':
        creditscore = request.POST['creditscore']
        origupb = request.POST['origupb']
        isfirsttime = request.POST['isfirsttime']
        creditrange_excellent = request.POST['creditrange_excellent']
        creditrange_good = request.POST['creditrange_good']
        creditrange_poor = request.POST['creditrange_poor']

        y_pred = model.predict([[ creditscore, origupb, isfirsttime, creditrange_excellent, creditrange_good, creditrange_poor]])
        if y_pred[0] == 0:
            y_pred = 'Not Ever Delinquent'
        elif y_pred[0] == 1:
            y_pred = 'Ever Delinquent'
       
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')

