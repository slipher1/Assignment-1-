"This is the first assignment project from reseach and implemenation, Micheal Smurfit UCD. Author Conor Shiel"
In [1]:
import sqlite3
In [ ]:
 
In [2]:
pwd
Out[2]:
u'C:\\Users\\darragh\\Documents\\Python workings'
In [3]:
conn = sqlite3.connect('renewable.db')# creates connection 
import pandas as pd 
locations = pd.read_sql_query("SELECT * FROM location", conn)
print locations 
    long   lat  production trips  trip
0  52.66  7.26      259696  None  None
1  52.86  8.99       89499  None  None
2  54.28  8.48      271650  None  None
3  53.42  7.95       87606  None  None
4  52.34  6.48      298978  None  None
5  53.22  6.68      200068  None  None
6  52.36  7.71       60573  None  None
7  52.84  6.92      159794  None  None
8  53.18  6.80      163358  None  None
9  53.66  6.69      210817  None  None
In [7]:
list_location_long=[]
c = conn.cursor()
for i in c.execute("SELECT long FROM location;"):
    list_location_long.append(i)
    
print list_location_long
[(52.66,), (52.86,), (54.28,), (53.42,), (52.34,), (53.22,), (52.36,), (52.84,), (53.18,), (53.66,)]
In [47]:
list_location_production=[]
h = c.execute("SELECT production FROM location")
for i in h:
    list_location_production.append(i)
print list_location_production
    
    
                
[(259696.0,), (89499.0,), (271650.0,), (87606.0,), (298978.0,), (200068.0,), (60573.0,), (159794.0,), (163358.0,), (210817.0,)]
In [11]:
list_location_lat=[]
for i in c.execute("SELECT lat FROM location;"):
    list_location_lat.append(i)
print list_location_lat
[(7.26,), (8.99,), (8.48,), (7.95,), (6.48,), (6.68,), (7.71,), (6.92,), (6.8,), (6.69,)]
In [12]:
ports = pd.read_sql_query("SELECT * FROM ports", conn)
print ports
    long   lat
0  52.70  8.63
1  53.33  6.25
2  52.27  6.39
In [13]:
list_port_long=[]
for i in c.execute("SELECT long FROM ports"):
    list_port_long.append(i)
print list_port_long
[(52.7,), (53.33,), (52.27,)]
In [15]:
list_port_lat=[]
for i in c.execute("SELECT lat FROM ports"):
    list_port_lat.append(i)
print list_port_lat
[(8.63,), (6.25,), (6.39,)]
In [92]:
list_location_production1=[259696.0, 89499.0, 271650.0, 87606.0, 298978.0, 200068.0, 60573.0, 159794.0, 163358.0,210817.0]
trips=[]
for i in list_location_production1:
    result = i/40
    trips.append(result)
print trips
trips_1 ={0:6492.4,1: 2237.475, 2:6791.25,3: 2190.15,4: 7474.45,5: 5001.7, 6:1514.325, 7:3994.85, 8:4083.95,9: 5270.425}
print trips_1
[6492.4, 2237.475, 6791.25, 2190.15, 7474.45, 5001.7, 1514.325, 3994.85, 4083.95, 5270.425]
{0: 6492.4, 1: 2237.475, 2: 6791.25, 3: 2190.15, 4: 7474.45, 5: 5001.7, 6: 1514.325, 7: 3994.85, 8: 4083.95, 9: 5270.425}
In [54]:
from math import radians, cos, sin, asin, sqrt

def length_km(lon1, lat1, lon2, lat2): #calculates the distance of two geographical points .
    
     
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) #convert decimal degrees to radians 
    # haversine formula 
    dlon = lon2 - lon1 #difference in longitudes
    dlat = lat2 - lat1 #difference in latitude
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return "%0.2lf" % km

print "\n"

