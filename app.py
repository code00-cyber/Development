from flask import Flask, render_template, jsonify
app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'New York',
        'salary':'$50,000',
        'company':'Google',
    },
  {
      'id':2,
      'title':'Data Scientist',
      'location':'New Delhi',
      'salary':'$250,000',
      'company':'Google',
  },
  {
      'id':3,
      'title':'Senior Developer',
      'location':'Benguluru',
      'salary':'$350,000',
      'company':'Google',
  },
  {
      'id':4,
      'title':'Front end developer',
      'location':'New York',
      'salary':'$150,000',
      'company':'Google',
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs=JOBS, company_name='Google')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)