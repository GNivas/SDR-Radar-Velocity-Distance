#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Term Assignment
# Author: Karthick
# Copyright: Team-05
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import math
from gnuradio import channels
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import Doppler_epy_block_0 as epy_block_0  # embedded python block
import Doppler_epy_block_1 as epy_block_1  # embedded python block
import sip
import threading



class Doppler(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Term Assignment", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Term Assignment")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Doppler")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.V = V = 0
        self.Fc = Fc = 2400000000
        self.samp_rate = samp_rate = 20000
        self.Fo = Fo = 2000
        self.Fif = Fif = 1000
        self.Fd = Fd = (V*2*Fc)/(3e8)*(5/18)

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            window.WIN_HANN, #wintype
            0, #fc
            samp_rate, #bw
            'Doppler Frequency Plot', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_2_0_0_1 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Transmitted and Intermediate Frequency (Fo and Fif))', #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_2_0_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_2_0_0_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_2_0_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2_0_0_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_2_0_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_2_0_0_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_2_0_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2_0_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_2_0_0_1.set_fft_window_normalized(False)



        labels = ['Transmitted Frequency (Fo)', 'Intermediate Frequency (Fif)', '', '', '',
            '', '', '', '', '']
        widths = [3, 3, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2_0_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2_0_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2_0_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_0_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_2_0_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_2_0_0_1_win)
        self.qtgui_freq_sink_x_2_0_0_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Filtered Spectrum', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_2_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_2_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_2_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_2_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_2_0_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_2_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_2_0_0_0.set_fft_window_normalized(False)



        labels = ['Fo + Fif ', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["magenta", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_2_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_2_0_0_0_win)
        self.qtgui_freq_sink_x_2_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Doppler with Intermediate Frequency', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_2_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_2_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_2_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_2_0.enable_grid(True)
        self.qtgui_freq_sink_x_2_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_2_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_2_0.set_fft_window_normalized(False)



        labels = ['Fif -Fd', '', '', '', '',
            '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["black", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_2_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_2_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Fd (Doppler frequency)', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Fd', '', '', '', '',
            '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["cyan", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.epy_block_1 = epy_block_1.blk(fc=2400000000)
        self.epy_block_0 = epy_block_0.blk(samp_rate=samp_rate)
        self.channels_fading_model_0 = channels.fading_model( 8, (10.0/samp_rate), True, 2, 0 )
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_conjugate_cc_1_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_multiply_conjugate_cc_1 = blocks.multiply_conjugate_cc(1)
        self.blocks_freqshift_cc_2_0 = blocks.rotator_cc(2.0*math.pi*Fd/samp_rate)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 100)
        self.band_pass_filter_0_0 = filter.interp_fir_filter_ccf(
            1,
            firdes.band_pass(
                5,
                samp_rate,
                (Fo+Fif -100),
                (Fo+Fif +100),
                100,
                window.WIN_HANN,
                6.76))
        self.analog_sig_source_x_1_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, Fo, 1, 0, 0)
        self.analog_sig_source_x_1_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, Fif, 1, 0, 0)
        self.Velocity = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Velocity.set_update_time(0.10)
        self.Velocity.set_title('Velocity(Km/h)')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Velocity.set_min(i, -1)
            self.Velocity.set_max(i, 1)
            self.Velocity.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Velocity.set_label(i, "Data {0}".format(i))
            else:
                self.Velocity.set_label(i, labels[i])
            self.Velocity.set_unit(i, units[i])
            self.Velocity.set_factor(i, factor[i])

        self.Velocity.enable_autoscale(False)
        self._Velocity_win = sip.wrapinstance(self.Velocity.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Velocity_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._V_range = qtgui.Range(0, 195, 1, 0, 200)
        self._V_win = qtgui.RangeWidget(self._V_range, self.set_V, "V", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._V_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Doppler_Frequency = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Doppler_Frequency.set_update_time(0.10)
        self.Doppler_Frequency.set_title('Doppler Frequency')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Doppler_Frequency.set_min(i, -1)
            self.Doppler_Frequency.set_max(i, 1)
            self.Doppler_Frequency.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Doppler_Frequency.set_label(i, "Data {0}".format(i))
            else:
                self.Doppler_Frequency.set_label(i, labels[i])
            self.Doppler_Frequency.set_unit(i, units[i])
            self.Doppler_Frequency.set_factor(i, factor[i])

        self.Doppler_Frequency.enable_autoscale(False)
        self._Doppler_Frequency_win = sip.wrapinstance(self.Doppler_Frequency.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Doppler_Frequency_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1_0_0, 0), (self.blocks_multiply_conjugate_cc_1_0, 0))
        self.connect((self.analog_sig_source_x_1_0_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_1_0_0, 0), (self.qtgui_freq_sink_x_2_0_0_1, 1))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.qtgui_freq_sink_x_2_0_0_1, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_conjugate_cc_1, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_2_0_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_freqshift_cc_2_0, 0))
        self.connect((self.blocks_freqshift_cc_2_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_1, 0), (self.blocks_multiply_conjugate_cc_1_0, 1))
        self.connect((self.blocks_multiply_conjugate_cc_1, 0), (self.qtgui_freq_sink_x_2_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_1_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_1_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_multiply_conjugate_cc_1, 1))
        self.connect((self.epy_block_0, 0), (self.Doppler_Frequency, 0))
        self.connect((self.epy_block_0, 0), (self.epy_block_1, 0))
        self.connect((self.epy_block_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.epy_block_1, 0), (self.Velocity, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Doppler")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_V(self):
        return self.V

    def set_V(self, V):
        self.V = V
        self.set_Fd((self.V*2*self.Fc)/(3e8)*(5/18))

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.set_Fd((self.V*2*self.Fc)/(3e8)*(5/18))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(5, self.samp_rate, (self.Fo+self.Fif -100), (self.Fo+self.Fif +100), 100, window.WIN_HANN, 6.76))
        self.blocks_freqshift_cc_2_0.set_phase_inc(2.0*math.pi*self.Fd/self.samp_rate)
        self.channels_fading_model_0.set_fDTs((10.0/self.samp_rate))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_2_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_2_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_2_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_Fo(self):
        return self.Fo

    def set_Fo(self, Fo):
        self.Fo = Fo
        self.analog_sig_source_x_1_1.set_frequency(self.Fo)
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(5, self.samp_rate, (self.Fo+self.Fif -100), (self.Fo+self.Fif +100), 100, window.WIN_HANN, 6.76))

    def get_Fif(self):
        return self.Fif

    def set_Fif(self, Fif):
        self.Fif = Fif
        self.analog_sig_source_x_1_0_0.set_frequency(self.Fif)
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(5, self.samp_rate, (self.Fo+self.Fif -100), (self.Fo+self.Fif +100), 100, window.WIN_HANN, 6.76))

    def get_Fd(self):
        return self.Fd

    def set_Fd(self, Fd):
        self.Fd = Fd
        self.blocks_freqshift_cc_2_0.set_phase_inc(2.0*math.pi*self.Fd/self.samp_rate)




def main(top_block_cls=Doppler, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
