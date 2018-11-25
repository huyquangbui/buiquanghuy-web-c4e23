import mlab
from data import River

mlab.connect()

# se2
# river_list = River.objects(continent__icontains = "Africa")
# for r in river_list:
#     print(r.name, r.continent, r.length)

# se3
river_list = River.objects(continent__icontains = "S. America", length__lt = 1000)
for r in river_list:
    print(r.name, r.continent, r.length)