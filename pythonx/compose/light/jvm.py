import os
import ctypes
os.environ['JAVA_HOME'] = os.path.join(os.getcwd(), "release", "runtime")
print("JVM Location:", os.environ['JAVA_HOME'])


if os.name == 'nt':
    ctypes.windll.user32.SetProcessDPIAware()


import jpype.imports
from jpype.types import *

jvm_options = [
    '-Dsun.java2d.uiScale=1.0',
    '-Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel',
    '-Dawt.useSystemAAFontSettings=on',
    '-Dswing.aatext=true'
]


def init_jvm():
    jpype.startJVM(classpath=["./build/libs/ComposeLight-1.0-all.jar", *jvm_options])

    from org.example.project import PlatformKt

    print("JVM Runtime Version:", PlatformKt.getPlatform().getName())
    print()
