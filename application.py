from flask import Flask, render_template      
import random
app = Flask(__name__)

@app.route("/")
def home():
  random_dice = { 
    1: "fas fa-dice-one",
    2: "fas fa-dice-two",
    3:"fas fa-dice-three",
    4:"fas fa-dice-four",
    5:"fas fa-dice-five",
    6: "fas fa-dice-six"
  }
  rand_test = random_dice[random.randint(1,6)]
  rand_test2 = random_dice[random.randint(1,6)]

  rand_dict = random_dice
  rand1 = random.randint(1,6)
  rand2 = random.randint(1,6)
  rand3 = random.randint(1,6)
  rand4 = random.randint(1,6)
  

  vinnare = None
  if (rand1 + rand2) > (rand3 + rand4):
    vinnare = True
   
  elif (rand1 + rand2) < (rand3 + rand4):
    vinnare = False
    

  return render_template("index.html",rand_dict=rand_dict,rand1=rand1,rand2=rand2,rand3 =rand3,rand4= rand4,vinnare=vinnare)
    

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
 