In [55]:
print length_km(52.66,7.26,52.86,8.99)
193.50
In [ ]:
In [57]:
list_location_long=[52.66,52.86, 54.28, 53.42, 52.34, 53.22, 52.36, 52.84, 53.18, 53.66]
list_location_lat=[7.26, 8.99, 8.48, 7.95, 6.48, 6.68, 7.71, 6.92, 6.8, 6.69]
list_port_long=[52.7,53.33,52.27]
list_port_lat=[8.63,6.25,6.39]
In [61]:
location_0_ports_dist=[]# The distance from location 0 to all of the ports. The same has been repeated for all the locations. 
for i in range(0,3):
        location_0_ports_dist.append(length_km(list_location_long[0],list_location_lat[0],list_port_long[i],list_port_lat[i]))
print location_0_ports_dist
['152.31', '134.40', '105.82']
In [62]:
location_1_ports_dist=[]
for i in range(0,3):
        location_1_ports_dist.append(length_km(list_location_long[1],list_location_lat[1],list_port_long[i],list_port_lat[i]))
print location_1_ports_dist
['43.69', '308.85', '296.14']
In [63]:
location_2_ports_dist=[]
for i in range(0,3):
        location_2_ports_dist.append(length_km(list_location_long[2],list_location_lat[2],list_port_long[i],list_port_lat[i]))
print location_2_ports_dist
['174.42', '269.02', '320.92']
In [64]:
location_3_ports_dist=[]
for i in range(0,3):
        location_3_ports_dist.append(length_km(list_location_long[3],list_location_lat[3],list_port_long[i],list_port_lat[i]))
print location_3_ports_dist
['109.45', '189.17', '214.77']
In [66]:
location_4_ports_dist=[]
for i in range(0,3):
        location_4_ports_dist.append(length_km(list_location_long[4],list_location_lat[4],list_port_long[i],list_port_lat[i]))
print location_4_ports_dist
['242.19', '112.28', '12.64']
In [67]:
location_5_ports_dist=[]
for i in range(0,3):
        location_5_ports_dist.append(length_km(list_location_long[5],list_location_lat[5],list_port_long[i],list_port_lat[i]))
print location_5_ports_dist
['224.13', '49.30', '109.72']
In [68]:
location_6_ports_dist=[]
for i in range(0,3):
        location_6_ports_dist.append(length_km(list_location_long[6],list_location_lat[6],list_port_long[i],list_port_lat[i]))
print location_6_ports_dist
['108.86', '194.34', '147.02']
In [69]:
location_7_ports_dist=[]
for i in range(0,3):
        location_7_ports_dist.append(length_km(list_location_long[7],list_location_lat[7],list_port_long[i],list_port_lat[i]))
print location_7_ports_dist
['190.65', '92.03', '86.18']
In [70]:
location_8_ports_dist=[]
for i in range(0,3):
        location_8_ports_dist.append(length_km(list_location_long[8],list_location_lat[8],list_port_long[i],list_port_lat[i]))
print location_8_ports_dist
['210.12', '63.32', '110.30']
In [71]:
location_9_ports_dist=[]
for i in range(0,3):
        location_9_ports_dist.append(length_km(list_location_long[9],list_location_lat[9],list_port_long[i],list_port_lat[i]))
print location_9_ports_dist
['240.11', '60.98', '157.04']
In [91]:
location_0_location=[]# The distance from 0 to all the loactions. The same has been repeated for all the locations. 
for i in range(0,10):
    if i !=0:
        location_0_location.append(length_km(list_location_long[0],list_location_lat[0],list_location_long[i],list_location_lat[i]))


dist_location_0 ={1:193.50, 2:224.01, 3:113.52, 4:93.59,5:89.27 ,6:59.94, 7: 42.68, 8:76.83, 9:76.83 }
print dist_location_0
{1: 193.5, 2: 224.01, 3: 113.52, 4: 93.59, 5: 89.27, 6: 59.94, 7: 42.68, 8: 76.83, 9: 76.83}
In [102]:
location_1_location=[]
for i in range(0,10):
    if i !=1:
        location_1_location.append(length_km(list_location_long[1],list_location_lat[1],list_location_long[i],list_location_lat[i]))

