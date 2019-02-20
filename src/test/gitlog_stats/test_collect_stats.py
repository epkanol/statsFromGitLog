
import unittest
from math import exp

import gitlog_stats.collect_stats

class test_collect_stats(unittest.TestCase):

    # preparatory lines
    preamble = ["commit f9c7e42261880778df9be7430986f2041012eec6",
                "Author: O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
                "Date:   2013-10-10"
                ]

    # message lines
    message2580 = ["    #2580 Just a message from a real commit"]
    mergemessage = ["    Merge with no tag marker at all"]

    # file examples
    srcfiles = ["emfc/src/main/java/com/O5Vj/TKfDe6gM4ihM5CdjRiidr57VGp2LEfWksZpOkE= | 21 +++++++++++++++------"]
    inttestfiles = [" emfc-bt/tests/nightly/TC_some_kind_of.xml | 16 ++++++++--------"]
    nofiles = ["version.properties | 2 +-"]

    # closing remarks
    postamble = [" 1 file changed, 1 insertion(+), 1 deletion(-)"]

    def assert_commitid(self, row, expected):
        self.assertEqual(expected, row[0], "commitid")

    def assert_author(self, row, expected):
        self.assertEqual(expected, row[1], "author")

    def assert_date(self, row, expected):
        self.assertEqual(expected, row[2], "date")

    def assert_changeid(self, row, expected):
        self.assertEqual(expected, row[3], "changeid")

    def assert_changetype(self, row, expected):
        self.assertEqual(expected, row[4], "changetype")

    def test_nothing_found(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.mergemessage + self.nofiles + self.postamble)
        self.assertListEqual(result, [])

    def test_nothing_found_src_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.mergemessage + self.srcfiles + self.postamble)
        self.assertListEqual(result, [])

    def test_found_one_commit_no_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.message2580 + self.nofiles + self.postamble)
        self.assert_commitid(result[0], "f9c7e42261880778df9be7430986f2041012eec6")
        self.assert_author(result[0], "O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=")
        self.assert_date(result[0], "2013-10-10")
        self.assert_changeid(result[0], "#2580")
        self.assert_changetype(result[0], "")
        self.assertListEqual(result, [
            ["f9c7e42261880778df9be7430986f2041012eec6",
             "O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
             "2013-10-10",
             "#2580",
             ""]
                             ])

    def test_found_one_commit_src_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.message2580 + self.srcfiles + self.postamble)
        self.assert_changetype(result[0], "code")
        self.assertListEqual(result, [
            ["f9c7e42261880778df9be7430986f2041012eec6",
             "O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
             "2013-10-10",
             "#2580",
             "code"]
                             ])

    def test_found_one_commit_inttest_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.message2580 + self.inttestfiles + self.postamble)
        self.assert_changetype(result[0], "integration test")
        self.assertListEqual(result, [
            ["f9c7e42261880778df9be7430986f2041012eec6",
             "O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
             "2013-10-10",
             "#2580",
             "integration test"]
                            ])
