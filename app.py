from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return render_template('search.html', query=query)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/voc')
def voc():
    return render_template('voc.html')

@app.route('/hvoc')
def hvoc():
    return render_template('hvoc.html') 

@app.route('/bhd')
def bhd():
     return render_template('bhd.html')


@app.route('/mhd')
def mhd():
    return render_template('mhd.html')  

@app.route('/phd')
def phd():
    return render_template('phd.html')   

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)