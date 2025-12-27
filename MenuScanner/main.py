from flask import Flask, render_template, request, url_for

main = Flask(__name__)

mood_recommendations = {
    'happy': {'dish': 'Испанский чизкейк', 'link': '/desserts', 'reason': 'Для сладкого праздника!'},
    'sad': {'dish': 'Домашняя лапша', 'link': '/first_course', 'reason': 'Теплый уют в каждой ложке.'},
    'winter': {'dish': 'Шурпа с бараниной', 'link': '/first_course', 'reason': 'Лучший способ согреться зимой.'},
    'hungry': {'dish': 'Плов', 'link': '/second_course', 'reason': 'Сытно и мощно для большого аппетита!'}
}

@main.route('/')
@main.route('/main1')
def main1():
    return render_template('main1.html')

@main.route('/menu1')
def menu1():

    return render_template('menu1.html', moods=mood_recommendations)

@main.route('/breakfast')
def breakfast(): return render_template('breakfast.html')

@main.route('/desserts')
def desserts(): return render_template('desserts.html')

@main.route('/first_course')
def first_course(): return render_template('first_course.html')

@main.route('/second_course')
def second_course(): return render_template('second_course.html')

if __name__ == "__main__":
    main.run(debug=True)