from array import array

import moderngl
import pygame as pg

_default_fragment_shader = """
#version 330 core
uniform sampler2D image;

in vec2 fragmentTexCoord;
out vec4 color;

void main() {
    color = texture(image, fragmentTexCoord);
}
"""

_default_vertex_shader = """
#version 330 core

in vec2 vert;
in vec2 texCoord;
out vec2 fragmentTexCoord;

void main() {
    fragmentTexCoord = texCoord;
    gl_Position = vec4(vert, 0.0, 1.0);
}
"""

# /!\                                       /!\
# It is not the final version of Shader !!!!!!!
# /!\                                       /!\

def init_shaders():
    """ Initialize the Shader classes
    You can call it by hand, or the program will call it for you when you create a new shader.
    """
    Shader.ctx = moderngl.create_context()
    Shader.quad_buffer = Shader.ctx.buffer(data=array('f', [
        # position (x, y), uv coordinates (x, y)
        -1.0, 1.0, 0.0, 0.0,  # top left
        1.0, 1.0, 1.0, 0.0,  # top right
        -1.0, -1.0, 0.0, 1.0,  # bottom left
        1.0, -1.0, 1.0, 1.0,  # bottom right
    ]))
    Shader.quad_buffer_invert_y = Shader.ctx.buffer(data=array('f', [
        # position (x, y), uv coordinates (x, y)
        -1.0, 1.0, 0.0, 1.0,  # top left
        1.0, 1.0, 1.0, 1.0,  # top right
        -1.0, -1.0, 0.0, 0.0,  # bottom left
        1.0, -1.0, 1.0, 0.0,  # bottom right
    ]))


class Shader:
    ctx: moderngl.Context = None
    quad_buffer: moderngl.Buffer = None
    quad_buffer_invert_y: moderngl.Buffer = None
    texture_index_max = 0
    screen_size = 800, 600

    def add_uniform(self, name, value):
        """
        It sends the value in the uniform variable with the name specified of the shader
        :param name: the name of the uniform variable
        :param value: the value to put in the variable
        The value can be of a primitive value: int/float/... or a pg.Surface for a sampler2D or a list of primitive
        values for openGL's vec or arrays. You must put the exact good size.

        You can put a moderngl.Texture in value as a sampler2D. But be careful, every time you put a new one, the
        previous one is destroyed.
        """
        pass

    def render(self, invert_y=False):
        """
        Apply the shader to the screen
        You ust use pg.display.flip to show the difference
        :param invert_y: If it inverts the y-axis on drawing
        """
        pass

    @staticmethod
    def set_screen_size(new_screen_size):
        Shader.screen_size = new_screen_size
        Shader.ctx.viewport = (0, 0, new_screen_size.x, new_screen_size.y)

    def change_screen_size(self, new_size):
        self.set_screen_size(new_size)


class Shader2D(Shader):
    def __init__(self, vertex_shader=None, frag_shader=None):
        """
        :param vertex_shader: the name of the file containing the vertex shader
        :param frag_shader: the name of the file containing the fragment shader
        If not specified, the default shader is used instead
        """
        if self.ctx is None:
            init_shaders()

        if vertex_shader is None:
            vertex_shader_source = _default_vertex_shader
        else:
            with open(vertex_shader, "r") as file:
                vertex_shader_source = file.read()
        if frag_shader is None:
            frag_shader_source = _default_fragment_shader
        else:
            with open(frag_shader, "r") as file:
                frag_shader_source = file.read()

        self.program = self.ctx.program(vertex_shader=vertex_shader_source, fragment_shader=frag_shader_source)
        self.renderer = self.ctx.vertex_array(self.program, [(self.quad_buffer, "2f 2f", "vert",
                                                              "texCoord")])
        self.renderer_invert_y = self.ctx.vertex_array(self.program, [(self.quad_buffer_invert_y, "2f 2f", "vert",
                                                                       "texCoord")])

        self.texture_indices = {}
        self.used_textures = {}

    def _surf_to_texture(self, surf: pg.Surface):
        tex = self.ctx.texture(surf.get_size(), 4)
        tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        tex.swizzle = "BGRA"
        tex.write(surf.get_view('1'))
        return tex

    def _add_texture(self, name, texture):
        """ You're supposed to use add_uniform instead ! """
        if name not in self.texture_indices:
            self.texture_indices[name] = self.texture_index_max
            Shader.texture_index_max += 1
        if name in self.used_textures:
            self.used_textures[name].release()
        texture.use(self.texture_indices[name])
        self.program[name] = self.texture_indices[name]
        self.used_textures[name] = texture

    def add_uniform(self, name, value):
        if isinstance(value, pg.Surface):
            texture = self._surf_to_texture(value)
            self._add_texture(name, texture)
        elif isinstance(value, moderngl.Texture):
            self._add_texture(name, value)
        else:
            self.program[name] = value

    def render(self, invert_y=False):
        if invert_y:
            self.renderer_invert_y.render(mode=moderngl.TRIANGLE_STRIP)
        else:
            self.renderer.render(mode=moderngl.TRIANGLE_STRIP)


class MultiShaders2D(Shader):
    """ A container with many shaders, applied one after another.

    Don't put a MultiShader in a MultiShader !!
    """

    def __init__(self):
        self.shaders: list[Shader] = []
        self.frame_buffers: list[moderngl.Framebuffer] = []

    def add_shader(self, shader):
        """ add a shader applied after all the others """
        assert not isinstance(shader, MultiShaders2D), "Don't put a MultiShader in a MultiShader !! It's not a tree"
        self.shaders.append(shader)
        if len(self.shaders) > 1:
            screen_size = self.ctx.screen.size
            self.frame_buffers.append(self.ctx.framebuffer(color_attachments=[self.ctx.texture(screen_size, 4)]))
            self.shaders[-1].add_uniform("image", self.frame_buffers[-1].color_attachments[0])

    def __getitem__(self, item):
        """ Get the i-th shader """
        return self.shaders[item]

    def __setitem__(self, key, value):
        """ modify the i-th shader """
        assert isinstance(value, Shader)
        self.shaders[key] = value

    def render(self, invert_y=False):
        for i in range(len(self.shaders)):
            if i < len(self.shaders) - 1:
                self.frame_buffers[i].use()
            else:
                self.ctx.screen.use()
            self.shaders[i].render(i < len(self.shaders) - 1)

    def add_uniform(self, name, value):
        """
        It sends in the first shader

        :param name: the name of the uniform variable
        :param value: the value to put in the variable
        The value can be of a primitive value: int/float/... or a pg.Surface for a sampler2D
        """
        self.shaders[0].add_uniform(name, value)

    def change_screen_size(self, new_size):
        super().change_screen_size(new_size)
        for i in range(len(self.frame_buffers)):
            self.frame_buffers[i].release()
            self.frame_buffers[i] = self.ctx.framebuffer(color_attachments=[self.ctx.texture(new_size.get(), 4)])
