import datetime
import pymysql

#import common
import plotting


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def fun_examples():

    r5 = [[2022, 3, 31],[2022, 3, 31],[2025, 3, 14],[2025, 3, 14]]

    [plot_script5, plot_div5] = plotting.create_at(r5)

    return render_template('examples.html', script5=plot_script5, div5=plot_div5)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)
