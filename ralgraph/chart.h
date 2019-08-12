#ifndef RALGRAPH_CHART_H
#define RALGRAPH_CHART_H

#include <nos/print.h>

#include <QtWidgets/QWidget>
#include <QtCharts>

#include <QtCharts/QChart>
#include <QtCharts/QChartView>
#include <QtCharts/QLineSeries>
#include <QtCharts/QChart>
#include <QtCharts/QValueAxis>

namespace ralgraph
{
	class chart : public QWidget
	{
		Q_OBJECT

		QChart *m_chart;
		QLineSeries *m_series;
		QChartView *m_chartView;

		QValueAxis *axisX;
		QValueAxis *axisY;

		QLayout* layout;
		QVector<QPointF> data;

	public:
		chart(QWidget * parent = nullptr) : QWidget(parent),
			m_chart(new QChart),
			m_series(new QLineSeries)
		{
			m_chartView = new QChartView(m_chart);

			m_chartView->setMinimumSize(800, 600);
			m_chart->addSeries(m_series);

			axisX = new QValueAxis;
			axisX->setRange(0, 10);
			//axisX->setLabelFormat("%g");
			axisX->setTitleText("X");

			axisY = new QValueAxis;
			axisY->setRange(0, 10);
			axisY->setTitleText("Y");

			m_chart->setAxisX(axisX, m_series);
			m_chart->setAxisY(axisY, m_series);

			layout = new QVBoxLayout();
			layout->addWidget(m_chartView);

			setLayout(layout);
		}

		void opengpl_enable() 
		{
			m_series->setUseOpenGL(true);
		}

		void autoscale() 
		{
			float xmin = data[0].x(), xmax = data[0].x(), ymin = data[0].y(), ymax = data[0].y();

			for (int i = 1; i < data.size(); ++i) 
			{
				QPointF& pnt = data[i];

				if (pnt.x() < xmin) xmin = pnt.x();
				if (pnt.x() > xmax) xmax = pnt.x();

				if (pnt.y() < ymin) ymin = pnt.y();
				if (pnt.y() < ymax) ymax = pnt.y();
			}

			axisX->setRange(xmin, xmax);
			axisY->setRange(ymin, ymax);
		}

		template<class X, class Y>
		void set_data(const X & x, const Y & y)
		{
			nos::println(x);
			nos::println(y);

			QVector<QPointF> arr(x.size());

			for (int i = 0; i < x.size(); ++i) 
			{
				arr[i] = QPointF(x[i], y[i]);
			} 

			data = arr;

			m_series->replace(data);
		}
	};
}

#endif