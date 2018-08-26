from Run_Time_Testing import Testing
from reading_file import Reading_Files
from flask import Flask, request
import main_file
text = ""
#new_obj = Testing(text)
#features = new_obj.get_F()
#training_obj = Reading_Files()
#training_obj.reading()

def testing():
    try:
        filename = 'Testing/1.txt'
        d_p = open(filename)
    except:
        print "No File in Folder for Testing"
        exit()
    else:
        text = d_p.read()
        new_obj = Testing(text)
        if new_obj.size > 0:
            features = new_obj.get_F()
            training_obj.Run_time_Predict(features)
        else:
            print "Not Enough Frames"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    text = request.get_data()
    print text
    testing(text)
    return 'Ok'
if __name__ == "__main__":
    training_obj = Reading_Files()
    training_obj.reading()
    testing()
    #app.run(host="0.0.0.0")

#training_obj.Testing_from_Files()
