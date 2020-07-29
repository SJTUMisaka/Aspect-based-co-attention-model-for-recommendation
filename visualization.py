def calculate(index1, index2):
    p = new_embeddings[index1]                               #aspect
    q = model.contrast_model.get_weights()[0][index2]        #cast
    q = np.array([q]).T
    A = model.contrast_model.get_weights()[3]                #kernel
    temp = np.dot(p, A)
    return np.dot(temp, q)[0]


toplist = []
for j in range(1,51):
    toplist.append[calculate(1, j), 1, j]
toplist = np.array(toplist)
for i in range(1, 446):
    for j in range(1, 9395):
        pd = calculate(i, j)
        if (pd > np.min(toplist.T[0])):
            toplist[np.argmin(toplist.T[0])] = [pd, i, j]



    