'''
refers:http://aosabook.org/en/500L/contingent-a-fully-dynamic-build-system.html
本项目的目的是为了解决构建过程中编译文件和修改文件不相符的问题
为了只编译那些已经修改的文件(包括交叉引用的文件)，项目构建了输入容器和输出容器，用来存储对应文件所关联的所有文件
当相应文件修改时，只需要修改所有关联的文件就可以了
'''