location_1_location ={0:193.50, 2:165.94, 3:130.94, 4:284.74, 5:259.74, 6:152.49, 7:230.04, 8:245.90, 9:270.33}
print location_1_location
{0: 193.5, 2: 165.94, 3: 130.94, 4: 284.74, 5: 259.74, 6: 152.49, 7: 230.04, 8: 245.9, 9: 270.33}
In [103]:
location_2_location=[]
for i in range(0,10):
    if i !=2:
        location_2_location.append(length_km(list_location_long[2],list_location_lat[2],list_location_long[i],list_location_lat[i]))
        
location_2_location = {0:224.01, 1:165.94, 3:111.42, 4:308.35, 5:231.61, 6:227.91, 7:234.94, 8:222.55, 9:210.31}
print location_2_location
{0: 224.01, 1: 165.94, 3: 111.42, 4: 308.35, 5: 231.61, 6: 227.91, 7: 234.94, 8: 222.55, 9: 210.31}
In [105]:
location_3_location=[]
for i in range(0,10):
    if i !=3:
        location_3_location.append(length_km(list_location_long[3],list_location_lat[3],list_location_long[i],list_location_lat[i]))

location_3_location={0:113.52, 1:130.94, 2:111.42, 4:202.14, 5:142.84, 6:119.70, 7:131.09, 8:130.50, 9:142.49}
print location_3_location
{0: 113.52, 1: 130.94, 2: 111.42, 4: 202.14, 5: 142.84, 6: 119.7, 7: 131.09, 8: 130.5, 9: 142.49}
In [106]:
location_4_location=[]
for i in range(0,10):
    if i !=4:
        location_4_location.append(length_km(list_location_long[4],list_location_lat[4],list_location_long[i],list_location_lat[i]))


location_4_location = {0:93.59, 1:284.74, 2:308.35, 3:202.14, 5:99.66, 6:136.70, 7:73.73, 8:99.30, 9:147.57}
print location_4_location
{0: 93.59, 1: 284.74, 2: 308.35, 3: 202.14, 5: 99.66, 6: 136.7, 7: 73.73, 8: 99.3, 9: 147.57}
In [107]:
location_5_location=[]
for i in range(0,10):
    if i !=5:
        location_5_location.append(length_km(list_location_long[5],list_location_lat[5],list_location_long[i],list_location_lat[i]))


location_5_location ={0:89.27, 1:259.74, 2:231.61, 3:142.84, 4:99.66, 6:148.63, 7:49.69, 8:14.05, 9:48.58}
print location_5_location
{0: 89.27, 1: 259.74, 2: 231.61, 3: 142.84, 4: 99.66, 6: 148.63, 7: 49.69, 8: 14.05, 9: 48.58}
In [108]:
location_6_location=[]
for i in range(0,10):
    if i !=6:
        location_6_location.append(length_km(list_location_long[6],list_location_lat[6],list_location_long[i],list_location_lat[i]))


location_6_location={0:59.94, 1:152.49, 2:227.91, 3:119.70, 4:136.70, 5:148.63, 7:102.50, 8:135.63, 9:182.73}
print location_6_location
{0: 59.94, 1: 152.49, 2: 227.91, 3: 119.7, 4: 136.7, 5: 148.63, 7: 102.5, 8: 135.63, 9: 182.73}
In [112]:
location_7_location=[]
for i in range(0,10):
    if i !=7:
        location_7_location.append(length_km(list_location_long[7],list_location_lat[7],list_location_long[i],list_location_lat[i]))


location_7_location = {0:42.68, 1:230.04, 2:234.94, 3:131.09, 4:73.73, 5:49.69, 6:102.50, 8:39.81, 9:94.02}
print location_7_location
{0: 42.68, 1: 230.04, 2: 234.94, 3: 131.09, 4: 73.73, 5: 49.69, 6: 102.5, 8: 39.81, 9: 94.02}
In [113]:
location_8_location=[]
for i in range(0,10):
    if i !=8:
        location_8_location.append(length_km(list_location_long[8],list_location_lat[8],list_location_long[i],list_location_lat[i]))

