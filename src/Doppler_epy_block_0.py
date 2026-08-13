from gnuradio import gr
import numpy as np

class blk(gr.sync_block):
    def __init__(self, samp_rate=10000):
        gr.sync_block.__init__(
            self,
            name="Phase Doppler Detector",
            in_sig=[np.complex64],
            out_sig=[np.float32]
        )
        self.fs = samp_rate

    def work(self, input_items, output_items):
        x = input_items[0]

        phase = np.unwrap(np.angle(x))
        dphi = np.diff(phase)

        fd = np.mean(dphi) * self.fs / (2*np.pi)

        output_items[0][:] = abs(fd)
        return len(output_items[0])
