#include <ralgraph/show.h>
#include <ralgraph/chart.h>
#include <ralgo/vecops.h>

int main() 
{
	ralgraph::init_qt_application();

	auto chart = ralgraph::chart();
	//chart.opengpl_enable();
	
	std::vector<float> x = {1,2,3};
	std::vector<float> y = ralgo::vecops::mul_vs(x, 3);

	chart.set_data(x, y);

	ralgraph::show(chart);
}