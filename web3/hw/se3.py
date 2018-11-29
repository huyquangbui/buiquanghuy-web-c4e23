import mlab
from data import VehicleInfo

mlab.connect()


bike = VehicleInfo.objects()
for b in bike:
    print(b.model)
    print(b.fee)
    print(b.image)
    print(b.year)
    print()
