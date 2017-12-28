import pylab

samples = []
linear = []
quadratic = []
cubic = []
exponential = []

for i in range(0,30):
    samples.append(i)
    linear.append(2*i + 2)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)

pylab.figure("Linear")
pylab.plot(samples, linear)
pylab.figure("Quadratic")
pylab.plot(samples, quadratic)
pylab.figure("Cubic")
pylab.plot(samples, cubic)
pylab.figure("Exponential")
pylab.plot(samples, exponential)
pylab.show()


##


pylab.figure("Quadrants", figsize=(16,6))

pylab.subplot(121)
pylab.title("Linear vs Quadratic")
pylab.xlabel("Sample points")
pylab.ylabel("Quadratic function")
pylab.plot(samples, linear)
pylab.plot(samples, quadratic)

pylab.subplot(122)
pylab.title("Cubic vs Exponential")
pylab.xlabel("Sample points")
pylab.ylabel("Function")
pylab.plot(samples, cubic, "c", label="Cubic")
pylab.plot(samples, exponential, "r", label="Exponential")
pylab.legend(loc="best")
pylab.show()


##


pylab.figure("Cubic vs Exponential", figsize=(16,6))

pylab.subplot(121)
pylab.title("Cubic vs Exponential (linear scaling)")
pylab.xlabel("Sample points")
pylab.ylabel("Function")
pylab.plot(samples, cubic, "c", label="Cubic")
pylab.plot(samples, exponential, "r", label="Exponential")
pylab.legend(loc="best")

pylab.subplot(122)
pylab.title("Cubic vs Exponential (log scaling)")
pylab.xlabel("Sample points")
pylab.ylabel("Function")
pylab.plot(samples, cubic, "c", label="Cubic")
pylab.plot(samples, exponential, "r", label="Exponential")
pylab.yscale("log")
pylab.legend(loc="best")
pylab.show()