
# Movie [id,title,genre,language,run_time]
# add_movie
# list_movie
# update
# delete


class Movie:

    def __init__(self):

        self.filims=[]

    def post(self,**kwargs):#{id:1,title:"kgf","genre":"action","lan"}

        self.filims.append(kwargs)

        print("movie has been added")

    def get(self):

        print(self.filims)

    def retrieve(self,id=None):

        data = [m for m in self.filims if m["id"] == id][0]

        print(data)

    def put(self,id=None,**kwargs):

        movie = [m for m in self.filims if m["id"]==id][0]
        movie.update(kwargs)

        print("movie has been updated................")

    def delete(self,id=None):

        movie = [m for m in self.filims if m["id"]==id][0]

        self.filims.remove(movie)

        print("movie has been deleted..........")





       


movie_instance = Movie()

movie_instance.post(id=1,title="kgf",genre="action",language="telungu",run_time=160)
movie_instance.post(id=2,title="kgf2",genre="action",language="telungu",run_time=160)
movie_instance.post(id=3,title="drisyam",genre="drama",language="malayalam",run_time=120)

movie_instance.put(id=3,genre="thriller",run_time=140)

# movie_instance.retrieve_movie(id=3)

movie_instance.delete(id=2)
movie_instance.get()



# create a simple crud application of CalorieTracker application
# -should have  {id:,title:,meal_type,calorie}
# add_foodlog()
# list_foodlog()
# retrive_foodlog()
# update_foodlog()
# destroy_foodlog()

