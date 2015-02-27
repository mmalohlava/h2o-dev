import sys, os
sys.path.insert(1,"../../../")
import h2o

def deeplearning_multi(ip,port):
    h2o.init(ip, port)

    print("Test checks if Deep Learning works fine with a categorical dataset")

    # print(locate("smalldata/logreg/protstate.csv"))
    prostate = h2o.import_frame(path="smalldata/logreg/prostate.csv")
    prostate[2] = prostate[2].asfactor() #AGE -> Factor
    prostate[3] = prostate[3].asfactor() #RACE -> Factor
    prostate[4] = prostate[4].asfactor() #DPROS -> Factor
    prostate[5] = prostate[5].asfactor() #DCAPS -> Factor
    prostate = prostate.drop('ID')       #remove ID
    prostate.describe()


    hh = h2o.deeplearning(x                     = prostate.drop('CAPSULE'),
                          y                     = prostate['CAPSULE'],
                          hidden                = [10, 10],
                          use_all_factor_levels = False)
    hh.show()
    
if __name__ == '__main__':
    h2o.run_test(sys.argv, deeplearning_multi)