===============================================================================
Get GUIDs
===============================================================================

To collect information about a basketball club or team, you need to determine
the relevant GUIDs first. This document outlines the structure of these GUIDs,
and how to find the GUIDs that you need.


-------------------------------------------------------------------------------
Structure of GUIDs
-------------------------------------------------------------------------------

Team GUID
~~~~~~~~~

A **team GUID** is a unique identifier that is used to identify a specific
basketball team. The GUID looks like 'BVBLXXXXCCC++T', where:

 - XXXX is a unique numeric club identifier (not the club's stamnummer!)
 - CCC is the age category (ex. HSE)
 - T is a numeric value that identifies different teams at the same club in
   the same age category (A->1,B->2,C->3,...)

For example, the GUID "BVBL1004HSE++2" is the GUID of the following team:

 - 1004 = Port of Antwerp Giants
 - HSE = Heren, Senioren (Male, Seniors)
 - 2 = Team B

Club GUID
~~~~~~~~~

A **club GUID** is similar to the Team GUIDs, but only consists of the first
part of a team's GUID, without the age category or team number.

For example, the GUID "BVBL1004" is the GUID of the Port of Antwerp Giants.

.. warning::
   The unique numeric club identifier of a GUID is completely arbitrary, so it
   is not the club's 'stamnummer'!


-------------------------------------------------------------------------------
How To Find Team GUIDs?
-------------------------------------------------------------------------------

These GUID can be determined manually by inspecting the actual service at the
following link:
https://www.basketbal.vlaanderen/competitie/resultaten-en-kalender

Use the website to find your team(s) of interest, and extract the GUID of the
team by using your browser's developer tools, or by inspecting the URLs. For
example, when you try to access the page with details about a team, the GUID
is in the URL:
https://vblweb.wisseq.eu/Home/TeamDetail?teamGuid=BVBL1328HSE%20%201