location_8_location = {0:76.83, 1:245.90, 2:222.55, 3:130.50, 4:99.30, 5:14.05, 6:135.63, 7:39.81, 9:54.36}
print location_8_location
{0: 76.83, 1: 245.9, 2: 222.55, 3: 130.5, 4: 99.3, 5: 14.05, 6: 135.63, 7: 39.81, 9: 54.36}
In [114]:
location_9_location=[]
for i in range(0,10):
    if i !=9:
        location_9_location.append(length_km(list_location_long[9],list_location_lat[9],list_location_long[i],list_location_lat[i]))


location_9_location={0:127.20, 1:270.33, 2:210.31, 3:142.49, 4:147.57, 5:48.58, 6:182.73, 7:94.02, 8:54.36}
print location_9_location
{0: 127.2, 1: 270.33, 2: 210.31, 3: 142.49, 4: 147.57, 5: 48.58, 6: 182.73, 7: 94.02, 8: 54.36}
In [98]:
def mult_dicts(dict1, dict2):# This function multiplies the numnber of trips that will have to be made from a plant.
  result_dict = {} # by the distance they will have to travel to the other. 
  for word in dict1:
    if word in dict2:
      result_dict[word] = dict1[word] * dict2[word]
  return result_dict
distance_traveled_to_location_0= mult_dicts(trips_1,dist_location_0)
print distance_traveled_to_location_0
{1: 432951.4125, 2: 1521307.9124999999, 3: 248625.828, 4: 699533.7755, 5: 446501.75899999996, 6: 90768.6405, 7: 170500.198, 8: 313769.8785, 9: 404926.75275}
In [101]:
def sum_dict(x): # This function sums the transport distance from the other locations. 
    result = 0.0
    for i in x: 
        result+=x[i]
    return result 
