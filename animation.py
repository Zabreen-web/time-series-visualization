import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

def setup_plot_style(ax):

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(axis='y',which='both',left=False)
    ax.tick_params(axis='x',which='both',bottom=False)
    ax.set_xlabel('Total Population',weight='bold')
    ax.set_title('Total 10 countries by Population',weight='bold')
    ax.grid(axis="x", linestyle="--", alpha=0.5)
def add_year_text(ax,year):
    if year<2025:

     ax.text(0.9,0.1,str(year),transform=ax.transAxes,ha='right', fontsize=28, color="black", alpha=0.7)

def create_animation(df):
    

    frames=df['Time'].unique()[:77]
    fig,ax=plt.subplots(figsize=(12,6))


    def animate(frame):
        ax.clear()
        top_countries=df[df['Time']==frame].nlargest(10,'TPopulation1Jan').sort_values('TPopulation1Jan',ascending=True)
        bars=ax.barh(top_countries['Location'],top_countries['TPopulation1Jan'],color='Yellow')
        for bar in bars:
            width = bar.get_width()
            ax.text(width +  0.01,bar.get_y() + bar.get_height() / 2, f"{int(width):,.2f}", 
         va='center', fontsize=10, color="black")
       
       
        setup_plot_style(ax)
        add_year_text(ax,frame)
        plt.tight_layout()
    anim= animation.FuncAnimation(fig,animate,frames=frames,interval=200)
    
    return anim
if __name__=='__main__':
     df=pd.read_csv('cleaned-data.csv')
     anim=create_animation(df)
     anim.save('video.gif', writer=PillowWriter(fps=10))
     plt.show()