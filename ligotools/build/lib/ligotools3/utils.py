import numpy as np
from scipy.io import wavfile

# function to whiten data
def whiten(strain, interp_psd, dt):
    Nt = len(strain)
    freqs = np.fft.rfftfreq(Nt, dt)
    freqs1 = np.linspace(0,2048.,Nt/2+1)

    # whitening: transform to freq domain, divide by asd, then transform back, 
    # taking care to get normalization right.
    hf = np.fft.rfft(strain)
    norm = 1./np.sqrt(1./(dt*2))
    white_hf = hf / np.sqrt(interp_psd(freqs)) * norm
    white_ht = np.fft.irfft(white_hf, n=Nt)
    return white_ht

# function to keep the data within integer limits, and write to wavfile:
def write_wavfile(filename,fs,data):
    d = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
    wavfile.write('audio/' + filename,int(fs), d)

# function that shifts frequency of a band-passed signal
def reqshift(data,fshift=100,sample_rate=4096):
    """Frequency shift the signal by constant
    """
    x = np.fft.rfft(data)
    T = len(data)/float(sample_rate)
    df = 1.0/T
    nbins = int(fshift/df)
    # print T,df,nbins,x.real.shape
    y = np.roll(x.real,nbins) + 1j*np.roll(x.imag,nbins)
    y[0:nbins]=0.
    z = np.fft.irfft(y)
    return z

def make_plot_detector(det, time, timecomp, strain, pcolor, label_strain, lim_x=None, lim_y=None, template=None) :
	plt.plot(time-timecomp,strain,pcolor,label=det+' whitened h(t)')
	if template is not None :
		plt.plot(time-timecomp,template_match,'k',label='Template(t)')
	if lim_y is not None :
		plt.ylim(lim_y)
	if lim_x is not None :
		plt.xlim(lim_x)
	plt.grid('on')
	plt.xlabel('Time since {0:.4f}'.format(timemax))
	plt.ylabel(label_strain)
	plt.legend(loc='upper left')