total_distance_tavelled_to_0= sum_dict(distance_traveled_to_location_0)
km_total_0 =  total_distance_tavelled_to_0 + float(location_0_ports_dist[2])
print km_total_0 #Total number for location 0 + the closest port.
4328991.97725
In [118]:
distance_traveled_to_location_1= mult_dicts(trips_1,location_1_location)
print distance_traveled_to_location_1
{0: 1256279.4, 2: 1126940.025, 3: 286778.241, 4: 2128274.893, 5: 1299141.558, 6: 230919.41925, 7: 918975.294, 8: 1004243.3049999999, 9: 1424753.99025}
In [119]:
total_distance_tavelled_to_1= sum_dict(distance_traveled_to_location_1)
In [120]:
km_total_1 =  total_distance_tavelled_to_1 + float(location_1_ports_dist[0])
In [121]:
print km_total_1 # Total number for location 1 + the closest port
9676349.8155
In [123]:
distance_traveled_to_location_2= mult_dicts(trips_1,location_2_location)
total_distance_tavelled_to_2= sum_dict(distance_traveled_to_location_2)
km_total_2 =  total_distance_tavelled_to_2 + float(location_2_ports_dist[0])
print km_total_2 # Total distance for location 2 + the closest port.
8834026.477
In [131]:
distance_traveled_to_location_3= mult_dicts(trips_1,location_3_location)
print distance_traveled_to_location_3
total_distance_tavelled_to_3= sum_dict(distance_traveled_to_location_3)
print total_distance_tavelled_to_3
km_total_3 =  total_distance_tavelled_to_3 + float(location_3_ports_dist[0])
print km_total_3
{0: 737017.2479999999, 1: 292974.9765, 2: 756681.075, 4: 1510885.3229999999, 5: 714442.828, 6: 181264.7025, 7: 523684.8865, 8: 532955.475, 9: 750982.85825}
6000889.37275
6000998.82275
In [125]:
distance_traveled_to_location_3= mult_dicts(trips_1,location_3_location)
total_distance_tavelled_to_3= sum_dict(distance_traveled_to_location_3)
km_total_3 =  total_distance_tavelled_to_3 + float(location_3_ports_dist[0])
print km_total_3 # Total distance for location 3 + the closest port.
6000998.82275
In [138]:
distance_traveled_to_location_4= mult_dicts(trips_1,location_4_location)
print distance_traveled_to_location_4
total_distance_tavelled_to_4= sum_dict(distance_traveled_to_location_4)
print total_distance_tavelled_to_4
km_total_4 =  total_distance_tavelled_to_4 + float(location_4_ports_dist[2])
print km_total_4 # Total distance for location 4 + the closest port.
{0: 607623.716, 1: 637098.6315, 2: 2094081.9375000002, 3: 442716.921, 5: 498469.42199999996, 6: 207008.22749999998, 7: 294540.2905, 8: 405536.235, 9: 777756.61725}
5964831.99825
5964844.63825
In [135]:
distance_traveled_to_location_5= mult_dicts(trips_1,location_5_location)
print distance_traveled_to_location_5
total_distance_tavelled_to_5= sum_dict(distance_traveled_to_location_5)
km_total_5 =  total_distance_tavelled_to_5 + float(location_5_ports_dist[1])
print km_total_5 # Total distance for location 5 + the closest port.
{0: 579576.548, 1: 581161.7565, 2: 1572921.4125, 3: 312841.026, 4: 744903.6869999999, 6: 225074.12475, 7: 198504.09649999999, 8: 57379.4975, 9: 256037.2465}
4528448.69525
In [136]:
distance_traveled_to_location_6= mult_dicts(trips_1,location_6_location)
total_distance_tavelled_to_6= sum_dict(distance_traveled_to_location_6)
km_total_6 =  total_distance_tavelled_to_6 + float(location_6_ports_dist[0])
print km_total_6 # Total distance for location 6 + the closest port.
6232013.631
In [139]:
distance_traveled_to_location_7= mult_dicts(trips_1,location_7_location)
total_distance_tavelled_to_7= sum_dict(distance_traveled_to_location_7)
km_total_7 =  total_distance_tavelled_to_7 + float(location_7_ports_dist[2])
print km_total_7 # Total distance for location 7 + the closest port.
4287484.9915
In [140]:
distance_traveled_to_location_8= mult_dicts(trips_1,location_8_location)
total_distance_tavelled_to_8= sum_dict(distance_traveled_to_location_8)
km_total_8 =  total_distance_tavelled_to_8 + float(location_8_ports_dist[1])
print km_total_8 # Total distance for location 8 + the closest port.
4309686.72825
In [141]:
distance_traveled_to_location_9= mult_dicts(trips_1,location_9_location)
total_distance_tavelled_to_9= sum_dict(distance_traveled_to_location_9)
km_total_9 =  total_distance_tavelled_to_9 + float(location_9_ports_dist[1])
print km_total_9 # Total distance for location 9 + the closest port.
5391392.2365
In [142]:
print km_total_0
print km_total_1
print km_total_2
print km_total_3
print km_total_4
print km_total_5
print km_total_6
print km_total_7
print km_total_8
print km_total_9
4328991.97725
9676349.8155
8834026.477
6000998.82275
5964844.63825
4528448.69525
6232013.631
4287484.9915
4309686.72825
5391392.2365
In [146]:
H = [km_total_0,km_total_1,km_total_2,km_total_3,km_total_4,km_total_5,km_total_6,km_total_7,km_total_8,km_total_9]
smallest = None 
for item in H:
    print item
    if (smallest == None) or (item < smallest):
        smallest = item
print "smallest = ", smallest #There for the cheapest area to produce would be km_total_7 which has:
# a longitude of 52.84 and a latitude of 6.92 and a total production of 159,794tonnes.
4328991.97725
9676349.8155
8834026.477
6000998.82275
5964844.63825
4528448.69525
6232013.631
4287484.9915
4309686.72825
5391392.2365
smallest =  4287484.9915