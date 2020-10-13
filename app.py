from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse/')
def browse():
    return render_template('browse.html')

@app.route('/basketball/')
def basketball():
    return render_template('basketball.html')

@app.route('/football/')
def football():
    return render_template('football.html')

@app.route('/baseball/')
def baseball():
    return render_template('baseball.html')

@app.route("/basketball-1/")
def bill():
    return "<h1>The Book of Basketball</h1>" \
           "<br>" \
           "<h2>Bill Simmons</h2>" \
           "<br>" \
           "<p>The Book of Basketball: The NBA According to the Sports Guy is the second book by former ESPN columnist Bill Simmons. Published in 2009, it covers the history of the National Basketball Association.</p>"


@app.route("/basketball-2/")
def rings():
    return "<h1>Eleven Rings: The Soul of Success</h1>" \
           "<br>" \
           "<h2>Hugh Delehanty and Phil Jackson</h2>" \
           "<br>" \
           "<p>During his storied career as head coach of the Chicago Bulls and Los Angeles Lakers, Phil Jackson won more championships than any coach in the history of professional sports. Even more important, he succeeded in never wavering from coaching his way, from a place of deep values.</p>"


@app.route("/basketball-3/")
def mamba():
    return "<h1>The Mamba Mentality: How I Play</h1>" \
           "<br>" \
           "<h2>Kobe Bryant</h2>" \
           "<p>The Mamba Mentality: How I Play is Kobe Bryant's personal perspective of his life and career on the basketball court and his exceptional, insightful style of playing the game—a fitting legacy from the late Los Angeles Laker superstar.</p>"


@app.route("/football-1/")
def fever():
    return "<h1>Fever Pitch</h1>" \
           "<br>" \
           "<h2>Nick Hornby</h2>" \
           "<br>" \
           "<p>Fever Pitch: A Fan's Life is a 1992 autobiographical essay by British author Nick Hornby. The book is the basis for two films: Fever Pitch and Fever Pitch. The first edition was subtitled A Fan's Life, but later paperback editions were not." \
           "</p>"


@app.route("/football-2/")
def enemy():
    return "<h1>Football Against the Enemy</h1>" \
           "<br>" \
           "<h2>Simon Kuper</h1>" \
           "<br>" \
           "<p>Football Against the Enemy is a book by Simon Kuper. It won the 1994 William Hill Sports Book of the Year award. In the United States, it was released as Soccer Against the Enemy.</p>"


@app.route("/football-3/")
def brilliant():
    return "<h1>Brilliant Orange: The Neurotic Genius of Dutch Football</h1>" \
           "<br>" \
           "<h2>David Winner</h2>" \
           "<br>" \
           "<p>Brilliant Orange: The Neurotic Genius of Dutch Football is a book by David Winner, first published in 2000. It looks at the development of football in the Netherlands from the 1960s onwards, and at how the footballing culture reflected changes in wider Dutch culture.</p>"


@app.route("/baseball-1/")
def ball():
    return "<h1>Ball Four</h1>" \
           "<br>" \
           "<h2>Jim Bouton and Leonard Shecter</h2>" \
           "<br>" \
           "<p>Ball Four is a book written by former Major League Baseball pitcher Jim Bouton in 1970. The book is a diary of Bouton's 1969 season, spent with the Seattle Pilots and then the Houston Astros following a late-season trade. In it, Bouton also recounts much of his baseball career, spent mainly with the New York Yankees.</p>"


@app.route("/baseball-2/")
def moneyball():
    return "<h1>Moneyball: The Art of Winning an Unfair Game</h1>" \
           "<br>" \
           "<h2>Michael Lewis</h1>" \
           "<br>" \
           "<p>Moneyball: The Art of Winning an Unfair Game is a book by Michael Lewis, published in 2003, about the Oakland Athletics baseball team and its general manager Billy Beane. Its focus is the team's analytical, evidence-based, sabermetric approach to assembling a competitive baseball team despite Oakland's small budget.</p>"


@app.route("/baseball-3/")
def summer():
    return "<h1>The Summer Game</h1>" \
           "<br>" \
           "<h2>Roger Angell</h2>" \
           "<br>" \
           "<p>This New York Times bestseller “takes you into the heart of baseball as it was in the 1960s, conveyed with humor and insight” (Tim McCarver, The Wall Street Journal).</p>"
