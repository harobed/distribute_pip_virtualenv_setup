#!python
import os, sys

def main():
    python_executable = os.environ['_']
    os.system('curl http://python-distribute.org/distribute_setup.py | %s' % python_executable)
    os.system('curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | %s' % python_executable)
    os.system(
        '%s/pip install virtualenv virtualenvwrapper' % 
        os.path.dirname(python_executable)
    )

if __name__ == '__main__':
    sys.exit(main())