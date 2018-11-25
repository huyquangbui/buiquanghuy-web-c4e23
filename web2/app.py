import mlab
from data import Movie
from data import Resource
from faker import Faker
from random import randint

mlab.connect()
fake = Faker("en_GB")

# for _ in range(500):
#     print (fake.name())

# ----CREATE----
# m = Movie(title = "Badman", year = 2019, image = "http://images.moc-pages.com/user_images/10669/1213845245_SPLASH.jpg")
# m.save()

# r = Resource(name = "Jessica", city = "NY", yob = 1969, height = 172, weight = 70)
# r.save()

#----READ----
# movie_list = Movie.objects()

# for m in movie_list:
#     print(m.year)

# resource_list = Resource.objects()

# for r in resource_list:
#     print(r.name, r.city, r.yob, r.height, r.weight)

#----DELETE----
# m = Resource.objects().with_id("5bf7fc2df1d51e14ac348be2")
# print(m.name)
# m.delete()

# m1 = Resource.objects(0) #delete all
# m1.delete()

# m1 = Resource.objects() #SEARCH
# m1[0].delete()

# m1 = Resource.objects().first()
# m1.delete()

# for _ in range(100):
#     name = fake.name()
#     city = fake.city()
#     yob = randint(1953,2000)
#     height = randint(150,200)
#     weight = randint (40,150)
#     r = Resource( name = name, city = city, yob = yob, height = height, weight = weight)
#     r.save()

# rec = Resource.objects(name__icontains = "an")
# for r in rec:
#     print(r.name)
#     print(r.city)
#     print(r.yob)
#     print(r.height)
#     print(r.weight)

# rec = Resource.objects(height__lt = 170, name__icontains = "ma")
# i = 0
# for r in rec:
#     print(r.name, r.city, r.yob, r.height, r.weight, sep=", ")
#     i += 1
# print("tong cong:", i)

# ----UPDATE----
# rec = Resource.objects()
# for r in rec:
#     r.update(set__available = False)

rec1 = Resource.objects().with_id("5bf80cdaf1d51e1e3704c8b2")
rec1.update(set__available = True)