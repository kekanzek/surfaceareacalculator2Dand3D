# Area calculator of 2D quadilateral:
import time
Pi = 3.1415
Delay = 0.005

def TwoDimAreaCalc():
    Height = int(input("Enter height: "));time.sleep(Delay)
    print("Height set to " + str(Height) + ".")
    Width = int(input("Enter width: "));time.sleep(Delay)
    print("Radius set to " + str(Width) + ".")
    Area = Height * Width
    print ("\nThe area is " + str(Area) + ".")

def ThreeDimAreaCalc():
    Height2 = int(input("Enter height: "));time.sleep(Delay)
    print("Height set to " + str(Height2) + ".")
    Width2 = int(input("Enter width: "));time.sleep(Delay)
    print("Radius set to " + str(Width2) + ".")
    Depth = int(input("Enter depth: "));time.sleep(Delay)
    print("Depth set to " +str(Depth) + ".")
    DH = Depth * Height2
    SQAREA = Width2 * DH
    print ("\nSquare area of 3D right-angled quad:" + str(SQAREA))

def Choose():
    Choice = int(input("Choose a selection.\n [ 1 ] for square area calculation of a 2D quad, [ 2 ] for square area calculation of a 3D right angle quad: "))
    if Choice == 2:
        ThreeDimAreaCalc()
    elif Choice == 1:
        TwoDimAreaCalc()
    else:
        print("Choose a valid option (1 or 2)")

Choose()