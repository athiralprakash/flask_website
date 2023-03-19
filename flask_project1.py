from flask import Flask,render_template
#from flask import Flask,render_template
#creating a website instances/object naming it as website
app=Flask ("flask_website")

@app.route("/home") #naming the page as home
def home ():# @ is a decorator it connects app.route to the function home
    return render_template("tutorial.html") #render_template functiom allows to read html file . \
                                            #it should be under templates folder

app.run(debug=True) #this will help us to see errors on the webpage


@app.route("/about") #adding another page called about
                    #add about in nav tag in main home page
def about () :
    return render_template("about.html")

app.run(debug=True)