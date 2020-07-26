def ecdf(data):
    import numpy as np
    import matplotlib.pyplot as plt
    data=np.sort(data)
    x=data
    y=np.arange(0, len(data))/len(data)
    plt.xlabel('data')
    plt.ylabel('ecdf')
    plt.scatter(x,y)
    plt.show()
