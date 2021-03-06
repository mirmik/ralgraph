#include <ralgraph/sprograms.h>

std::string ralgraph::simple_vertex_shader = 
R"(
	#version 330 core
	layout (location = 0) in vec3 position;

	void main()
	{
   		gl_Position = vec4(position.x, position.y, position.z, 1.0);
	}
)";

std::string ralgraph::simple_fragment_shader = 
R"(
	#version 330 core
	out vec4 color;

	void main()
	{
		color = vec4(1.0f, 0.5f, 0.2f, 1.0f);
	}
)";