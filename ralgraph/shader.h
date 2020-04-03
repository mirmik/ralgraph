#ifndef SHADER_H
#define SHADER_H

#include <GL/glew.h> 
#include <GLFW/glfw3.h>
#include <string>

namespace ralgraph
{
	class shader_programm
	{
	public:
		// Идентификатор программы
		GLuint Program;

		// Конструктор считывает и собирает шейдер
		shader_programm(const std::string& vertex_shader_code, const std::string& fragment_shader_code);

		// Использование программы
		void Use();
	};

	GLFWwindow* create_glfw_window();
	int init();

	//int event_loop();
}

#endif