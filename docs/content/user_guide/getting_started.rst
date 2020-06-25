===============================================================================
Getting Started
===============================================================================

-------------------------------------------------------------------------------
What is bvl-api?
-------------------------------------------------------------------------------

TODO


-------------------------------------------------------------------------------
Installation
-------------------------------------------------------------------------------

You can install this package using pip:

.. code-block:: sh

    $ python3 -m pip install --user bvl-api


-------------------------------------------------------------------------------
Retrieving Team GUID
-------------------------------------------------------------------------------

The GUID can be determined by using the actual service at the following link:
https://www.basketbal.vlaanderen/competitie/resultaten-en-kalender

Find your team(s) of interest, and extract the GUID of those teams by
using your browser's developer tools, or inspecting the URLs of different
pages.

The GUID looks like 'BVBLXXXXCCC++T', where:

 - XXXX is a unique numeric club identifier
 - CCC is the age category (ex. HSE)
 - T is a numeric value that identifies different teams at the same club in
   the same age category (A->1,B->2,C->3,...)

Note that the first number is not the club's stamnummer!

For example, the GUID "BVBL1004HSE++2" is the GUID of the following team:

 - 1004 = Port of Antwerp Giants
 - HSE = Heren, Senioren (Male, Seniors)
 - 2 = Team B

