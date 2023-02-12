# importing the ability to peform the test.
from jaseci.utils.test_core import CoreTest


class FileLibTest(CoreTest):

    fixture_src = __file__
    # fucntion that will test new feature
    def test_json_dump(self):
        #makes the api call to run the jac code which uses the new functionality .
        ret = self.call(
            self.mast,
            ["sentinel_register", {"code": self.load_jac("file_stuff.jac")}], # file_stuff.jac , the jac code being ran
        )
        ret = self.call(self.mast, ["walker_run", {"name": "pack_it"}])
        #running walker that was loaded from the JAC code
        self.assertEqual(ret["report"][0], {"hello": 5})
