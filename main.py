import requests

FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
CREDITS_LIST_PATH = "http://api.themoviedb.org/3/movie"
QUERY = "https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Jack+Reacher"
RELEASE_DATE = "2018-01-01"
BACON_ID = "4724"
PAUL_ID = "781"
WHALB_ID = "13240"

API_KEY = "a6ced572e0288192872a7ed83283261c"  # Your API key goes here or else the program will not work


def get_film_list(actor_id):
    params = {"api_key": API_KEY, "with_people": actor_id,
              "primary_release_date.gte": RELEASE_DATE}
    r = requests.get(url=FILM_LIST_PATH, params=params)
    data = r.json()
    return data


# end def get_film_list(actor_id):


def data_to_set(data):
    film_set = set()
    for res in data['results']:
        film_set.add(res['title'])
    return film_set


def get_cast_list(film_id):
    url = CREDITS_LIST_PATH + "/" + film_id + "/credits"
    params = {"api_key": API_KEY}
    r = requests.get(url=url, params=params)
    data = r.json()
    return data


# end def get_cast_list(film_id):


def find_actor_id(fname, lname):
    api_key = API_KEY
    url = "https://api.themoviedb.org/3/search/person?api_key={0}&language=en-US&page=1" \
          "&include_adult=false&query={1} {2}".format(api_key, fname, lname)
    r = requests.get(url=url)
    data = r.json()
    if data['total_results'] > 0:
        # return data['results'][0]['id'], data['results'][0]['name']
        actor_id = data['results'][0]['id']
        actor_name = data['results'][0]['name']
        print(".......................................................................................................")
        print(f"Here's the search result for {actor_name} who has an actor's ID: {actor_id}")
        print(".......................................................................................................")
    else:
        print(".......................................................................................................")
        print("Couldn't find the person. Check the name and try again")
        print(".......................................................................................................")


def compare_actors(id_1, id_2):
    actor_1_movies = data_to_set(get_film_list(id_1))
    actor_2_movies = data_to_set(get_film_list(id_2))
    common_films = actor_1_movies & actor_2_movies
    if len(common_films) > 0:
        print(f"Both actors appeared in the movie '{common_films}'.")
    else:
        print("No current films in common")


def handle_find_actor():
    print("===========================================================================================================")
    print("You can find an actor's ID by typing the actors firstname and lastname, one after the other.")
    first_name = input("Enter the actor's FirstName: ")
    last_name = input("Enter the actor's LastName: ")
    find_actor_id(first_name, last_name)
    print("===========================================================================================================")


def handle_compare_actors():
    print("===========================================================================================================")
    print("You can compare two actors by typing their IDs one after the other")
    first_id = input("Enter actor one's ID: ")
    second_id = input("Enter actor two's ID: ")
    compare_actors(first_id, second_id)
    print("===========================================================================================================")


def main():
    prompt = input("============================================================================================"
                   "==================================================================== \n"
                   "To find an actor's ID, reply by typing 1 \n"
                   "To compare two actors, reply by typing 2 \n"
                   "============================================================================================"
                   "==================================================================== \n: ")
    if prompt == "1":
        handle_find_actor()
    elif prompt == "2":
        handle_compare_actors()
    else:
        print("Invalid input")


# end def main:


if __name__ == "__main__":
    main()
