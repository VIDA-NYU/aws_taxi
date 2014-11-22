import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot

if __name__=='__main__':
    counts = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            counts.append(map(int, line.strip().split('\t')))
    counts.sort()
    fig = m_plot.figure(figsize=(11, 4))
    fig.suptitle('Trips vs Time', fontsize=20)
    ax = fig.add_subplot(111)
    ax.plot_date(*zip(*counts), fmt='r-', aa=True)
    ax.set_ylim([0, 600000])
    fig.savefig(sys.argv[2])
