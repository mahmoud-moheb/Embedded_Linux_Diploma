#!/usr/bin/python3
import task_functions
task_functions.open_prog("vscode")
task_functions.open_extensions()
task_functions.extension_install("clangd")
task_functions.extension_install("c++ testmate")
task_functions.extension_install("c++ helper")
task_functions.extension_install("cmake")
task_functions.extension_install("cmake tools")
print("extensions are installed successfully")