import sys
import antigravity 
    
if __name__=='__main__':
    if len(sys.argv) == 4:
        latitude = sys.argv[1]
        longitude = sys.argv[2]
        datedow = sys.argv[3]

        # latitude = 48.85341
        # longitude = 2.3488
        # datedow = "25-06-11-35000"

        if not isinstance(latitude, float):
            print('Error latitude: expected Float number')
        elif not isinstance(longitude, float) :
            print('Error longitude: expected Float number')
        elif not isinstance(datedow, string):
            print("Error datedow: expected string")
        else:
            try:
                datedow_encode = datedow.encode("utf-8")
                antigravity.geohash(latitude, longitude, datedow_encode)
            except:
                print("Error")
    else:
        print("Expected three arguments")