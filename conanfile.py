from conans import ConanFile, CMake


class lysConan(ConanFile):
    name = "lys"
    version = "0.1.0"
    license = "MIT License"
    url = "https://github.com/dysbeat/lys"
    description = "lys application"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "lys/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="lys")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/lys %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="lys")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lys"]
