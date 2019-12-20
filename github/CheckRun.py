from __future__ import absolute_import

import github.GithubObject


class CheckRun(github.GithubObject.CompletableGithubObject):
    """
    This Class represents CheckRun. The reference can be found here https://developer.github.com/v3/checks/runs/
    """

    def __repr__(self):
        # TODO: Representation
        return self.get__repr__({})

