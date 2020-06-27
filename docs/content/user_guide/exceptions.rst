===============================================================================
Exceptions
===============================================================================

While using this package, several exceptions may be raised. Every exception
that is raised by this package will be derived from the following base class:

.. autoclass:: bvlapi.BvlApiException


There are also several situations where you may pass invalid parameters to one
of the package's functions. In such cases, there are typically guards in place
notify the user of their mistake.

.. autoclass:: bvlapi.InvalidGuid

.. autoclass:: bvlapi.LogoInvalidFileExtension


Whenever you use this package, there is always a possibility of things going
completely wrong due to the extensive reliance of I/O in the background. In
such cases, you can expect the following exceptions to be raised:

.. autoclass:: bvlapi.ApiCallFailed

.. autoclass:: bvlapi.FailedToGetLogo
