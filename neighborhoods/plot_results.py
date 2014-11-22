import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot

if __name__=='__main__':
    counts = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            name, value = line.strip().split('\t')
            counts.append((int(value), name))
    counts.sort(reverse=True)
    counts = counts[:20]
    values, names = zip(*counts)
    yticks = map(lambda x: len(counts)-x-0.5,range(len(names)))
    fig = m_plot.figure(figsize=(7, 8))
    fig.suptitle('Trips per Neighborhood', fontsize=20)
    ax = m_plot.Axes(fig, [.3,.1,.6,.8])
    fig.add_axes(ax) 
    ax.barh(yticks, values, align='center')
    m_plot.yticks(yticks, names)
    fig.savefig(sys.argv[2])
