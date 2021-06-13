from flask import Flask, render_template, request
import pickle
import numpy as np


filename = 'logistic_regression.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__,template_folder='Template')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        
        first_team = request.form['team1']
        first_team_array = []
        if first_team == 'Chennai Super Kings':
            first_team_array = 0
        elif first_team == 'Delhi Capitals':
            first_team_array = 1
        elif first_team == 'Kolkata Knight Riders':
            first_team_array = 2
        elif first_team == 'Mumbai Indians':
            first_team_array = 4
        elif first_team == 'Punjab Kings':
            first_team_array = 3
        elif first_team == 'Royal Challengers Banglore':
            first_team_array = 5
        elif first_team == 'Rajasthan Royals':
            first_team_array = 6
        elif first_team == 'Sunrisers Hyedrabad':
            first_team_array = 7
            
        
        second_team = request.form['team2']
        second_team_array = []
        if second_team == 'Chennai Super Kings':
            second_team_array = 0
        elif second_team == 'Delhi Capitals':
            second_team_array = 1
        elif second_team == 'Kolkata Knight Riders':
            second_team_array = 2
        elif second_team == 'Mumbai Indians':
            second_team_array = 4
        elif second_team == 'Punjab Kings':
            second_team_array = 3
        elif second_team == 'Royal Challengers Banglore':
            second_team_array = 5
        elif second_team == 'Rajasthan Royals':
            second_team_array = 6
        elif second_team == 'Sunrisers Hyedrabad':
            second_team_array = 7            
            
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
            
        Pitch_type=request.form['Pitch_type']
        if Pitch_type=='Batting' :
            Pitch_type=0
        elif Pitch_type=='Bowling' :
            Pitch_type=3
        elif Pitch_type=='Batting & Spinner Friendly':
            Pitch_type=2
        elif Pitch_type=='Both':
            Pitch_type=1
        
        # city=request.form['city']
        # if city== 'Bangalore':
        #     city = 0
        # elif city== 'Chandigarh':
        #     city =1
        # elif city== 'Kolkata':
        #     city =2
        # elif city== 'Hyderabad':
        #     city =3
        # elif city== 'Chennai':
        #     city =4
        # elif city== 'Delhi':
        #     city =5
        # elif city== 'Mumbai':
        #     city =6
        # elif city== 'Cape Town':
        #     city =7
        # elif city== 'Port Elizabeth':
        #     city =8
        # elif city== 'Durban':
        #     city =9
        # elif city== 'Centurion':
        #     city =10
        # elif city== 'Johannesburg':
        #     city =11
        # elif city== 'East London':
        #     city =12
        # elif city== 'Kimberley':
        #     city =13
        # elif city== 'Bloemfontein':
        #     city =14
        # elif city== 'Cuttack':
        #     city =15
        # elif city== 'Nagpur':
        #     city =16
        # elif city== 'Dharamsala':
        #     city =17
        # elif city== 'Kochi':
        #     city =18
        # elif city== 'Indore':
        #     city =19
        # elif city== 'Visakhapatnam':
        #     city =20
        # elif city== 'Pune':
        #     city =21
        # elif city== 'Raipur':
        #     city =22
        # elif city=='Ranchi' :
        #     city =23
        # elif city=='Sharjah' :
        #     city =24
        # elif city== 'Abu Dhabi':
        #     city =25
        # elif city== 'Dubai':
        #     city =26
        # elif city== 'Mohali':
        #     city =27
            
            
        team1_homeground=request.form['team1_homeground']
        if(team1_homeground=='Yes'):
            team1_homeground=1
        else:
            team1_homeground=0	
        
            
    
        
        temp_array = [first_team_array] + [second_team_array] + [ team1_toss_win, toss_decision, Pitch_type, team1_homeground] #, city] 
        
        data = np.array(temp_array)
        data = data.reshape(1,6)
        
    
        my_prediction = model.predict(data)
        if (my_prediction == 0):
            return render_template('index.html',prediction_text="The winner team is {}".format(second_team))
            
        else:
            return render_template('index.html', prediction_text="The winner team is {}".format(first_team))
    


if __name__ == '__main__':
	app.run(debug=True)