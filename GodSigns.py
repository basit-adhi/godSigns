"""
See: https://bptsi.unisayogya.ac.id/fussilat-53/#Fun-Fact
"""

from openlocationcode import openlocationcode as olc_lib
import math


def plus_code_to_lat_lon(plus_code):
    """
    Converts a Plus Code to its corresponding latitude and longitude.
    """
    try:
        decoded_code = olc_lib.decode(plus_code)
        
        return decoded_code.latitudeCenter, decoded_code.longitudeCenter
    except ValueError:
        print(f"Error: Invalid Plus Code '{plus_code}'")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during decoding: {e}")
        return None
    
    
def calculate_bearing_plus_code(plus_code1, plus_code2, log=True, rounding=200):
    """
    Calculates the bearing from a starting point to a destination point, using plus code.
    """    
    lat1, lon1 = plus_code_to_lat_lon(plus_code1.PLUSCODE_)
    lat2, lon2 = plus_code_to_lat_lon(plus_code2.PLUSCODE_)
    if log :
        print("\n++++++++++++++++++++++++++++++++++++")
        print(f"{plus_code1.NAME_}: {plus_code1.PLUSCODE_} {lat1}, {lon1} ({math.radians(lat1)} rad, {math.radians(lon1)} rad )")
        print(f"{plus_code2.NAME_}: {plus_code2.PLUSCODE_} {lat2}, {lon2} ({math.radians(lat2)} rad, {math.radians(lon2)} rad )")
        print("++++++++++++++++++++++++++++++++++++")
    return calculate_bearing(plus_code1.NAME_, plus_code2.NAME_, lat1, lon1, lat2, lon2, log, rounding)


def calculate_bearing(label1, label2, lat1, lon1, lat2, lon2, log=True, rounding=200):
    """
    Calculates the bearing from a starting point to a destination point.
    """

    # Convert degrees to radians
    lat1_rad = round(math.radians(lat1), rounding)
    lon1_rad = round(math.radians(lon1), rounding)
    lat2_rad = round(math.radians(lat2), rounding)
    lon2_rad = round(math.radians(lon2), rounding)

    delta_lon = round(lon2_rad - lon1_rad, rounding)

    x = round(round(math.sin(delta_lon), rounding) * round(math.cos(lat2_rad), rounding), rounding)
    y = round(round(math.cos(lat1_rad), rounding) * round(math.sin(lat2_rad), rounding) - round(math.sin(lat1_rad), rounding) * round(math.cos(lat2_rad), rounding) * round(math.cos(delta_lon), rounding), rounding)
    if log :
        print(f"x = math.sin({delta_lon}) * math.cos({lat2_rad})")
        print(f"x = {round(math.sin(delta_lon), rounding)} * {round(math.cos(lat2_rad), rounding)}")
        print(f"x = {x}")
        print(f"y = math.cos({lat1_rad}) * math.sin({lat2_rad}) - math.sin({lat1_rad}) * math.cos({lat2_rad}) * math.cos({delta_lon})")
        print(f"y = {round(math.cos(lat1_rad), rounding)} * {round(math.sin(lat2_rad), rounding)} - {round(math.sin(lat1_rad), rounding)} * {round(math.cos(lat2_rad), rounding)} * {round(math.cos(delta_lon), rounding)}")
        print(f"y = {y}")
        
    initial_bearing = round(math.atan2(x, y), rounding)

    # Convert bearing from radians to degrees
    initial_bearing_deg = round(math.degrees(initial_bearing), rounding)
    if log :
        print(f"Initial Bearing: \nmath.atan2({x}, {y}) = {initial_bearing} rad = {initial_bearing_deg} degrees")
        
    # Normalize bearing to a 0-360 degree range
    compass_bearing = round((initial_bearing_deg + 360) % 360, rounding)
    if log :
        print(f"Normalized Bearing: \n{compass_bearing} degrees")
    return compass_bearing

class MapPoint:
    NAME_       = ""
    PLUSCODE_   = ""
    
    
#makkah boundary
nearMainGate = MapPoint()
nearMainGate.NAME_     = "Haram Border [Near Main Gate (W)]"
nearMainGate.PLUSCODE_ = "7GHX9J2P+W4V"

MainGate = MapPoint()
MainGate.NAME_     = "Haram Border [Main Gate (W)]"
MainGate.PLUSCODE_ = "7GHX9M68+WP"

Hudaibiyah = MapPoint()
Hudaibiyah.NAME_     = "Haram Border [Al Hudaibiyah (NW)]"
Hudaibiyah.PLUSCODE_ = "7GHXCJJW+7W"

Taneem = MapPoint()
Taneem.NAME_     = "Haram Border [Near Masjid Aisha 'Umm al-Mumineen' (Masjid Al-Taneem) (N)]"
Taneem.PLUSCODE_ = "7GHXFR82+JC"

Kaaba = MapPoint()
Kaaba.NAME_     = "Kaaba"
Kaaba.PLUSCODE_ = "7GHXCRFG+2F"

#aproximately south of Saud Al Ruwais mosque God's mercy, GWMR+V2X, Al Ju'ranah 24434, Arab Saudi
Juranah = MapPoint()
Juranah.NAME_     = "Haram Border [Al Ju'ranah (E}']"
Juranah.PLUSCODE_ = "7GHXGWJQ+FHP"

