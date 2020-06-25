===============================================================================
Documentation
===============================================================================

High-quality software requires proper documentation! For this reason, it is
very important that all code is accompanied by clear and concise documentation
that is up-to-date.


-------------------------------------------------------------------------------
Source Code Documentation
-------------------------------------------------------------------------------

At the very least, the following documentation should be added to source code:

* every module
    * short description of module's purpose/contents
    * long description that describes module in more detail
* global variables and constants
    * short description of purpose
* classes
    * short description of class
    * long description that describes class in more detail
    * class/instance members
* functions and methods
    * short description of function/method
    * type, name, and short description of each parameter
    * return value and return type
    * exceptions raised by function/methods


-------------------------------------------------------------------------------
Online Documentation
-------------------------------------------------------------------------------

The online documentation should feature the following four sections:

1. a user guide
    contains information aimed to help any users
2. a developer guide
    contains information aimed to help any developers
3. a code reference
    contains authoritative description of source code
4. history
    contains information about project's history and decisions


-------------------------------------------------------------------------------
Code Reference Documentation
-------------------------------------------------------------------------------

It is easy to use a tool to automatically extracts a code reference from
source code, but the result is often messy and cluttered. As such, it is
better to adhere the following guidelines:

* organize documentation of source code per topic
* write from a user's perspective in a way that is to a guide
* include code documentation in a granular way using Sphinx's autodoc:
    * automodule
    * autoclass
    * autofunction
    * ...
