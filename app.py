from flask import Flask, render_template, request
import pickle
import numpy as np


filename = 'tree11.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        
        first_team = request.form['team1']
        f_team_CSK = [0]
        f_team_DC = [0]
        f_team_MI = [0]
        f_team_KKR = [0]
        f_team_RCB = [0]
        f_team_RR = [0]
        f_team_PBKS = [0]
        f_team_SRH = [0]
        if first_team == 'Chennai Super Kings':
            f_team_CSK[0] = 1
        elif first_team == 'Delhi Capitals':
            f_team_DC[0] = 1
        elif first_team == 'Kolkata Knight Riders':
            f_team_KKR[0] = 1
        elif first_team == 'Mumbai Indians':
            f_team_MI[0] = 1
        elif first_team == 'Kings XI Punjab':
            f_team_PBKS[0] = 1
        elif first_team == 'Royal Challengers Banglore':
            f_team_RCB[0] = 1
        elif first_team == 'Rajasthan Royals':
            f_team_RR[0] = 1
        elif first_team == 'Sunrisers Hyedrabad':
            f_team_SRH[0] = 1
            
        
        second_team = request.form['team2']
        s_team_CSK = [0]
        s_team_DC = [0]
        s_team_MI = [0]
        s_team_KKR = [0]
        s_team_RCB = [0]
        s_team_RR = [0]
        s_team_PBKS = [0]
        s_team_SRH = [0]
        if second_team == 'Chennai Super Kings':
            s_team_CSK[0] = 1
        elif second_team == 'Delhi Capitals':
            s_team_DC[0] = 1
        elif second_team == 'Kolkata Knight Riders':
            s_team_KKR[0] = 1
        elif second_team == 'Mumbai Indians':
            s_team_MI[0] = 1
        elif second_team == 'Kings XI Punjab':
            s_team_PBKS[0] = 1
        elif second_team == 'Royal Challengers Banglore':
            s_team_RCB[0] = 1
        elif second_team == 'Rajasthan Royals':
            s_team_RR[0] = 1
        elif second_team == 'Sunrisers Hyedrabad':
            s_team_SRH[0] = 1            
            
        team1_toss_win=request.form['team1_toss_win']
        if(team1_toss_win=='Yes'):
            team1_toss_win=1
        else:
            team1_toss_win=0	
            
        
        toss_decision=request.form['toss_decision']
        if(toss_decision=='Batting'):
            toss_decision=1
        else:
            toss_decision=0	
            
        
        team1_homeground=request.form['team1_homeground']
        if(team1_homeground=='Yes'):
            team1_homeground=1
        else:
            team1_homeground=0	
        
        result_runs = [0]
        result_wickets = [0]
        result_tie = [0]
            
    
        
        temp_array = f_team_CSK + f_team_DC + f_team_MI + f_team_KKR + f_team_RCB + f_team_RR + f_team_PBKS + f_team_SRH + s_team_CSK + s_team_DC + s_team_MI + s_team_KKR + s_team_RCB + s_team_RR + s_team_PBKS + s_team_SRH + [team1_toss_win, toss_decision, team1_homeground] + result_runs + result_tie + result_wickets
        
        data = np.array([[temp_array]])
        
    
        my_prediction = model.predict(data[0])
        if (my_prediction == 0):
            return render_template('index.html',prediction_text="The winner team is {}".format(second_team))
            
        else:
            return render_template('index.html', prediction_text="The winner team is {}".format(first_team))
    


if __name__ == '__main__':
	app.run(debug=True)