cdef extern from 'lowlevel/module.c' nogil:
    int calc_c(int a, int b, int c);


cdef int calc_tc(int a, int b, int c) nogil:
    return calc_c(a, b, c);

def calc(int a, int b, int c, results = None):
    cdef int result;

    with nogil:
        result = calc_tc(a,b,c)

    if results is not None:
        results.append(result)

    return result