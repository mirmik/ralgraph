#include <ralgraph/show.h>
#include <ralgraph/chart.h>

#include <QtWidgets/QApplication>

QApplication * QTAPP;
int QTAPP_argc = 0;
char* QTAPP_argv[] {};

void ralgraph::show(ralgraph::chart& chart)
{
	chart.show();
	QTAPP->exec();
}

void ralgraph::init_qt_application() 
{

	QTAPP = new QApplication(QTAPP_argc, QTAPP_argv);	
}