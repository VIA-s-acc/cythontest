from time import time 
from multiprocessing import Process
from threading import Thread
import multiprocessing as mp
import build.nogil as ng

def performance(f):
    def handler(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        end = time()
        handler.resultString = (f'Elapsed time: {(end - start):.3f} with result {res}')
        
    handler.resultString = None
    return handler

def linear(a,b,c):
    results = []
    ng.calc(a,b,c,results)
    ng.calc(a,b,c,results)
    ng.calc(a,b,c,results)
    ng.calc(a,b,c,results)
    ng.calc(a,b,c,results)
     
    return results

def multithread(a,b,c):
    results = []
    t1 = Thread(target=ng.calc, args=(a,b,c,results))
    t2 = Thread(target=ng.calc, args=(a,b,c,results))
    t3 = Thread(target=ng.calc, args=(a,b,c,results))
    t4 = Thread(target=ng.calc, args=(a,b,c,results))
    t5 = Thread(target=ng.calc, args=(a,b,c,results))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    
    return results


def multiprocess(a, b, c):
    results = mp.Manager().list() 
    
    p1 = mp.Process(target=ng.calc, args=(a,b,c,results))
    p2 = mp.Process(target=ng.calc, args=(a,b,c,results))
    p3 = mp.Process(target=ng.calc, args=(a,b,c,results))
    p4 = mp.Process(target=ng.calc, args=(a,b,c,results))
    p5 = mp.Process(target=ng.calc, args=(a,b,c,results))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    
    return results

def p_calc(a,b,c, results = None):
    result = a+b+c
    if results is not None:
        results.append(result)
    
    return result



def p_lin(a,b,c):
    results = []
    
    p_calc(a,b,c,results)
    p_calc(a,b,c,results)
    p_calc(a,b,c,results)
    p_calc(a,b,c,results)
    p_calc(a,b,c,results)

    return results
    

if __name__ == "__main__":
    a = 14512412
    b = 421521
    c = 2152152
    func1 = performance(linear)
    func2 = performance(multithread)
    func3 = performance(multiprocess)
    func4 = performance(p_lin)
    func1(a,b,c)
    print(func1.resultString)
    func2(a,b,c)
    print(func2.resultString)
    func3(a,b,c)
    print(func3.resultString)
    func4(a,b,c)
    print(func4.resultString)
    
