from flask import Flask, render_template, request
# from werkzeug import secure_filename
# import web_predictor as wp


app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')


# Upload page
@app.route('/WildLifeID')
def wildlifeid():
    pass
    # return render_template('blog.html')



@app.route('/Blog')
def blog():
    pass
    # return render_template('upload.html')




if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)
