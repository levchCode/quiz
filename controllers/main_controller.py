from flask import Blueprint, render_template, abort, request, redirect, url_for
from models import Question, Option, Answer
from app import db

main_controller = Blueprint('main_controller', __name__)

@main_controller.route('/')
def index():
    questions = Question.query.all()
    return render_template('index.html', questions=questions)

@main_controller.route('/create', methods = ['GET', 'POST'])
def products():
    if request.method == 'POST':
        question_text = request.form['question_text']
        options = request.form.getlist('options[]')

        # Create a new question
        question = Question(text=question_text)
        for option_text in options:
            option = Option(text=option_text)
            question.options.append(option)

        # Save to the database
        db.session.add(question)
        db.session.commit()

        return redirect(url_for('main_controller.index'))

    return render_template('create.html')


@main_controller.route('/question/<int:question_id>')
def question(question_id):
    question = Question.query.filter_by(id=question_id).first()
        
    if question:
        return render_template('question.html', question=question)
    else:
       abort(404)


@main_controller.route('/results/<int:question_id>')
def result(question_id):
    question = Question.query.filter_by(id=question_id).first()
        
    if question:
        return render_template('results.html', question=question)
    else:
       abort(404)


@main_controller.route('/submit', methods = ['GET', 'POST'])
def submit_option():
    option_id = request.form.get('response')
    if not option_id:
        return redirect(url_for('main_controller.index'))

    option = Option.query.get(option_id)
    if not option:
        return redirect(url_for('main_controller.index'))

    user = request.form.get('user')
    response = Answer(user=user, option=option_id)

    db.session.add(response)
    db.session.commit()

    return redirect(url_for('main_controller.index'))
