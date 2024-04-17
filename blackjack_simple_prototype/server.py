from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

# Importing the lessons and quiz questions
from lessons import lessons
from questions import quiz_questions

app = Flask(__name__)

score = 0

########################
#        ROUTES        #
########################

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/results')
def results():
    global quiz_questions 
    global score
    tmp = score 
    score = 0
    total = int(len(quiz_questions))
    return render_template('results.html', score = tmp, total=total)

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/quiz_start')
def quiz_start():
    return render_template('quiz_start.html')

@app.route('/lesson/<module_id>/<lesson_id>')
def lesson(module_id, lesson_id):

    lesson = lessons[module_id][lesson_id]
    return render_template('lesson.html', lesson = lesson, module_id = module_id, lesson_id = lesson_id)

@app.route('/lesson_complete/<module_id>')
def lesson_complete(module_id):
    
    lesson = lessons[module_id]
    return render_template('lesson_complete.html', module_id = module_id, lesson = lesson)


@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    question = quiz_questions[quiz_id]
    return render_template('quiz.html', question = question)


@app.route('/answer', methods=['POST'])
def answer():
    
   data = request.json
   answer_index = int(data.get('answerIndex'))
   quizID = data.get('quizId')
   if answer_index == quiz_questions[quizID]['answer']:
        result = "Correct!"
        global score 
        score += 1
   else:
        result = "Wrong, the correct answer was: " + quiz_questions[quizID]['panswers'][quiz_questions[quizID]['answer']]

   quiz_questions[quizID]['result'] = result
   quiz_questions[quizID]['client_response'] = quiz_questions[quizID]['panswers'][answer_index]
   
   return result




if __name__ == '__main__':
   app.run(debug = True)


