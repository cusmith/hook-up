# Copyright 2004-2013 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class Object(object):
    """
    Our own base class. Contains methods to simplify serialization.
    """

    __version__ = 0
    
    nosave = [ ]

    def __getstate__(self):
        rv = vars(self).copy()
        
        for f in self.nosave:
            if f in rv:
                del rv[f]


        rv["__version__"] = self.__version__
                
        return rv


    # None, to prevent this from being called when unnecessary.
    after_setstate = None

    def __setstate__(self, new_dict):

        version = new_dict.pop("__version__", 0)
        
        self.__dict__.update(new_dict)
        
        if version != self.__version__:
            self.after_upgrade(version) # E1101
            
        if self.after_setstate:
            self.after_setstate() # E1102

# We don't handle slots with this mechanism, since the call to vars should
# throw an error.
