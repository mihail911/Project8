import numpy as np



def normalize_fft(f):
    N = len(f)
    normalized = np.zeros(N)
    for idx, elem in enumerate(f):
        normalized[idx] = np.abs(elem)

    return normalized


def multiply(f, g):
    N = len(f)
    fplus = np.zeros(2*N)
    gplus = np.zeros(2*N)

    fplus[0:N] = f
    gplus[0:N] = g

    ffplus = np.fft.rfft(fplus)
    fgplus = np.fft.rfft(gplus)

    n_ffplus = normalize_fft(ffplus)
    n_fgplus = normalize_fft(fgplus)

    prod = n_ffplus * n_fgplus

    inverse = np.fft.irfft(prod)

    print inverse

    print "-"*5

    print normalize_fft(inverse)

    print "-"*5

    print np.convolve(f, g)


if __name__ == "__main__":
    f = np.array([2,3,4])
    g = np.array([4,5,5])

    multiply(f,g)
