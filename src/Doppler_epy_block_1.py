from gnuradio import gr
import numpy as np

class blk(gr.sync_block):
    def __init__(self, fc=2.4e9):
        gr.sync_block.__init__(
            self,
            name="Speed Calculator",
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.c = 3e8

    def work(self, input_items, output_items):
        fd = input_items[0]
        v = (self.c * fd) / (2 * self.fc)
        output_items[0][:] = v * 3.6  # km/h
        return len(output_items[0])
