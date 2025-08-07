import sys
import antigravity 
    
if __name__=='__main__':
    if len(sys.argv) == 4:
        try:
            latitude = float(sys.argv[1])
        except Exception as e:
            print('Error latitude: expected Float number')
            sys.exit(1)
        try:
            longitude = float(sys.argv[2])
        except Exception as e:
            print('Error longitude: expected Float number')
            sys.exit(1)
        datedow = sys.argv[3]
        try:
            datedow_encode = datedow.encode("utf-8")
        except Exception as e:
            print('Error longitude: expected str')
            sys.exit(1)
        antigravity.geohash(latitude, longitude, datedow_encode)

    else:
        print("Expected three arguments")