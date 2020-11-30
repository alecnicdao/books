from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse/')
def browse():
    return render_template('browse.html')

@app.route('/genre/<category>')
def category(category):
    cat = content['category'][category]
    return render_template('category.html', genre=cat['genre'], genreDesc=cat['genreDesc'], books=cat['books'])

@app.route('/books/<book>')
def book(book):
    theBook = content['book'][book]
    if 'subtitle' in theBook:
        return render_template('book.html', title=theBook['title'], subtitle=theBook['subtitle'], author=theBook['author'], description=theBook['description'])
    else:
        return render_template('book.html', title=theBook['title'], author=theBook['author'], description=theBook['description'])

content = {
    'category': {
        'sportsfiction': {
            'genre': 'Sports Fiction',
            'genreDesc': 'A sports novel is a literary genre that focuses on the theme of sports and athletics in general.',
            'books': [
                { 'title': 'The Crossover', 'route': 'the-crossover' },
                { 'title': 'Last Shot: A Final Four Mystery', 'route': 'lastShot' },
                { 'title': 'Friday Night Lights: A Town, a Team, and a Dream', 'route': 'friday-night-lights' }
            ]
        },
        'scifi': {
            'genre': 'Science Fiction',
            'genreDesc': 'Science fiction is a genre of speculative fiction that typically deals with imaginative and futuristic concepts such as advanced science and technology, space exploration, time travel, parallel universes, and extraterrestrial life.',
            'books': [
                { 'title': 'Dune', 'route': 'dune' },
                { 'title': 'The Left Hand of Darkness', 'route': 'left-darkness' },
                { 'title': 'Neuromancer', 'route': 'neuromancer' }
            ]
        },
        'mystery': {
            'genre': 'Mystery',
            'genreDesc': 'Mystery fiction is a genre of fiction that usually involves a mysterious death or a crime to be solved. Often within a closed circle of suspects, each suspect is usually provided with a credible motive and a reasonable opportunity for committing the crime.',
            'books': [
                { 'title': 'The Sentinel', 'route': 'sentinel' },
                { 'title': 'Troubled Blood', 'route': 'troubled-blood' },
                { 'title': 'Fortune and Glory: A Novel', 'route': 'fortune-glory' }
            ]
        }
    },
    'book': {
        'the-crossover': {
            'title': 'The Crossover',
            'subtitle': 'Page count: 240',
            'author': 'Kwame Alexander',
            'description': 'The Crossover is a 2015 childrens book by American author Kwame Alexander and the winner of the 2015 Newbery Medal and Coretta Scott King Award Honor. The book, which is told entirely through verse, was first published in the United States in hardback on March 18, 2014 through HMH Books for Young Readers.'
        },
        'lastShot': {
            'title': 'Last Shot: A Final Four Mystery',
            'subtitle': 'Page count: 272',
            'author': 'John Feinstein',
            'description': 'Last Shot: A Final Four Mystery is a young adult novel by John Feinstein. It tells the story of two young reporters, Stevie Thomas and Susan Carol Anderson, who stumble upon a plot to blackmail fictional Minnesota State basketball player Chip Graber into throwing the Final Four in New Orleans.'
        },
        'friday-night-lights': {
            'title': 'Friday Night Lights: A Town, a Team, and a Dream',
            'subtitle': 'Page count: 419',
            'author': 'Buzz Bissinger',
            'description': 'Friday Night Lights: A Town, a Team, and a Dream is a 1990 non-fiction book written by H. G. Bissinger. The book follows the story of the 1988 Permian High School Panthers football team from Odessa, Texas, as they made a run towards the Texas state championship.'
        },
        'dune': {
            'title': 'Dune',
            'subtitle': 'Page count: 412',
            'author': 'Frank Herbert',
            'description': 'Dune is a 1965 science-fiction novel by American author Frank Herbert, originally published as two separate serials in Analog magazine. It tied with Roger Zelaznys This Immortal for the Hugo Award in 1966, and it won the inaugural Nebula Award for Best Novel..'
        },
        'left-darkness': {
            'title': 'The Left Hand Darkness',
            'subtitle': 'Page count: 286',
            'author': 'Ursula K. Le Guin',
            'description': 'The Left Hand of Darkness is a science fiction novel by U.S. writer Ursula K. Le Guin. Published in 1969, it became immensely popular, and established Le Guins status as a major author of science fiction.'
        },
        'neuromancer': {
            'title': 'Neuromancer',
            'subtitle': 'Page count: 271',
            'author': 'William Gibson',
            'description': 'Neuromancer is a 1984 science fiction novel by American-Canadian writer William Gibson. It is one of the best-known works in the cyberpunk genre and the first novel to win the Nebula Award, the Philip K. Dick Award, and the Hugo Award. It was Gibsons debut novel and the beginning of the Sprawl trilogy.'
        },
        'sentinel': {
            'title': 'The Sentinel',
            'subtitle': 'Page count: 260',
            'author': 'Lee Child',
            'description': 'The Sentinel is the 25th novel in the Jack Reacher series and was published on October 27, 2020. It is the first Jack Reacher book to be co-authored by James Grant and his younger brother Andrew Grant but published using their respective pen names of Lee Child and Andrew Child.'
        },
        'troubled-blood': {
            'title': 'Troubled Blood',
            'subtitle': 'Page count: 941',
            'author': 'J.K. Rowling',
            'description': 'Troubled Blood is the fifth novel in the Cormoran Strike series, written by J. K. Rowling and published under the pseudonym Robert Galbraith. The novel was released on 15 September 2020.'
        },
        'fortune-glory': {
            'title': 'Fortune and Glory: A Novel',
            'subtitle': 'Page count: 316',
            'author': 'Janet Evanovich',
            'description': 'Fortune and Glory is the highly anticipated 27th book in Janet Evanovich’s #1 New York Times bestselling Stephanie Plum series!When Stephanie’s beloved Grandma Mazurs new husband died on their wedding night, the only thing he left her was a beat-up old easy chair…and the keys to a life-changing fortune.'
        }
    }
}