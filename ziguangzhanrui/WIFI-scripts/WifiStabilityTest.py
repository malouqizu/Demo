import os

def WifiStabilityTest(testTimes):
    for i in range(0,testTimes):
        print("Test round ",str(i+1),":")
        os.system("python E:\demo\Python\project88\WifiCaseRuner.py" )

if __name__=="__main__":
    WifiStabilityTest(10)
