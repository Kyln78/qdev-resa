import unittest
from resa.resa import *

class bookMeetingRoomUnitTests(unittest.TestCase):
  def test_small_room(self):
    self.assertEqual(bookMeetingRoom(5), Room.SMALL)
    self.assertEqual(bookMeetingRoom(10), Room.SMALL)
    self.assertEqual(bookMeetingRoom(18), Room.MEDIUM)
    self.assertEqual(bookMeetingRoom(46), Room.LARGE)
    self.assertEqual(bookMeetingRoom(60),  Room.REFUSE)
    self.assertRaises(ValueError, bookMeetingRoom, 0)


if __name__ == '__main__':
  unittest.main()
