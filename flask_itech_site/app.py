from flask import Flask, render_template, request

app = Flask(__name__)

#หน้าเว็บสำหรับการแสดงผลของ หน้าแรก
@app.route('/')
def index():
    return render_template('index.html')

#หน้าเว็บสำหรับการแสดงผลของ ช่องทางค้นหา
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return render_template('search.html', query=query)

#หน้าเว็บสำหรับการแสดงผลของ ช่องทางการคติดต่อ
@app.route('/contact')
def contact():
    return render_template('contact.html')

#หน้าเว็บสำหรับการแสดงผลของ ระดับปวช
@app.route('/voc')
def voc():
    return render_template('voc.html')

#หน้าเว็บสำหรับการแสดงผลของ ระดับปวส
@app.route('/hvoc')
def hvoc():
    return render_template('hvoc.html') 


#หน้าเว็บสำหรับการแสดงผลของ ปริญญาตรี
@app.route('/bhd')
def bhd():
     return render_template('bhd.html')

#หน้าเว็บสำหรับการแสดงผลของ ปริญญาโท
@app.route('/mhd')
def mhd():
    return render_template('mhd.html')  

#หน้าเว็บสำหรับการแสดงผลของ ปริญญาเอก
@app.route('/phd')
def phd():
    return render_template('phd.html')   

#หน้าเว็บสำหรับการแสดงผลของ ประวัติ
@app.route('/history')
def history():
    return render_template('history.html')

#หน้าเว็บสำหรับการแสดงผลของ วิสัยทัศน์
@app.route('/vision')
def vision():
    return render_template('vision.html') 

#คณะผู้บริหาร
@app.route('/ec')
def ec():
    return render_template('ec.html')

#หน้าเว็บสำหรับการแสดงผลของ อาคารเรียน  
@app.route('/tower.html')
def tower():
    return render_template('tower.html')

#หน้าเว็บสำหรับการแสดงผลของ ระบบอื่นๆ
@app.route('/otherapp')
def otherapp():
    return render_template('otherapp.html')



if __name__ == '__main__':
    app.run(debug=True)

