import sys

if __name__ == "__main__":
    # python searches location of invoked script
    # if run as standalone script (not thru django) need to add project to python path
    proj_root = "/home/rona/projects/moshimoji-backend/graphene-django-backend/"
    sys.path.append(proj_root)
    # also need to set Django config, models, and app context
    import config.wsgi

from project.gql_platform.models.content.serialization.comic import Genre

genre_list = [
    'Action',
    'Adventure',
    'Comedy',
    'Drama',
    'Fantasy',
    'Historical',
    'Horror',
    'Josei',
    'Mystery',
    'Psychological',
    'Romance',
    'Sci-fi',
    'Seinen',
    'Shoujo',
    'Shounen',
    'Slice of Life',
    'Sports',
    'Supernatural',
    'Tragedy'
]

def generate_genres():
    for genre in genre_list:
        if not Genre.objects.filter(name=genre):
            Genre.objects.create(name=genre)

def main():
    generate_genres()

if __name__ == "__main__":
    main()
