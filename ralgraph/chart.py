#!/usr/bin/python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import numpy
import time
import threading

class ArrayChart:
	def __init__(self, plot=None):
		self.plot = plot

		self.x_chart_coords = []
		self.y_chart_coords = []

		self.autoscale = True
		self.xmin = float("inf")
		self.ymin = float("inf")
		self.xmax = -float("inf")
		self.ymax = -float("inf")

		if plot is not None:
			self.plot.attach_chart(self)

	def redraw(self):
		self.plot.redraw()

	def set_vertices(self, vtxs):
		self.vertices = vtxs

	def set_color(self, r, g, b, a=1):
		self.qcolor = QColor.fromRgbF(r,g,b,a)

	def set_xrange(self, xmin, xmax):
		self.xmin = xmin
		self.xmax = xmax
		self.autoscale = False

	def set_yrange(self, ymin, ymax):
		self.ymin = ymin
		self.ymax = ymax
		self.autoscale = False

	def set_xcoords(self, xarr):
		if self.autoscale:
			for x in xarr:
				if x > self.xmax: self.xmax = x
				if x < self.xmin: self.xmin = x

		xr = 2 / (self.xmax - self.xmin)
		self.x_chart_coords = [ ((x - self.xmin) * xr) - 1 for x in xarr ]

	def set_ycoords(self, yarr):
		if self.autoscale:
			for y in yarr:
				if y > self.ymax: self.ymax = y
				if y < self.ymin: self.ymin = y

		yr = 2 / (self.ymax - self.ymin)
		self.y_chart_coords = [ ((y - self.ymin) * yr) - 1 for y in yarr ]

	def set_coords(self, x, y):
		self.set_xcoords(x)
		self.set_ycoords(y)

	def draw(self, painter, center, whalf, hhalf):
		painter.setPen(self.qcolor)

		points = [0] * len(self.x_chart_coords)
		for i in range(len(self.x_chart_coords)):
			x = self.x_chart_coords[i]
			y = self.y_chart_coords[i]
			points[i] = center + QPointF(x*whalf, y*hhalf)

		for i in range(len(points) - 1):
			painter.drawLine(points[i], points[i+1])


class PlotWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		#self.vertices = []
		self.charts = []
		self.margins = [80,20,20,50]

		self.border=True
		self.set_border_color(0.5,0.5,0.5)
		self.set_background(0,0,0)

	def set_background(self, r, g, b):
		pal = self.palette();
		pal.setColor(QPalette.Background, QColor.fromRgbF(r,g,b))
		self.setAutoFillBackground(True)
		self.setPalette(pal)

	def set_border_color(self, r, g, b):
		self._border_color = QColor.fromRgbF(r,g,b)

	def attach_chart(self, chart):
		self.charts.append(chart)
		chart.plot = self

	def redraw(self):
		self.update()

	def set_left_margin(self, arg):
		self.margins[0] = arg
		self.redraw()

	def set_bottom_margin(self, arg):
		self.margins[3] = arg
		self.redraw()

	def set_top_margin(self, arg):
		self.margins[2] = arg
		self.redraw()

	def set_right_margin(self, arg):
		self.margins[1] = arg
		self.redraw()

	def set_margins(self, mrgs):
		self.margins = mrgs
		self.redraw()

	def paintEvent(self, ev):
		w = self.width() - self.margins[0] - self.margins[1]
		h = self.height() - self.margins[2] - self.margins[3]

		w_half = w/2
		h_half = h/2

		c = QPointF(w_half + self.margins[0], h_half+self.margins[2])

		painter = QPainter(self)

		for chart in self.charts:
			chart.draw(painter, c, w_half, h_half)

		if self.border:
			painter.setPen(self._border_color)
			if self.border:
				painter.drawLine(QPoint(self.margins[0], self.margins[2]), QPoint(self.margins[0], self.height()-self.margins[3]))
				painter.drawLine(QPoint(self.margins[0], self.height()-self.margins[3]), QPoint(self.width()-self.margins[1], self.height()-self.margins[3]))

		painter.end()

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv[1:])

	plot = PlotWidget()
	chart = ArrayChart(plot)
	chart2 = ArrayChart(plot)

	t = numpy.linspace(-100, 100, 1000)
	y = numpy.sin(t*0.2) * 100
	y2 = numpy.cos(t*0.2) * 100

	chart.set_color(1,0,0)
	chart2.set_color(0,1,0)
	chart.set_coords(t, y)
	chart2.set_coords(t, y2)
	chart.redraw()
	chart2.redraw()

	class Thr(QThread):
		def run(self):
			stime = time.time()
			while 1:
				ctime = time.time() - stime
		
				t = numpy.linspace(-100+ctime*5, 100+ctime*5, 1000)
				y = numpy.sin(t*0.2) * 100
				y2 = numpy.cos(t*0.2) * 100
		
				chart.set_xrange(-100+ctime*5, 100+ctime*5)
				chart2.set_xrange(-100+ctime*5, 100+ctime*5)

				chart.set_coords(t, y)
				chart2.set_coords(t, y2)
				chart.redraw()
				chart2.redraw()

				time.sleep(0.01)


	thr = Thr()
	thr.start()



	plot.show()
	app.exec()