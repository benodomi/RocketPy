import time
class FlightSoftware:
    def __init__(self, sampling_period = 0.01, real_time = False):
        self.sampling_period = sampling_period
        self.sampling_rate = 1/ sampling_period
        self.real_time = real_time
        self.last_call_sim = 0

    def evaluate_fsw(self,t,y):
        if abs((t-self.last_call_sim)-self.sampling_period) <= 1e-5:
            
            '''
            TODO: Controller in C calling, UDP communication implementation, etc...
            '''
            
            
            self.last_call_sim = t
            if(self.real_time == True):
                time.sleep(0.8*self.sampling_period)
                
        else:
            pass