Rashidiya = MapPoint()
Rashidiya.NAME_     = "Haram Border [Rashidiya (E)]"
Rashidiya.PLUSCODE_ = "7GHXFWPR+4JW"

#miqot
MasjidHudaibiyah = MapPoint()
MasjidHudaibiyah.NAME_     ="Miqot [Masjid Hudaibiyah NW]"
MasjidHudaibiyah.PLUSCODE_ = "7GHXCJRG+Q7X"

MasjidJironah = MapPoint()
MasjidJironah.NAME_     = "Miqot [Masjid Ji'ronah (NE)]"
MasjidJironah.PLUSCODE_ = "7GHXHX92+8F"


#mount sinai
JabalMoses = MapPoint()
JabalMoses.NAME_     = "Jabal Musa" 
JabalMoses.PLUSCODE_ = "7GWMGXQG+C3"

JabalSerbal = MapPoint()
JabalSerbal.NAME_     = "Jabal Serbal"
JabalSerbal.PLUSCODE_ = "7GWMJMW2+HM"


loc_ = JabalMoses
rounding_ = 4
rounding_result_ = 2
cb1 = calculate_bearing_plus_code(nearMainGate, JabalMoses, True, rounding_)
cb2 = calculate_bearing_plus_code(MainGate, JabalMoses, True, rounding_)
cb3 = calculate_bearing_plus_code(Hudaibiyah, JabalMoses, True, rounding_)
cb4 = calculate_bearing_plus_code(Taneem, JabalMoses, True, rounding_)
cb5 = calculate_bearing_plus_code(Kaaba, JabalMoses, True, rounding_)
cb6 = calculate_bearing_plus_code(Juranah, JabalMoses, True, rounding_)
cb7 = calculate_bearing_plus_code(Rashidiya, JabalMoses, True, rounding_)

mq1 = calculate_bearing_plus_code(MasjidHudaibiyah, JabalMoses, True, rounding_)
mq2 = calculate_bearing_plus_code(MasjidJironah, JabalMoses, True, rounding_)

print("")
point1 = MasjidHudaibiyah
point2 = MasjidJironah
bear1  = calculate_bearing_plus_code(point1, loc_, False, rounding_)
bear2  = calculate_bearing_plus_code(point2, loc_, False, rounding_)
hh  = round(bear1-bear2, rounding_)
print(f"The half-span of the angle formed by the bearings from western ({point1.NAME_}) and eastern ({point2.NAME_}) boundaries of the Haram to {loc_.NAME_}=({round(bear2-360, rounding_)}-{round(bear1-360, rounding_)})/2={hh/2}\n\n")

point1 = nearMainGate
point2 = Rashidiya
bear1  = calculate_bearing_plus_code(point1, loc_, False, rounding_)
bear2  = calculate_bearing_plus_code(point2, loc_, False, rounding_)
hh  = round(bear1-bear2, rounding_)
print(f"The half-span of the angle formed by the bearings from western ({point1.NAME_}) and eastern ({point2.NAME_}) boundaries of the Haram to {loc_.NAME_}=({round(bear2-360, rounding_)}-{round(bear1-360, rounding_)})/2={hh/2}\n\n")
print(f"{hh/2}≈{round(hh/2, rounding_result_)} --> Surah At-Tin (Quran Chapter 95) mentions the Mount Sinai and the Secure City of Mecca in its second and third verse.")

loc_ = JabalSerbal
cb1 = calculate_bearing_plus_code(nearMainGate, JabalSerbal, True, rounding_)
cb2 = calculate_bearing_plus_code(MainGate, JabalSerbal, True, rounding_)
cb3 = calculate_bearing_plus_code(Hudaibiyah, JabalSerbal, True, rounding_)
cb4 = calculate_bearing_plus_code(Taneem, JabalSerbal, True, rounding_)
cb5 = calculate_bearing_plus_code(Kaaba, JabalSerbal, True, rounding_)
cb6 = calculate_bearing_plus_code(Juranah, JabalSerbal, True, rounding_)
cb7 = calculate_bearing_plus_code(Rashidiya, JabalSerbal, True, rounding_)

mq1 = calculate_bearing_plus_code(MasjidHudaibiyah, JabalSerbal, True, rounding_)
mq2 = calculate_bearing_plus_code(MasjidJironah, JabalSerbal, True, rounding_)

print("")
point1 = MasjidHudaibiyah
point2 = MasjidJironah
bear1  = calculate_bearing_plus_code(point1, loc_, False, rounding_)
bear2  = calculate_bearing_plus_code(point2, loc_, False, rounding_)
hh  = round(bear1-bear2, rounding_)
print(f"The half-span of the angle formed by the bearings from western ({point1.NAME_}) and eastern ({point2.NAME_}) boundaries of the Haram to {loc_.NAME_}=({round(bear2-360, rounding_)}-{round(bear1-360, rounding_)})/2={hh/2}\n\n")

point1 = nearMainGate
point2 = Rashidiya
bear1  = calculate_bearing_plus_code(point1, loc_, False, rounding_)
bear2  = calculate_bearing_plus_code(point2, loc_, False, rounding_)
hh  = round(bear1-bear2, rounding_)
print(f"The half-span of the angle formed by the bearings from western ({point1.NAME_}) and eastern ({point2.NAME_}) boundaries of the Haram to {loc_.NAME_}=({round(bear2-360, rounding_)}-{round(bear1-360, rounding_)})/2={hh/2}\n\n")
