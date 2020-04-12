def Posts():
    posts = [
        {
            'id': 1,
            'title': 'Man must explore, and this is exploration at its greatest',
            'body': 'Problems look mighty small from 150 miles up',
            'author': 'Eko Teguh Widodo',
            'create_date': '2020-04-11'
        },
        {
            'id': 2,
            'title': 'Science has not yet mastered prophecy',
            'body': 'We predict too much for the next year and yet far too little for the next ten.',
            'author': 'Eko Teguh Widodo',
            'create_date': '2020-04-10'
        },
        {
            'id': 3,
            'title': 'Failure is not an option',
            'body': 'Many say exploration is part of our destiny, but it’s actually our duty to future generations.',
            'author': 'Eko Teguh Widodo',
            'create_date': '2020-04-09'
        }
    ]

    return posts

def Post(id):
    posts = [
        {
            'id': 1,
            'title': 'Man must explore, and this is exploration at its greatest',
            'body': 'Problems look mighty small from 150 miles up',
            'author': 'Eko Teguh Widodo',
            'create_date': '2020-04-11'
        },
        {
            'id': 2,
            'title': 'Science has not yet mastered prophecy',
            'body': 'We predict too much for the next year and yet far too little for the next ten.',
            'author': 'Eko Teguh Widodo',
            'create_date': '2020-04-10'
        },
        {
            'id': 3,
            'title': 'Failure is not an option',
            'body': 'Many say exploration is part of our destiny, but it’s actually our duty to future generations.',
            'author': 'Eko Teguh Widodo',
            'create_date': '2020-04-09'
        }
    ]

    post = {}
    for p in posts:
        if int(p['id']) == int(id):
            post = p
    
    return post
        
    