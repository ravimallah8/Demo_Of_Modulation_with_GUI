import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal
def amAnimation():
    fm=3
    fc = 80
    em = 0.2
    ec = 0.21
    fig, (ax1, ax2,ax3) = plt.subplots(3)
    x = np.arange(0, 2*np.pi, 0.01)
    s = em*np.sin(fm*x)
    c = ec*np.sin(fc*x)
    am = (ec+s)*c
    line_s, = ax1.plot(x, s, color="r", label="signal")
    line_c, = ax2.plot(x, c, color="b", label="carrier")
    line_am, = ax3.plot(x, am,label="am wave")
    ax1.legend()
    ax2.legend()
    ax3.set_ylim(-1.2*(em+ec),1.2*(em+ec))
    ax3.legend()
    
    def animate(i):
        line_s.set_ydata(em*np.sin(fm*x+i/10.0))
        line_c.set_ydata(ec*np.sin(fc*x+i/10.0))
        line_am.set_ydata((ec+em*np.sin(fm*x+i/10.0))*np.sin(fc*x+i/10.0))
        return line_s,line_c,line_am
    
    def init():
        line_s.set_ydata(np.ma.array(x, mask=True))
        line_c.set_ydata(np.ma.array(x, mask=True))
        return line_s,line_c,
    
    ani = animation.FuncAnimation(fig, animate, np.arange(1,500),
                                  interval = 10, blit = True, init_func= init)
    plt.style.use('ggplot')
    plt.show()
    
def fmAnimation():
    fm= 3
    fc = 50
    em = 2
    ec = 2.1
    beta = 1.25
    del_f = beta*em
    fig, (ax1, ax2,ax3) = plt.subplots(3)
    x = np.arange(0, 2*np.pi, 0.01)
    s = em*np.sin(fm*x)
    c = ec*np.sin(fc*x)
    am = ec*np.sin((fc+(del_f/fm)*s)*x)
    line_s, = ax1.plot(x, s, color="r", label="signal")
    line_c, = ax2.plot(x, c, color="b", label="carrier")
    line_am, = ax3.plot(x, am,label="fm wave")
    ax1.legend()
    ax2.legend()
    ax3.set_ylim(-(em+ec),(em+ec))
    ax3.legend()
    
    def animate(i):
        line_s.set_ydata(em*np.sin(fm*x+i/10.0))
        line_c.set_ydata(ec*np.sin(fc*x+i/10.0))
        line_am.set_ydata(ec*np.sin((fc+(del_f/fm)*(em*np.sin(fm*x+i/10.0)))*x+i/10.0))
        return line_s,line_c,line_am
    
    def init():
        line_s.set_ydata(np.ma.array(x, mask=True))
        line_c.set_ydata(np.ma.array(x, mask=True))
        line_am.set_ydata(np.ma.array(x, mask=True))
        return line_s,line_c, line_am,
    
    ani = animation.FuncAnimation(fig, animate, np.arange(1,500),
                                  interval = 10, blit = True, init_func= init)
    plt.style.use('ggplot')
    plt.show()

def pmAnimation():
    fm=3
    fc = 50
    em = 0.2
    ec = 0.21
    ps = 40
    pc = 1/8
    fig, (ax1, ax2,ax3) = plt.subplots(3)
    x = np.arange(0, 2*np.pi, 0.01)
    s = em*np.sin(fm*x)
    c = ec*np.sin(fc*x)
    pm = ec*np.sin(fc*x+(pc+ps*s))
    p = 1/8
    line_s, = ax1.plot(x, s, color="r", label="signal")
    line_c, = ax2.plot(x, c, color="b", label="carrier")
    line_pm, = ax3.plot(x, pm,label="pm wave")
    ax1.legend()
    ax2.legend()
    ax3.set_ylim(-(em+ec),(em+ec))
    ax3.legend()
    
    def animate(i):
        line_s.set_ydata(em*np.sin(fm*x+i/10.0))
        line_c.set_ydata(ec*np.sin(fc*x+i/10.0))
        line_pm.set_ydata(ec*np.sin(fc*x+i/10.0+(p+ps*(em*np.sin(fm*x+i/10.0)))))
        return line_s,line_c,line_pm
    
    def init():
        line_s.set_ydata(np.ma.array(x, mask=True))
        line_c.set_ydata(np.ma.array(x, mask=True))
        return line_s,line_c,
    
    ani = animation.FuncAnimation(fig, animate, np.arange(1,500),
                                  interval = 10, blit = True, init_func= init)
    plt.style.use('ggplot')
    plt.show()

    
def pamAnimation():
    sampling_freq = 2000
    fm=3
    fp = 50
    em = 1
    ep = 1.02
    fig, (ax1, ax2, ax3) = plt.subplots(3)
    x = np.arange(0, 2*np.pi, 0.01)
    s = em*np.sin(fm*x)
    p = signal.square(fp*x)
    pam = (ep+s)*p
    line_s, = ax1.plot(x, s, color="r", label="signal")
    line_p, = ax2.plot(x, p, color="b", label="pulse")
    line_pam, = ax3.plot(x, pam, label="pam wave")
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax1.set_xlim(0,6)
    ax2.set_xlim(0,6)
    ax3.set_xlim(0,6)
    
    def animate(i):
        line_s.set_ydata(em*np.sin(fm*x+i/10.0))
        line_p.set_ydata(signal.square(fp*x+i/10.0))
        line_pam.set_ydata((ep+em*np.sin(fm*x+i/10.0))*(signal.square(fp*x+i/10.0)))
        return line_s, line_p, line_pam,
    
    def init():
        line_s.set_ydata(np.ma.array(x, mask=True))
        line_p.set_ydata(np.ma.array(x, mask=True))
        line_pam.set_ydata(np.ma.array(x, mask=True))
        return line_s, line_p,line_pam,
    
    ani = animation.FuncAnimation(fig, animate, np.arange(1,500),
                                  interval =  10, blit = True, init_func= init)
    plt.style.use('ggplot')
    plt.show()
