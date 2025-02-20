from flask import Flask, render_template, url_for, request
app= Flask(__name__)
import math

#route = url or link 

#main route 
@app.route("/")
def main():
    
    return render_template("index.html",home=True)

@app.route("/simple")
def simple():
    return render_template("simple.html",home=False)

@app.route("/advanced")
def advanced():
    return render_template("advanced.html",home=False)

@app.route("/calculate",methods=["post"])
def calculate():
    first_number = int(request.form["First number"])
    operation=request.form["operation"]
    second_number=int(request.form["Second number"])
    note=""
    color="alert-success"
    if  operation=="plus":
        result=first_number+second_number
        note="addition was perfromed successfully"
    elif  operation=="minus":
        result=first_number-second_number
        note="Subtraction was perfromed successfully"   
    elif  operation=="multiply":
        result=first_number*second_number
        note="multiplication was perfromed successfully"  
    elif  operation=="divide":
        result=first_number/second_number
        note="division was perfromed successfully"
    else:
        note="There is an error"
        color="alert-danger"
        return render_template("simple.html",note=note)
    return render_template("simple.html",result=result,note=note,color=color)

@app.route("/calculate_advanced",methods=["post"])
def calculate_advanced():
    note=""
    color="alert-success"
    first_number = int(request.form["First number"])
    operation=request.form["operation"]
    try: 
        if operation=="Sin":
            result=math.sin(first_number)
            note="sin was perfromed successfully"
        elif operation=="Cos":
            result=math.cos(first_number)
            note="Cos was perfromed successfully"
        elif operation=="Tan":
            result=math.tan(first_number)
            note="Tan was perfromed successfully"
        elif operation=="Square Root":
            result=math.sqrt(first_number)
            note="Square Root was perfromed successfully"
        elif operation=="log":
            result=math.log(first_number)
            note="log was perfromed successfully"
        elif operation=="asinh":
            result=math.asinh(first_number)
            note="Asinh was perfromed successfully"
        elif operation=="acosh":
            result=math.acosh(first_number)
            note="acosh was perfromed successfully"
        elif operation=="factorial":
            result=math.factorial(first_number)
            note="factorial was perfromed successfully" 
        elif operation=="atanh":   
            result=math.atanh(first_number)
            note="atanh was perfromed successfully"
        else:
            color="alert-danger"
            return render_template("advanced.html",note="There is an error")
    except ValueError:
        return render_template("advanced.html",result=0,note="Mathematical error",color="alert-danger")
    return render_template("advanced.html",result=result,note=note,color=color)
        
if __name__ == "__main__":
    app.run(debug=True) # to see the error msg if false - we see no error msg 