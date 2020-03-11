from numpy import zeros

def interpolate(y, t):
    """Uses linear interpolation to find intermediate y"""
    i = int(t)
    # Scheme: y(t) = y_i + delta-y/delta-t * dt
    return y[i] + ((y[i+1] - y[i])/delta_t)*(t-i)

def find_y():
    """Repeatedly finds y at t by interpolation"""
    print 'For time t on the interval [0,%d]...' % (N)
    t = input('Give your desired t > 0: ')
    while t >= 0:
        print 'y(t) = %g' % (interpolate(y, t))
        t = input('Give new time t (to stop, enter t < 0): ')

# Note: do not need to store the sequence of times
N = 4            # Total number of measurements
delta_t = 1.0    # Time difference between measurements

y = zeros(5)
y[0] = 4.4; y[1] = 2.0; y[2] = 11.0
y[3] = 21.5; y[4] = 7.5

find_y()