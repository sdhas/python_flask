from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/home')
    def homepage():
        return render_template('index_tmp.html')
    
    @app.route('/contact')
    def about():
        return render_template('contact.html')

    # @app.route('/services')
    # def services():
    #     return render_template('services.html')

    # @app.route('/events')
    # def events():
    #     return render_template('events.html')

    # @app.route('/about')
    # def about():
    #     return render_template('about.html')

    # @app.route("/contact", methods=['POST', 'GET'])
    # def contact():
    #     if request.method == 'POST':
    #         n = request.form.get('name')
    #         a = request.form.get('age')
    #         c = request.form.get('city')
    #         return  render_template('contact.html',name=n,age=a,city=c)
        

    # app name 
    @app.errorhandler(404) 
    
    # inbuilt function which takes error as parameter 
    def not_found(e): 
    
        # defining function 
        return render_template("index_tmp.html")
    
    return app

app = create_app()
if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port="80")
