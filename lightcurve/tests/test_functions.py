"""
Test Misc functions

"""

from ..lightcurve import expand_refname
import os

#-------------------------------------------------------------------------------

def test_expand_refname():
    """  Test that i can accurately find the header reference file """

    assert expand_refname('lref$something_tds.fits') == 'something_tds.fits', \
        "Without lref, didn't return None"

    os.environ['lref'] = '/grp/hst/cdbs/lref/'
    full_refname = os.path.join( os.environ['lref'], 'something_tds.fits')
    assert expand_refname( 'lref$something_tds.fits' ) == full_refname, \
        "With lref, didn't find the file"

    assert expand_refname( '' ) == '', "didn't return blank on blank"

#-------------------------------------------------------------------------------