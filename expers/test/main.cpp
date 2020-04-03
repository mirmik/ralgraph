#include <ralgraph/shader.h>
#include <ralgraph/sprograms.h>

#include <GLFW/glfw3.h>

#include <thread>
#include <chrono>

int main () 
{
	auto window = ralgraph::create_glfw_window();
	ralgraph::init();

	auto programm = ralgraph::shader_programm(
		ralgraph::simple_vertex_shader,
		ralgraph::simple_fragment_shader
	);

	while (!glfwWindowShouldClose(window))
	{
		glfwPollEvents();

		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);

		glfwSwapBuffers(window);
		std::this_thread::sleep_for(std::chrono::milliseconds(20));
	}

	glfwTerminate();
	return 0;
}