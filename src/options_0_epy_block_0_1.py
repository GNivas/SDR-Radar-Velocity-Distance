import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self, delay=40, samp_rate=2e6):
        gr.sync_block.__init__(
            self,
            name="distance_calc",
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

        self.delay = delay
        self.samp_rate = samp_rate
        self.c = 3e8

    def work(self, input_items, output_items):

        tau = self.delay / self.samp_rate
        R = (self.c * tau) / 2

        output_items[0][:] = R

        return len(output_items[0])