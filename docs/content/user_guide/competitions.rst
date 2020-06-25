Get Information About Competitions
==================================

If you want to retrieve information about a team's competition, you should
first determine a team's GUID, and then pass it to the following function:

.. autofunction:: bvlapi.get_competitions


It will return a list of competitions that the team with the given GUID is
part of. For each competition, you can access the competition's name, and
the standings among teams.

.. autoclass:: bvlapi.Competition
   :members:
   :undoc-members:


.. autoclass:: bvlapi.CompetitionStanding
   :members:
   :undoc-members:
