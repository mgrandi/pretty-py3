from distutils.core import setup
setup(
    name='pretty-py3',
    author='Mark Grandi',
    author_email='markgrandi@gmail.com',
    version='0.2.2',
    url='https://github.com/mgrandi/pretty-py3',
    py_modules=['pretty'],
    description='extensible pprint successor - python3 version',
    long_description="""
Pretty
******

Python advanced pretty printer.  This pretty printer is intended to
replace the old `pprint` python module which does not allow developers
to provide their own pretty print callbacks.

This module is based on ruby's `prettyprint.rb` library by `Tanaka Akira`.


Example Usage
=============

To directly print the representation of an object use `pprint`::

    from pretty import pprint
    pprint(complex_object)

To get a string of the output use `pretty`::

    from pretty import pretty
    string = pretty(complex_object)


Extending
=========

The pretty library allows developers to add pretty printing rules for their
own objects.  This process is straightforward.  All you have to do is to
add a `__pretty__` method to your object and call the methods on the
pretty printer passed::

    class MyObject(object):

        def __pretty__(self, p, cycle):
            ...

Here the example implementation of a `__pretty__` method for a list
subclass::

    class MyList(list):

        def __pretty__(self, p, cycle):
            if cycle:
                p.text('MyList(...)')
            else:
                with p.group(8, 'MyList([', '])'):
                    for idx, item in enumerate(self):
                        if idx:
                            p.text(',')
                            p.breakable()
                        p.pretty(item)

The `cycle` parameter is `True` if pretty detected a cycle.  You *have* to
react to that or the result is an infinite loop.  `p.text()` just adds
non breaking text to the output, `p.breakable()` either adds a whitespace
or breaks here.  If you pass it an argument it's used instead of the
default space.  `p.pretty` prettyprints another object using the pretty print
method.

The first parameter to the `group` function specifies the extra indentation
of the next line. The second and the third parameter are the opening and 
closing strings that will be printed before and after the group.
In this example the next item will either be not
breaked (if the items are short enough) or aligned with the right edge of
the opening bracked of `MyList`.

:copyright: 2007 by Armin Ronacher.
:copyright: 2014 by Mark Grandi - python 3 port
:license: BSD License.
""",
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3'
    ]
)
