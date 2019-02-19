
import unittest
import gitlog_stats.collect_stats

class test_collect_stats(unittest.TestCase):

    preamble = ["commit f9c7e42261880778df9be7430986f2041012eec6",
                "Author: O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
                "Date:   2013-10-10"
                ]
    message2580 = ["    #2580 Just a message from a real commit"]
    mergemessage = ["    Merge with no tag marker at all"]
    srcfiles = ["emfc/src/main/java/com/O5Vj/TKfDe6gM4ihM5CdjRiidr57VGp2LEfWksZpOkE= | 21 +++++++++++++++------"]
    inttestfiles = [" emfc-bt/tests/nightly/TC_some_kind_of.xml | 16 ++++++++--------"]

    nofiles = ["version.properties | 2 +-"]

    postamble = [" 1 file changed, 1 insertion(+), 1 deletion(-)"]


    def test_nothing_found(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.mergemessage + self.nofiles + self.postamble)
        self.assertListEqual(result, [])

    def test_nothing_found_src_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.mergemessage + self.srcfiles + self.postamble)
        self.assertListEqual(result, [])

    def test_found_one_commit_no_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.message2580 + self.nofiles + self.postamble)
        self.assertListEqual(result, [
            ["f9c7e42261880778df9be7430986f2041012eec6",
             "O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
             "2013-10-10",
             "#2580",
             ""]
                             ])

    def test_found_one_commit_src_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.message2580 + self.srcfiles + self.postamble)
        self.assertListEqual(result, [
            ["f9c7e42261880778df9be7430986f2041012eec6",
             "O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
             "2013-10-10",
             "#2580",
             "code"]
                             ])

    def test_found_one_commit_inttest_files(self):
        result = gitlog_stats.collect_stats.process(self.preamble + self.message2580 + self.inttestfiles + self.postamble)
        self.assertListEqual(result, [
            ["f9c7e42261880778df9be7430986f2041012eec6",
             "O7+Qei3vEC/1qgw+gKz0p5h0JnJxvpK0sd1XnwE1VOU=",
             "2013-10-10",
             "#2580",
             "integration test"]
                            ])
