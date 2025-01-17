import torch
import random
import numpy as np
from scipy import signal
from scipy.ndimage.interpolation import shift

class TwoTransform:
    def __init__(self, transform):
        self.transform = transform

    def __call__(self, x, x_random=None):
        return [
            self.transform(x, x_random=x_random),
            self.transform(x, x_random=x_random)
        ]


class Compose:

    def __init__(self, transforms, mode='full'):
        self.transforms = transforms
        self.mode = mode

    def __call__(self, x, x_random=None):
        if self.mode == 'random':
            index = random.randint(0, len(self.transforms) - 1)
            x = self.transforms[index](x)
        elif self.mode == 'full':
            for t in self.transforms:
                if hasattr(t, 'requires_x_random') and t.requires_x_random:
                    x = t(x, x_random=x_random)
                else:
                    x = t(x)
        elif self.mode == 'shuffle':
            transforms = np.random.choice(self.transforms, len(self.transforms), replace=False)
            for t in transforms:
                x = t(x)
        else:
            raise NotImplementedError
        return x

    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        for t in self.transforms:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string


class RandomAmplitudeScale:

    def __init__(self, range=(0.5, 2.0), p=0.5):
        self.range = range
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            scale = random.uniform(self.range[0], self.range[1])
            return x * scale
        return x

    def __repr__(self):
        return self.__class__.__name__ + '()'


class RandomDCShift:
    
    def __init__(self, range=(-10.0, 10.0), p=0.5):
        self.range = range
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            shift = random.uniform(self.range[0], self.range[1])
            return x + shift
        return x

    def __repr__(self):
        return self.__class__.__name__ + '()'


class RandomTimeShift:

    def __init__(self, range=(-300, 300), mode='constant', cval=0.0, p=0.5):
        self.range = range
        self.mode = mode
        self.cval = cval
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            t_shift = random.randint(self.range[0], self.range[1])
            if len(x.shape) == 2:
                x = x[0]
            x = shift(input=x, shift=t_shift, mode=self.mode, cval=self.cval)
            x = np.expand_dims(x, axis=0)
        return x

    def __repr__(self):
        return self.__class__.__name__ + '()'


class RandomZeroMasking:
    
    def __init__(self, range=(0, 300), p=0.5):
        self.range = range
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            mask_len = random.randint(self.range[0], self.range[1])
            random_pos = random.randint(0, x.shape[1] - mask_len)
            mask = np.concatenate([np.ones((1, random_pos)), np.zeros((1, mask_len)), np.ones((1, x.shape[1] - mask_len - random_pos))], axis=1)
            return x * mask
        return x

    def __repr__(self):
        return self.__class__.__name__ + '()'


class RandomAdditiveGaussianNoise:
    
    def __init__(self, range=(0.0, 0.2), p=0.5):
        self.range = range
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            sigma = random.uniform(self.range[0], self.range[1])
            return x + np.random.normal(0, sigma, x.shape)
        return x

    def __repr__(self):
        return self.__class__.__name__ + '()'


class RandomBandStopFilter:

    def __init__(self, range=(0.5, 30.0), band_width=2.0, sampling_rate=100.0, p=0.5):
        self.range = range
        self.band_width = band_width
        self.sampling_rate = sampling_rate
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            low_freq = random.uniform(self.range[0], self.range[1])
            center_freq = low_freq + self.band_width / 2.0
            b, a = signal.iirnotch(center_freq, center_freq / self.band_width, fs=self.sampling_rate)
            x = signal.lfilter(b, a, x)

        return x

    def __repr__(self):
        return self.__class__.__name__ + '()'
    
    
class TimeWarping:

    def __init__(self, n_segments=4, scale_range=(0.5, 2.0), p=0.5):
        self.n_segments = n_segments
        self.scale_range = scale_range
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            L = x.shape[-1]
            segment_length = L // self.n_segments
            segments = []
            for i in range(self.n_segments):
                start = i * segment_length
                end = start + segment_length if i < self.n_segments - 1 else L
                Si = x[..., start:end]
                omega = random.uniform(self.scale_range[0], self.scale_range[1])
                new_length = max(1, int(Si.shape[-1] * omega))
                Si_transformed = signal.resample(Si, new_length, axis=-1)
                segments.append(Si_transformed)
            x_aug = np.concatenate(segments, axis=-1)
            x_aug = signal.resample(x_aug, L, axis=-1)
            return x_aug
        return x

    def __repr__(self):
        return f"{self.__class__.__name__}(n_segments={self.n_segments}, scale_range={self.scale_range}, p={self.p})"


class Permutation:

    def __init__(self, n_segments=4, p=0.5):
        self.n_segments = n_segments
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            L = x.shape[-1]
            segment_length = L // self.n_segments
            segments = []
            indices = list(range(self.n_segments))
            for i in indices:
                start = i * segment_length
                end = start + segment_length if i < self.n_segments - 1 else L
                Si = x[..., start:end]
                segments.append(Si)
            random.shuffle(indices)
            shuffled_segments = [segments[i] for i in indices]
            x_aug = np.concatenate(shuffled_segments, axis=-1)
            return x_aug
        return x

    def __repr__(self):
        return f"{self.__class__.__name__}(n_segments={self.n_segments}, p={self.p})"


class CutoutResize:

    def __init__(self, n_segments=4, p=0.5):
        self.n_segments = n_segments
        self.p = p

    def __call__(self, x):
        if torch.rand(1) < self.p:
            L = x.shape[-1]
            segment_length = L // self.n_segments
            segments = []
            for i in range(self.n_segments):
                start = i * segment_length
                end = start + segment_length if i < self.n_segments - 1 else L
                Si = x[..., start:end]
                segments.append(Si)
            r = random.randint(0, self.n_segments - 1)
            del segments[r]
            x_aug = np.concatenate(segments, axis=-1)
            x_aug = signal.resample(x_aug, L, axis=-1)
            return x_aug
        return x

    def __repr__(self):
        return f"{self.__class__.__name__}(n_segments={self.n_segments}, p={self.p})"


class TailoredMixup:
    def __init__(self, p=0.5, fs=100, beta=0.5):
        self.p = p
        self.fs = fs
        self.beta = beta
        self.requires_x_random = True

    def __call__(self, x_anchor, x_random=None):
        if torch.rand(1) < self.p and x_random is not None:
            X_anchor = np.fft.fft(x_anchor)
            X_random = np.fft.fft(x_random)
            A_anchor = np.abs(X_anchor)
            P_anchor = np.angle(X_anchor)
            A_random = np.abs(X_random)
            P_random = np.angle(X_random)
            lambda_A = random.uniform(self.beta, 1.0)
            lambda_P = random.uniform(self.beta, 1.0)
            A_mix = lambda_A * A_anchor + (1 - lambda_A) * A_random
            delta_theta = P_anchor - P_random
            delta_theta = (delta_theta + np.pi) % (2 * np.pi) - np.pi
            P_mix = P_anchor - delta_theta * (1 - lambda_P)
            X_mix = A_mix * np.exp(1j * P_mix)
            x_anchor = np.fft.ifft(X_mix).real
        return x_anchor