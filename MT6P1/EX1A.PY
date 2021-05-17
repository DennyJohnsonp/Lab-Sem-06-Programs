from matplotlib import pyplot as plt
import numpy as np
vectors=[(1,1),(1,2),(2,3),(1,3)]
def plot_vectors(vectors,title=None):
    fig,ax=plt.subplots(1,1,figsize=(5,5))
    for x_cor,y_cor in vectors:
        ax.quiver(0,0,x_cor,y_cor,scale=1,angles='xy',scale_units='xy',color='steelblue')
        limit=np.max(np.abs(vectors)*1.25)
        ax.set_xlim([-limit,limit])
        ax.set_ylim([-limit,limit])
        ax.grid(True,linewidth=1.2,alpha=0.95,animated=True,linestyle="--",color='red')
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        if title!=None:
            plt.title(title)
    plt.show()
plot_vectors(vectors,'1.Vectors Using Quiver-18MEC24006-DENNY JOHNSON P')

a1=np.array((1,3))
b1=np.array((3,1))
vectors1=[a1,b1,a1+b1]
plot_vectors(vectors1,'2.Addition Of Vectors-18MEC24006-DENNY JOHNSON P')

a2=np.array((1,2))
vectors2=[a2,5*a2,0.75*a2,10*a2,-3*a2]
plot_vectors(vectors2,'3.18MEC24006-DENNY JOHNSON P')

a3=np.array((1,2))
b3=np.array((2,3))
vectors3=[a3,b3,a3+b3,a3-b3,2*a3,-3*a3]
plot_vectors(vectors3,'4.18MEC24006-DENNY JOHNSON P')